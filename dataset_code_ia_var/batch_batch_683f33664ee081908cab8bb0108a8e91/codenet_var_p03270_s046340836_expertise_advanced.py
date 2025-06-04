from functools import lru_cache
from operator import mul
from sys import stdin

K, N = map(int, stdin.readline().split())
MOD = 998244353
MAX = 2 * K + N + 10

# Pré-calcul des factorielles et inverses
fact = [1]
for i in range(1, MAX):
    fact.append(fact[-1] * i % MOD)

factinv = [1] * MAX
factinv[MAX-1] = pow(fact[MAX-1], MOD-2, MOD)
for i in range(MAX-2, -1, -1):
    factinv[i] = factinv[i+1] * (i+1) % MOD

def ncr(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * factinv[r] % MOD * factinv[n - r] % MOD

def nhr(n, r):
    if n == 0 and r == 0:
        return 1
    return ncr(n + r - 1, r) if n + r - 1 >= 0 and r >= 0 else 0

pow2 = [1] * (MAX)
for i in range(1, MAX):
    pow2[i] = pow2[i-1] * 2 % MOD

for i in range(2, 2*K+1):
    if i % 2 == 0:
        np = i//2 - max(i-1-K, 0) - 1
        ans = 0
        nr = K - np*2 - 1
        for nq in range(np+1):
            coef = ncr(np, nq) * pow2[nq] % MOD
            t = coef * nhr(nr + nq, N - nq) % MOD
            t += coef * nhr(nr + nq, N - nq - 1) % MOD
            ans = (ans + t) % MOD
    else:
        np = i//2 - max(i-1-K, 0)
        ans = 0
        nr = K - np*2
        for nq in range(np+1):
            coef = ncr(np, nq) * pow2[nq] % MOD
            t = coef * nhr(nr + nq, N - nq) % MOD
            ans = (ans + t) % MOD
    print(ans)