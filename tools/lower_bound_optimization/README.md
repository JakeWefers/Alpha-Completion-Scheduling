# Fractional-partition optimization

This directory contains the reproducible numerical experiment used to search
for large fractional-partition objective values.

## Files

- `simple_minlp.py` builds and solves the mixed-integer nonlinear program with
  PySCIPOpt. Its parameters are defined near the top of the script.
- `requirements.txt` records the Python dependency needed by the solver.
- `objective_results_table.tex` and
  `objective_results_table_50000_nodes.tex` are LaTeX tables produced from
  experiment runs; the PDF is a rendered preview.

## Run the experiment

From the repository root, create the local environment and install the solver:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r tools/lower_bound_optimization/requirements.txt
```

Then run:

```bash
.venv/bin/python tools/lower_bound_optimization/simple_minlp.py
```

Alternatively, open `simple_minlp.py` in VS Code and use the Python Run button.

Edit these values near the top of the file:

```python
m = 6
a = 1 / 4
b = 1.0
l_bound = 10.0
max_nodes = 10_000
```

The script automatically restarts with the repository's `.venv` interpreter
when it is launched from another Python environment.
