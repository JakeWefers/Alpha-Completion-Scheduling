# Thesis repository

This repository contains a TUM master's thesis on the approximation ratio of
the Largest-Ratio-First rule for total weighted alpha-completion-time
scheduling. The canonical document entry point is `master.tex`; the current
compiled thesis is `pdf/master.pdf`.

## Repository map

| Path | Purpose |
| --- | --- |
| `master.tex` | Main thesis document and the only canonical build entry point. |
| `literature.bib` | BibLaTeX bibliography database used by the thesis. |
| `tex/` | Standalone proofs, lemmas, figures, and exploratory chapter drafts. See `tex/README.md`. |
| `pdf/` | Compiled thesis and preview PDFs generated from TeX sources. See `pdf/README.md`. |
| `tools/` | Reproducible optimization and exploratory search programs. See `tools/README.md`. |
| `literature/` | External papers used as research references. |
| `images/` | Thesis-specific raster images. |
| `resources/` | Thesis-specific branding and visual resources. |
| `tum-templates/` | Vendored TUM LaTeX class, style, and template assets. |
| `.latexmkrc` | Shared `latexmk` output and temporary-file configuration. |
| `.vscode/` | Editor settings for consistent LaTeX builds. |

## Build

The project requires a TeX distribution with `latexmk`, `pdflatex`, and
`biber`. From the repository root, run:

```bash
latexmk master.tex
```

The final PDF is written to `pdf/master.pdf`. Auxiliary files are also written
to `pdf/`, but are ignored by Git. To remove generated build state, run:

```bash
latexmk -C master.tex
```

VS Code users can use the included LaTeX Workshop recipe. Generated auxiliary
files, local virtual environments, and operating-system metadata are ignored
by Git.

## Working conventions

- Keep thesis prose and structure in `master.tex`.
- Keep reusable or exploratory TeX material in `tex/`.
- Keep generated PDF previews only in `pdf/`.
- Keep research programs and their run instructions in `tools/`.
- Use descriptive `snake_case` names for new scripts and generated artifacts.
- Do not edit files in `tum-templates/` unless intentionally updating the
  vendored university template.
