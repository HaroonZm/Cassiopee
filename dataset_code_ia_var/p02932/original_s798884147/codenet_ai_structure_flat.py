import sys
input = sys.stdin.readline

import numpy as np

N, M, L, R = map(int, input().split())

MOD = 10 ** 9 + 7

X = 1000
fact = np.arange(X * X, dtype=np.int64).reshape(X, X)
fact[0, 0] = 1

n = 1
while n < X:
    fact[:, n] *= fact[:, n - 1]
    fact[:, n] %= MOD
    n += 1

n = 1
while n < X:
    fact[n] *= fact[n - 1, -1]
    fact[n] %= MOD
    n += 1

fact = fact.ravel()

fact_inv = np.arange(1, X * X + 1, dtype=np.int64)[::-1].reshape(X, X)
fact_inv[0, 0] = pow(int(fact[-1]), MOD - 2, MOD)

n = 1
while n < X:
    fact_inv[:, n] *= fact_inv[:, n - 1]
    fact_inv[:, n] %= MOD
    n += 1

n = 1
while n < X:
    fact_inv[n] *= fact_inv[n - 1, -1]
    fact_inv[n] %= MOD
    n += 1

fact_inv = fact_inv.ravel()[::-1]

U = N - M
comb = fact[U] * fact_inv[:U + 1] % MOD * fact_inv[U::-1] % MOD
comb[1::2] *= (-1)

P = np.zeros(R + 1, dtype=np.int64)
i = 0
for x in comb:
    idx = M + i
    P[::idx] += x
    i += 1

P[:M - 1:-1] -= P[-M - 1::-1]
P %= MOD

Q = fact[N:N + R + 1] * fact_inv[:R + 1] % MOD * fact_inv[N] % MOD

R0 = R
total = fact[R0 + N] * fact_inv[R0] % MOD * fact_inv[N] % MOD
x = Q[R0::-1] * P[:R0 + 1] % MOD
x_sum = 0
i = 0
while i < x.size:
    x_sum += x[i]
    i += 1
x_sum %= MOD
coef = fact[N] * fact_inv[M] % MOD * fact_inv[N - M] % MOD
fR = (total - x_sum * coef) % MOD

L0 = L - 1
total2 = fact[L0 + N] * fact_inv[L0] % MOD * fact_inv[N] % MOD
x2 = Q[L0::-1] * P[:L0 + 1] % MOD
x_sum2 = 0
i = 0
while i < x2.size:
    x_sum2 += x2[i]
    i += 1
x_sum2 %= MOD
coef2 = fact[N] * fact_inv[M] % MOD * fact_inv[N - M] % MOD
fL = (total2 - x_sum2 * coef2) % MOD

answer = (fR - fL) % MOD
print(answer)