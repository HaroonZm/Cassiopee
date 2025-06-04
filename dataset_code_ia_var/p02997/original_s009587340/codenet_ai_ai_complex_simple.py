from functools import reduce
from itertools import combinations, count, islice, cycle
import sys

N, K = map(int, input().split())

f = lambda x: reduce(lambda a, b: a*b, x, 1)
cnt = f(range(N-1, N-3, -1)) // 2

if cnt < K:
    print(-1)
    sys.exit()

edges = [list() for _ in range(N)]
list(map(lambda i: edges[0].append(i), range(1, N)))

def triangular_pairs(limit):
    def skip_diag(i, j): return i != j
    pairs = ((i, j) for i in range(1, N) for j in range(i+1, N) if skip_diag(i, j))
    return islice(pairs, limit)

list(map(lambda p: edges[p[0]].append(p[1]), triangular_pairs(cnt-K)))

M = sum(map(len, edges))
print(M)
[
    [print(u+1, v+1) for v in edges[u]]
        for u in range(N)
]