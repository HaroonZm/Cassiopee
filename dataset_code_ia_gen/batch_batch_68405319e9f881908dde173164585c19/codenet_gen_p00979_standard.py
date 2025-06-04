import sys
sys.setrecursionlimit(10**7)

t = int(input())
if t == 0:
    print(0)
    exit()

from functools import lru_cache

@lru_cache(None)
def dfs(x):
    if x == 0:
        return 0
    res = x  # all normal speed
    if x % 3 == 0:
        res = min(res, dfs(x // 3) + 1)
    else:
        res = min(res, dfs(x - 1) + 1)
        if (x + 1) % 3 == 0:
            res = min(res, dfs((x + 1) // 3) + 2)
    return res

print(dfs(t))