#!/bin/sh

set -eu

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 path/to/document.tex" >&2
    exit 2
fi

source_file=$1
job_name=$(basename "$source_file" .tex)
project_dir=$(pwd)
build_dir="$project_dir/.latex-build"
publish_dir="$project_dir/pdf"
staged_pdf="$build_dir/$job_name.pdf"
published_pdf="$publish_dir/$job_name.pdf"
temporary_pdf="$publish_dir/.$job_name.pdf.tmp"

mkdir -p "$build_dir" "$publish_dir"

# Older universal Biber launchers use lipo -extract_family, which newer macOS
# versions no longer support. Use a cached native copy on Apple Silicon.
# Keep the installed TeX distribution untouched and refresh after upgrades.
if [ "$(uname -s)" = Darwin ] && [ "$(uname -m)" = arm64 ]; then
    biber_source=$(command -v biber || true)
    if [ -n "$biber_source" ] && /usr/bin/file "$biber_source" | /usr/bin/grep -q 'Mach-O universal binary'; then
        native_bin="$build_dir/bin"
        native_biber="$native_bin/biber"
        mkdir -p "$native_bin"
        if [ ! -x "$native_biber" ] || [ "$biber_source" -nt "$native_biber" ]; then
            /usr/bin/lipo "$biber_source" -thin arm64 -output "$native_biber.tmp"
            chmod +x "$native_biber.tmp"
            mv -f "$native_biber.tmp" "$native_biber"
        fi
        PATH="$native_bin:$PATH"
        export PATH
    fi
fi

build_staged_pdf() {
    latexmk \
        -norc \
        -synctex=1 \
        -interaction=nonstopmode \
        -halt-on-error \
        -file-line-error \
        -pdf \
        -outdir="$build_dir" \
        "$source_file" < /dev/null
}

# Keep the published PDF untouched while LaTeX is still writing. An
# interrupted editor build can leave a truncated AUX or BCF file behind, so
# retry once from clean staged state before reporting a source-level failure.
if ! build_staged_pdf; then
    echo "Initial build failed; clearing staged auxiliary files and retrying once." >&2
    latexmk -norc -C -outdir="$build_dir" "$source_file" || true
    build_staged_pdf
fi

if [ ! -s "$staged_pdf" ]; then
    echo "Build succeeded but did not create $staged_pdf" >&2
    exit 1
fi

# Rename on the same filesystem so readers see either the old complete PDF or
# the new complete PDF, never an in-progress copy.
cp "$staged_pdf" "$temporary_pdf"
mv -f "$temporary_pdf" "$published_pdf"

staged_synctex="$build_dir/$job_name.synctex.gz"
if [ -s "$staged_synctex" ]; then
    temporary_synctex="$publish_dir/.$job_name.synctex.gz.tmp"
    cp "$staged_synctex" "$temporary_synctex"
    mv -f "$temporary_synctex" "$publish_dir/$job_name.synctex.gz"
fi
