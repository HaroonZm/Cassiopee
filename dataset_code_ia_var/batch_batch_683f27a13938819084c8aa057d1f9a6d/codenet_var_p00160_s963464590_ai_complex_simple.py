from functools import reduce
from operator import add

compute = lambda x, y, h, w: next((v for (cond, v) in [
    (x+y+h <= 60 and w <= 2, 600),
    (x+y+h <= 80 and w <= 5, 800),
    (x+y+h <= 100 and w <= 10, 1000),
    (x+y+h <= 120 and w <= 15, 1200),
    (x+y+h <= 140 and w <= 20, 1400),
    (x+y+h <= 160 and w <= 25, 1600)
] if cond), 0)

aggregate = lambda n: reduce(add, (
    compute(*map(int, input().split()))
    for _ in range(n)
), 0)

import sys
from itertools import takewhile, accumulate, chain

inputs = iter(sys.stdin.readline, '')
outputs = list(
    accumulate(
        takewhile(lambda x: x != 0, map(int, inputs)),
        lambda acc, n: aggregate(n),
        initial=None
    )
)[1:]

print('\n'.join(map(str, outputs)))