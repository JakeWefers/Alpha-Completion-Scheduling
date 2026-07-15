# Vendored TUM template

This directory contains the university-provided document implementation and is
kept separate from thesis-authored material.

- `book/` provides the `tumbook` document class, package, and cover class.
- `commons/` provides shared layout, typography, color, language, logo, page,
  caption, author, and box packages.
- `commons/resources/` contains flags, logo imagery, and the ORCID mark used by
  the template.

Treat these files as vendored dependencies. Thesis-specific settings belong in
`master.tex`; update this directory only when intentionally upgrading the TUM
template.
