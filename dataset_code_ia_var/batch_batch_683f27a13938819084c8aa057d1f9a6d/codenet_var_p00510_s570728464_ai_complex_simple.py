from functools import reduce
from itertools import accumulate, chain
from operator import add, sub
import sys

n = int(input())
m = int(input())

changes = list(accumulate(
    chain([(0, 0)], (tuple(map(int, input().split())) for _ in range(n))),
    lambda acc, x: (acc[0]+x[0], acc[1]+x[1])
))

balances = list(
    accumulate(
        ((a-b,) for a, b in (x for x in changes)),
        lambda current, step: (current[0] + step[0],)
    )
)

snapshots = list(map(lambda x: m + x[0], balances))

next(
    filter(lambda pair: sys.exit(0) if pair[1] < 0 else False, enumerate(snapshots[1:]),),
    None
)

print(max(snapshots))