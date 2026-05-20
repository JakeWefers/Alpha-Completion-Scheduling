import random


NAMES = ["a1", "b", "a2", "c1", "d", "c2", "e1", "f", "e2"]
P_VALUES = [0.01, 0.05, 0.1, 0.25, 0.5]


def positive(value, eps=1e-12):
    return value > eps


def feasible(x, eps=1e-9):
    a1, b, a2, c1, d, c2, e1, f, e2 = x
    A = a1 + b + a2
    C = c1 + d + c2
    E = e1 + f + e2
    L = a1 + c1 + e1
    M = b + d + f
    R = a2 + c2 + e2

    if min(x) < -eps:
        return False

    def pos(value):
        return positive(value, eps)

    if pos(b) and not pos(a1):
        return False
    if pos(a2) and not pos(b):
        return False
    if pos(d) and not pos(c1):
        return False
    if pos(c2) and not pos(d):
        return False
    if pos(f) and not pos(e1):
        return False
    if pos(e2) and not pos(f):
        return False

    if pos(b) and (C + eps < a1 or E + eps < a1):
        return False
    if pos(d) and (A + eps < c1 or E + eps < c1):
        return False
    if pos(f) and (C + eps < e1 or A + eps < e1):
        return False

    if pos(a2) and (C + eps < a1 + b or E + eps < a1 + b):
        return False
    if pos(c2) and (A + eps < c1 + d or E + eps < c1 + d):
        return False
    if pos(e2) and (A + eps < e1 + f or C + eps < e1 + f):
        return False

    if pos(a1) and pos(c1) and (M + eps < a1 or R + eps < a1):
        return False
    if pos(b) and pos(d) and (L + eps < b or R + eps < b):
        return False
    if pos(a2) and pos(c2) and (L + eps < a2 or M + eps < a2):
        return False

    if pos(a1) and pos(c1) and pos(e1) and (
        M + eps < a1 + c1 or R + eps < a1 + c1
    ):
        return False
    if pos(b) and pos(d) and pos(f) and (
        L + eps < b + d or R + eps < b + d
    ):
        return False
    if pos(a2) and pos(c2) and pos(e2) and (
        M + eps < a2 + c2 or L + eps < a2 + c2
    ):
        return False

    return True


def objective(x, p):
    a1, b, a2, c1, d, c2, e1, f, e2 = x
    rows = [a1 + b + a2, c1 + d + c2, e1 + f + e2]
    cols = [a1 + c1 + e1, b + d + f, a2 + c2 + e2]
    norm = sum(value * value for value in x)
    q = 2 * p - 1
    denominator = sum(value * value for value in cols) + q * norm
    numerator = sum(value * value for value in rows) + q * norm
    if denominator <= 1e-12:
        return None
    return numerator / denominator


def sample_from_support(lengths):
    x = []
    for length in lengths:
        row = [random.random() ** 2 for _ in range(length)]
        row += [0.0] * (3 - length)
        x.extend(row)

    total = sum(x)
    if total == 0:
        return None
    return tuple(value / total for value in x)


def support_names(lengths):
    active = []
    inactive = []
    for row, length in enumerate(lengths):
        for col in range(3):
            name = NAMES[3 * row + col]
            if col < length:
                active.append(name)
            else:
                inactive.append(name)
    return active, inactive


def main(samples_per_support=5000):
    best = {p: (0.0, None, None) for p in P_VALUES}

    for l1 in range(4):
        for l2 in range(4):
            for l3 in range(4):
                lengths = (l1, l2, l3)
                for _ in range(samples_per_support):
                    x = sample_from_support(lengths)
                    if x is None or not feasible(x, 1e-12):
                        continue
                    for p in P_VALUES:
                        value = objective(x, p)
                        if value is not None and value > best[p][0]:
                            best[p] = (value, lengths, x)

    print("Best observed support for each p")
    print("=" * 40)
    for p in P_VALUES:
        value, lengths, x = best[p]
        active, inactive = support_names(lengths)
        rounded = tuple(round(entry, 8) for entry in x)
        print(f"p={p}: value={value:.12f}")
        print(f"  {lengths}: active={active},")
        print(f"  inactive={inactive}")
        print(f"  x={rounded}")
        print()


if __name__ == "__main__":
    main()
