from sys import stdin
from functools import lru_cache
from operator import mul
from itertools import accumulate

n, k = map(int, stdin.readline().split())
mod = 10**9 + 7
MAX_N = 10**6 + 5

fact = [1] + [0]*MAX_N
for i in range(1, MAX_N+1):
    fact[i] = fact[i-1] * i % mod

fact_inv = [1] * (MAX_N+1)
fact_inv[MAX_N] = pow(fact[MAX_N], mod-2, mod)
for i in range(MAX_N-1, -1, -1):
    fact_inv[i] = fact_inv[i+1] * (i+1) % mod

@lru_cache(maxsize=None)
def mod_comb_k(n, k):
    if k < 0 or k > n: return 0
    return fact[n] * fact_inv[k] % mod * fact_inv[n - k] % mod

if k >= n:
    print(mod_comb_k(2*n - 1, n))
else:
    res = 1 + sum((mod_comb_k(n, i) * mod_comb_k(n-1, n-i-1)) % mod for i in range(1, k+1))
    print(res % mod)