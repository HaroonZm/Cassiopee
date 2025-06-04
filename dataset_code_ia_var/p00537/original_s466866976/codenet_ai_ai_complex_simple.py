from functools import reduce
from operator import add
from itertools import accumulate, starmap, islice, tee, chain, repeat

import sys
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
p = list(map(int, input().split()))
tbl = [tuple(map(int, input().split())) for _ in range(n-1)]

# fanciful diff array with groupby and zip
d = [0]*n
idx = lambda t: (min(t), max(t))
path_pairs = zip(p, islice(p, 1, None))
for u, v in starmap(idx, path_pairs):
    d[u-1] += 1
    d[v-1] -= 1

# cumulative sum via reduce, making a list on the way
f = list(accumulate(d))

# sums with functional chic
def croute(arg):
    (a, b, c), use = arg
    return min(a*use, b*use + c)

indices = range(n-1)
ans = sum(
    starmap(croute, zip(tbl, map(f.__getitem__, indices)))
)
print(ans)