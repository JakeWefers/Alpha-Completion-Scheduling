# Compiled PDF catalog

This directory contains generated previews. `master.pdf` is the compiled
thesis; the other PDFs correspond to standalone material in `tex/` or to
computational experiments. TeX sources, rather than PDFs, are authoritative.

Names beginning with `root-` are older root-level build variants retained for
comparison. Files ending in `_legacy` are explicitly preserved earlier
versions. Auxiliary LaTeX files are ignored and should not be committed.

The principal groups are:

- `SchwCorr*.pdf` and `SchwiegelshohnRaw.pdf`: source-proof reconstructions.
- `*UpperBound*.pdf`, `*Bound*.pdf`, and `ratio_factor_bound.pdf`: bound proofs.
- `*Schedule*.pdf`, `ComputationalFigure.pdf`, and `EveningMachineLoad.pdf`:
  diagrams and illustrative schedules.
- `objective_*.pdf`, `lambda_mu_conditions.pdf`, and
  `parameter_improvements.pdf`: computational and parameter studies.
- `NewLowerBoundFamily.pdf` and `UnboundedInstance.pdf`: lower-bound examples.

Files with a direct counterpart in `tex/` are rendered previews of that source.
Additional files have these roles:

- `master.pdf`: canonical compiled thesis.
- `GeneralUpperBound.pdf`: preview of the general observations draft.
- `KnownUpperBound.pdf` and `mKnownUpperBound.pdf`: known-bound previews.
- `LocalExchange.pdf`: local-exchange proof preview.
- `M2UpperBoundNoJobZero.pdf` and `M2UpperBoundOneJobZero.pdf`: two-machine
  case previews.
- `MaxOfLambda.pdf`: lambda maximization preview; `max_of_lambda_legacy.pdf`
  preserves an earlier rendering.
- `PeakIsGood.pdf`: peak-structure proof preview.
- `unification_lemma.pdf`: corrected-name preview;
  `unification_lemma_legacy.pdf` preserves an earlier rendering.
- `new_upper_bound.pdf`, `m_upper_bound.pdf`, and
  `strict_upper_bound_proof.pdf`: upper-bound proof variants.
- `bCutBound.pdf`: b-cut proof preview.
- `objective_grid_m3_m7_l30_n20000.pdf`: finite objective-grid experiment.
- `root-M2UpperBoundNoJobZero.pdf`, `root-M2UpperBoundOneJobZero.pdf`,
  `root-SingleScheduleMachine.pdf`, and `root-m3SpecialCaseBound.pdf`: retained
  outputs from the former root-level build layout.
