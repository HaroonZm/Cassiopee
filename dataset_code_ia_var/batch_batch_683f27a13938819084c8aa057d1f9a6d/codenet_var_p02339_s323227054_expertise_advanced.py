import sys
from functools import lru_cache
from operator import mul
from functools import reduce

sys.setrecursionlimit(10_000_000)

MOD = 10**9 + 7

n, k = map(int, input().split())

@lru_cache(maxsize=None)
def comb(N, K):
    if K < 0 or K > N:
        return 0
    if K == 0 or K == N:
        return 1
    return (comb(N - 1, K - 1) + comb(N - 1, K)) % MOD

@lru_cache(maxsize=None)
def mod_pow(base, exp):
    result = 1
    base %= MOD
    while exp:
        if exp & 1:
            result = result * base % MOD
        base = base * base % MOD
        exp >>= 1
    return result

@lru_cache(maxsize=None)
def inv(N):
    return mod_pow(N, MOD - 2)

def multinom_fact(N):
    res = 1
    for i in range(2, N + 1):
        res = res * i % MOD
    return res

# Compute sum_{i=0}^k (-1)^i * C(k,i) * i^n
terms = ((-1) ** (k - i) * comb(k, i) * mod_pow(i, n)) % MOD for i in range(k + 1)
total = sum(terms) % MOD

# Divide by k! (multinomial coefficient denominator)
for i in range(1, k + 1):
    total = total * inv(i) % MOD

print(total)