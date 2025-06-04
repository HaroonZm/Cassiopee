from functools import lru_cache
from operator import mul
from itertools import accumulate

n, k = map(int, input().split())
mod = 10**9 + 7
max_m = min(n - 1, k)

# Precompute factorials and inverse factorials with accumulate for efficiency
f = [1, *accumulate(range(1, n + 1), lambda x, y: x * y % mod)]
fi = [pow(f[-1], mod - 2, mod)]
for x in reversed(f[1:-1]):
    fi.append(fi[-1] * x % mod)
fi = fi[::-1]

def comb_mod(n, r):
    if r < 0 or r > n: return 0
    return f[n] * fi[r] % mod * fi[n - r] % mod

ans = sum(comb_mod(n, m) * comb_mod(n - 1, m) % mod for m in range(max_m + 1)) % mod
print(ans)