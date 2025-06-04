import sys
from functools import lru_cache

sys.setrecursionlimit(10**6)

H, N = map(int, input().split())

P = [0] * H
for _ in range(N):
    x, y = map(int, input().split())
    P[y] |= 1 << x

combos = [(0b0011, 1), (0b0110, 1), (0b1100, 1), (0b1111, 2)]

@lru_cache(maxsize=None)
def dfs(i, state):
    if i == H - 1:
        return 0
    p = P[i + 1]
    s = state | p
    res = dfs(i + 1, p)
    for mask, val in combos:
        if s & mask == 0:
            res = max(res, dfs(i + 1, p | mask) + val)
    return res

print(dfs(0, P[0]))