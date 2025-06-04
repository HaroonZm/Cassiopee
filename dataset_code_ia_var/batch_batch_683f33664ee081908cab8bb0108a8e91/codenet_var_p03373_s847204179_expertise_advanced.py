from operator import mul
from functools import partial

*a, = map(int, input().split())
a1, b1, c1, x1, y1 = a

costs = (
    a1 * x1 + b1 * y1,
    2 * c1 * min(x1, y1) + (a1 * (x1 - y1) if x1 > y1 else b1 * (y1 - x1) if x1 < y1 else 0),
    2 * c1 * max(x1, y1)
)

print(min(costs))