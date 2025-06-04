import sys
from functools import lru_cache
from math import isqrt

@lru_cache(maxsize=None)
def f(b, n):
    if n < b:
        return n
    q, r = divmod(n, b)
    return f(b, q) + r

n, s = map(int, sys.stdin.readline), map(int, sys.stdin.readline)
n, s = int(next(n)), int(next(s))

if n == s:
    print(n + 1)
    sys.exit(0)

limit = isqrt(n)
for b in range(2, limit + 1):
    if f(b, n) == s:
        print(b)
        sys.exit(0)

for p in range(1, limit + 1):
    if (n - s) % p != 0:
        continue
    b = (n - s) // p + 1
    if limit < b <= n and f(b, n) == s:
        print(b)
        sys.exit(0)
print(-1)