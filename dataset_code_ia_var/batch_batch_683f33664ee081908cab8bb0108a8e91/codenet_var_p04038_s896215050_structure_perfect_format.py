import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np

N, K = map(int, read().split())

if K == 1:
    print(1)
    exit()

MOD = 10 ** 9 + 7

def cumprod(A, MOD=MOD):
    L = len(A)
    Lsq = int(L ** .5 + 1)
    A = np.resize(A, Lsq ** 2).reshape(Lsq, Lsq)
    for n in range(1, Lsq):
        A[:, n] *= A[:, n - 1]
        A[:, n] %= MOD
    for n in range(1, Lsq):
        A[n] *= A[n - 1, -1]
        A[n] %= MOD
    return A.ravel()[:L]

def make_fact(U, MOD=MOD):
    x = np.arange(U, dtype=np.int64)
    x[0] = 1
    fact = cumprod(x, MOD)
    x = np.arange(U, 0, -1, dtype=np.int64)
    x[0] = pow(int(fact[-1]), MOD - 2, MOD)
    fact_inv = cumprod(x, MOD)[::-1]
    return fact, fact_inv

U = (N + 10) * (K + 10)
fact, fact_inv = make_fact(U)

dp = np.array([0, 1], np.int64)
for n in range(2, N + 1):
    prev = dp
    dp = np.zeros(n + 1, np.int64)
    S = prev.sum() % MOD
    np.cumsum(prev, out=prev)
    prev %= MOD
    dp[1] = S
    dp[2:] = S - prev[:-1]
    coef = fact[n * (K - 1) - 1:n * K][::-1].copy()
    coef *= fact_inv[K - 2]
    coef %= MOD
    coef *= fact_inv[(n - 1) * (K - 1):(n - 1) * K + 2][::-1]
    coef %= MOD
    dp *= coef
    dp %= MOD

answer = dp.sum() % MOD
answer *= fact[N]
answer %= MOD
print(answer)