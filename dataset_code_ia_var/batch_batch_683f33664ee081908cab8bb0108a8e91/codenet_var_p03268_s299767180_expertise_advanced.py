from sys import stdin
from functools import lru_cache

n, k = map(int, stdin.readline().split())
q, r = divmod(n, k)

@lru_cache(maxsize=None)
def count(x):
    return q + (1 if (x and x <= r) or (not x and r == k) else 0)

ans = sum(
    count(i) * count(-i % k) * count(-i % k)
    for i in range(k)
    if (2 * (-i % k)) % k == 0
)

print(ans)