"""A compact, direct SCIP formulation of the fractional partition MINLP."""

import os
import sys
from pathlib import Path
from pprint import pprint

# Use the Thesis-Template project's Python environment automatically.
project_python = Path(__file__).resolve().parents[2] / ".venv" / "bin" / "python"
project_environment = project_python.parent.parent
if Path(sys.prefix).resolve() != project_environment.resolve():
    if not project_python.exists():
        raise RuntimeError(f"Project Python was not found at {project_python}")
    os.execv(str(project_python), [str(project_python), str(Path(__file__).resolve())])

from pyscipopt import Model, quicksum


m = 9
a = 1 / 2
b = 1.0
l_bound = 10.0
max_nodes = 50_000
epsilon = 1.0e-5
zero_tolerance = 1.0e-7

if a <= 0:
    raise ValueError("The objective upper bound 1 + 1/(6a) requires a > 0.")

objective_upper_bound = 1 + 1 / (6 * a)


model = Model("simple_fractional_partition")
model.setParam("limits/nodes", max_nodes)

# Continuous variables p[i,j] and l[i].
p = {
    (i, j): model.addVar(lb=0.0, ub=b, name=f"p_{i + 1}_{j + 1}")
    for i in range(m)
    for j in range(m)
}
l = {
    i: model.addVar(lb=0.0, ub=l_bound, name=f"l_{i + 1}")
    for i in range(m)
}

# Put all p and l variables into one list so they can be partitioned.
items = [p[i, j] for i in range(m) for j in range(m)] + [l[i] for i in range(m)]
item_names = [
    f"p_{i + 1}_{j + 1}" for i in range(m) for j in range(m)
] + [f"l_{i + 1}" for i in range(m)]

# x[k,g] = 1 exactly when item k belongs to partition group g.
x = {
    (k, g): model.addVar(vtype="B", name=f"x_{k + 1}_{g + 1}")
    for k in range(len(items))
    for g in range(m)
}

# P[g] is the sum of the item values assigned to group g.
P = {
    g: model.addVar(
        lb=epsilon,
        ub=m * b + m * l_bound,
        name=f"P_{g + 1}",
    )
    for g in range(m)
}

# Each row of p sums to b.
for i in range(m):
    model.addCons(quicksum(p[i, j] for j in range(m)) == b)

# Every item is assigned to exactly one partition group.
for k in range(len(items)):
    model.addCons(quicksum(x[k, g] for g in range(m)) == 1)

# Define each group sum and require every group to have positive total value.
for g in range(m):
    model.addCons(
        P[g] == quicksum(x[k, g] * items[k] for k in range(len(items)))
    )

# Remove equivalent solutions obtained only by renaming partition groups.
model.addCons(x[0, 0] == 1)
for g in range(1, m):
    model.addCons(x[0, g] == 0)
for k in range(1, len(items)):
    for g in range(1, m):
        model.addCons(x[k, g] <= quicksum(x[h, g - 1] for h in range(k)))

# Build the numerator and denominator of the fractional objective.
c = 2 * a - 1
squares = (
    quicksum(p[i, j] * p[i, j] for i in range(m) for j in range(m))
    + quicksum(l[i] * l[i] for i in range(m))
)
numerator = quicksum((l[i] + b) * (l[i] + b) for i in range(m)) + c * squares
denominator = quicksum(P[g] * P[g] for g in range(m)) + c * squares

# Maximize r subject to r * denominator <= numerator.
# The proven bound r <= 1 + 1/(6a) gives SCIP a much tighter search region.
r = model.addVar(
    lb=0.0,
    ub=objective_upper_bound,
    name="objective_ratio",
)
model.addCons(denominator >= epsilon)
model.addCons(r * denominator <= numerator)
model.setObjective(r, "maximize")

model.optimize()

if model.getNSols() == 0:
    raise RuntimeError(f"SCIP found no solution. Status: {model.getStatus()}")

solution = model.getBestSol()
p_values = [
    [model.getSolVal(solution, p[i, j]) for j in range(m)]
    for i in range(m)
]
l_values = [model.getSolVal(solution, l[i]) for i in range(m)]
P_values = [model.getSolVal(solution, P[g]) for g in range(m)]
groups = [[] for _ in range(m)]
for k, name in enumerate(item_names):
    group = max(range(m), key=lambda g: model.getSolVal(solution, x[k, g]))
    groups[group].append(name)


def clean_near_zero(value):
    """Display tiny numerical errors as exactly zero."""
    return 0.0 if abs(value) <= zero_tolerance else value


cleaned_p_values = [
    [clean_near_zero(value) for value in row]
    for row in p_values
]
cleaned_l_values = [clean_near_zero(value) for value in l_values]
cleaned_P_values = [clean_near_zero(value) for value in P_values]

print("\nSCIP status:", model.getStatus())
print("Objective:", model.getSolVal(solution, r))
print("\nRaw p values:")
pprint(p_values)
print("Raw l values:", l_values)
print("Raw group sums P:", P_values)

print(f"\nCleaned values (absolute value <= {zero_tolerance:g} becomes 0):")
print("Cleaned p values:")
pprint(cleaned_p_values)
print("Cleaned l values:", cleaned_l_values)
print("Cleaned group sums P:", cleaned_P_values)

print("Partition groups:")
pprint(groups)
