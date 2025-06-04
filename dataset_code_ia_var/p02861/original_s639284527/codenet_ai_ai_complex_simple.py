from functools import reduce
from itertools import product, chain
import sys
import math

input = sys.stdin.readline

N, *_ = map(int, [input()] + [''])
xy = [tuple(map(int, input().split())) for _ in range(N)]

pairs = filter(lambda t: t[0] != t[1], product(range(N), repeat=2))

sm = reduce(
    lambda acc, ij: acc + math.hypot(*(a-b for a, b in zip(xy[ij[0]], xy[ij[1]]))),
    pairs,
    0
)

print((lambda s, n: (lambda: s/n)())(sm, N))