from sys import stdin
from functools import lru_cache
from operator import mul
from itertools import accumulate

input = stdin.readline

mod = 10 ** 9 + 7

N, M = map(int, input().split())

# Efficient factorial and invfactorial using precomputation
MAXN = M + 10

# Precompute factorials and inverses
fact = [1] * MAXN
invfact = [1] * MAXN

for i in range(1, MAXN):
    fact[i] = fact[i - 1] * i % mod
invfact[MAXN - 1] = pow(fact[MAXN - 1], mod - 2, mod)
for i in range(MAXN - 2, -1, -1):
    invfact[i] = invfact[i + 1] * (i + 1) % mod

def comb(n, k):
    if not 0 <= k <= n:
        return 0
    return fact[n] * invfact[k] % mod * invfact[n - k] % mod

# Inclusion-Exclusion Principle for derangements
res = sum(
    (1 if k % 2 == 0 else -1) * comb(N, k) * fact[M - k] % mod
    for k in range(N + 1)
) * invfact[M - N] % mod
print(res if res >= 0 else res + mod)