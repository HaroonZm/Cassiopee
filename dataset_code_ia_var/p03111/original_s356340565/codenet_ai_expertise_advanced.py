import sys
from functools import lru_cache

sys.setrecursionlimit(1 << 25)
INF = 10 ** 9
n, a, b, c = map(int, input().split())
l = [int(input()) for _ in range(n)]

@lru_cache(maxsize=None)
def dfs(i, x, y, z, m):
    if i == n:
        return abs(x - a) + abs(y - b) + abs(z - c) + m if all((x, y, z)) else INF

    choices = [
        dfs(i + 1, x + l[i] if x else l[i], y, z, m + 10 if x else m),
        dfs(i + 1, x, y + l[i] if y else l[i], z, m + 10 if y else m),
        dfs(i + 1, x, y, z + l[i] if z else l[i], m + 10 if z else m),
        dfs(i + 1, x, y, z, m)
    ]
    return min(choices)

print(dfs(0, 0, 0, 0, 0))