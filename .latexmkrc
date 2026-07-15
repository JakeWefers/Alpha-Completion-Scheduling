$out_dir = 'pdf';
$aux_dir = '.latex-build';

# Keep generated LaTeX state disposable. Interrupted editor builds can leave
# truncated .aux/.bcf files or a stale synctex(busy) marker, which then makes
# later builds look like they are stuck. Rebuild master from clean generated
# state each time; the final PDF remains in pdf/.
use File::Find;
use File::Path qw(make_path);

make_path($out_dir) unless -d $out_dir;
make_path($aux_dir) unless -d $aux_dir;

find(
    sub {
        return unless -f $_ && /\.synctex\(busy\)\z/;
        unlink $File::Find::name;
    },
    '.'
);

for my $dir ($aux_dir, '.') {
    for my $ext (qw(aux bbl bcf blg fdb_latexmk fls lof log lot out run.xml synctex synctex.gz toc)) {
        my $file = "$dir/master.$ext";
        unlink $file if -e $file;
    }
}

$pdf_mode = 1;
$pdflatex = 'pdflatex -synctex=1 -interaction=nonstopmode -file-line-error %O %S';
