$out_dir = 'pdf';
$aux_dir = $out_dir;

# This TeX Live version does not support pdflatex's newer -aux-directory
# option, so auxiliary state and final PDFs both go to pdf/. Git ignores the
# auxiliary extensions, while latexmk retains them for fast incremental builds.
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

$pdf_mode = 1;
$max_repeat = 5;
$pdflatex = 'pdflatex -synctex=1 -interaction=nonstopmode -file-line-error %O %S';
