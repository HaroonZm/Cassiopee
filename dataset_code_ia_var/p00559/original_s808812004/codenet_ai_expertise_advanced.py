from sys import stdin
from itertools import accumulate

def compute_cost(val, s, t):
    return -val * (s if val > 0 else t)

n, q, s, t = map(int, next(stdin).split())
a = [int(next(stdin)) for _ in range(n + 1)]
diffs = [a[0], *(a[i] - a[i - 1] for i in range(1, n + 1))]
cost = sum(map(lambda v: compute_cost(v, s, t), diffs))

for _ in range(q):
    l, r, x = map(int, next(stdin).split())
    for idx in (l, r + 1):
        if idx <= n:
            old = diffs[idx]
            if idx == l:
                diffs[idx] += x
            else:
                diffs[idx] -= x
            cost += compute_cost(diffs[idx], s, t) - compute_cost(old, s, t)
    print(cost)