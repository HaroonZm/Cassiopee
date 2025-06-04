from operator import mul
from functools import reduce, partial
import sys

N, K = map(int, sys.stdin.readline().split())

comb = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // reduce(mul, range(1, r + 1), 1) if 0 <= r <= n else 0

lim = comb(N - 1, 2)
if K > lim:
    print(-1)
    sys.exit()

edges = list(map(lambda i: (1, i), range(2, N + 1)))
pairs = ((i, j) for i in range(2, N + 1) for j in range(i + 1, N + 1))
slim = lim - K
edges2 = [p for idx, p in enumerate(pairs) if idx < slim]
edges.extend(edges2)
print(len(edges))
print('\n'.join(map(lambda uv: f"{uv[0]} {uv[1]}", edges)))