from functools import reduce
from operator import mul

s = int(input())
mod = 10**9 + 7

def nCr(n, r):
    return reduce(lambda x, y: x * y % mod, range(n, n - r, -1), 1) * pow(reduce(mul, range(1, r + 1), 1), -1, mod) % mod if 0 <= r <= n else 0

ans = sum(nCr(s - 2 * l - 1, l - 1) for l in range(1, 1000) if s - 2 * l - 1 >= 0) % mod

print(ans)