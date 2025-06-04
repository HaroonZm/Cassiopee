import sys

sys.setrecursionlimit(10**5)
from functools import lru_cache

mod = 10**9 + 7

@lru_cache(maxsize=None)
def expsq(n, k):
    if k == 0:
        return 1
    if k & 1 == 0:
        half = expsq(n, k >> 1)
        return pow(half, 2, mod)
    else:
        return (n * expsq(n, k - 1)) % mod

m, n = map(int, raw_input().split())
print(expsq(m, n) % mod)