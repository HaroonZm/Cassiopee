from functools import reduce
from itertools import product, combinations
import operator

INF = float("inf")

def deep_clone(obj):
    return eval(repr(obj))

def warshall_floyd(matrix):
    n = len(matrix)
    dist = deep_clone(matrix)
    indices = range(n)
    def update(i, j, k):
        if dist[i][j] > dist[i][k] + dist[k][j]:
            dist[i][j] = dist[i][k] + dist[k][j]
    list(map(lambda k: list(map(lambda i: list(map(lambda j: update(i, j, k), indices)), indices)), indices))
    return dist

n = int(input())
d = [list(map(int,input().split())) for _ in range(n)]
floyd = warshall_floyd(d)

if any(any(x != y for x, y in zip(rowd, rowf)) for rowd, rowf in zip(d, floyd)):
    print(-1)
else:
    def is_direct(i, j):
        return all(d[i][mid] + d[mid][j] > d[i][j] or mid in (i, j) for mid in range(n))
    pairs = [(i,j) for i in range(n) for j in range(i+1, n)]
    ret = sum(d[i][j] * is_direct(i, j) for i, j in pairs)
    print(ret)