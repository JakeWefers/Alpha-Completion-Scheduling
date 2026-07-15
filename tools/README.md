# Research tools

- `lower_bound_optimization/` contains the PySCIPOpt fractional-partition
  model, its dependency declaration, result tables, and detailed run guide.
- `exploratory_support_search.py` performs a randomized search over support
  patterns for the three-by-three structural model. It uses only Python's
  standard library and prints the best observed support for each configured
  parameter value.

Run the exploratory search from the repository root with:

```bash
python3 tools/exploratory_support_search.py
```
