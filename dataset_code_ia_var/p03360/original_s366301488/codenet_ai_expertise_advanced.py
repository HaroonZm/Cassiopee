from functools import lru_cache
from operator import mul
from itertools import starmap

A, B, C = map(int, input().split())
K = int(input())
vals = (A, B, C)

@lru_cache(maxsize=None)
def dfs(i, a, b, c):
    if i == K:
        return sum(starmap(mul, zip(vals, (1 << a, 1 << b, 1 << c))))
    return max(
        dfs(i + 1, a + 1, b, c),
        dfs(i + 1, a, b + 1, c),
        dfs(i + 1, a, b, c + 1),
    )

print(dfs(0, 0, 0, 0))