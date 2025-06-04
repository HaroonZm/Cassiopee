import sys
import numpy as np

input = sys.stdin.readline

N, M, L, R = map(int, input().split())
MOD = 10 ** 9 + 7

X = 1000
fact = np.arange(X * X, dtype=np.int64).reshape(X, X)
fact[0, 0] = 1
for n in range(1, X):
    fact[:, n] *= fact[:, n - 1]
    fact[:, n] %= MOD
for n in range(1, X):
    fact[n] *= fact[n - 1, -1]
    fact[n] %= MOD
fact = fact.ravel()

fact_inv = np.arange(1, X * X + 1, dtype=np.int64)[::-1].reshape(X, X)
fact_inv[0, 0] = pow(int(fact[-1]), MOD - 2, MOD)
for n in range(1, X):
    fact_inv[:, n] *= fact_inv[:, n - 1]
    fact_inv[:, n] %= MOD
for n in range(1, X):
    fact_inv[n] *= fact_inv[n - 1, -1]
    fact_inv[n] %= MOD
fact_inv = fact_inv.ravel()[::-1]

U = N - M
comb = fact[U] * fact_inv[:U + 1] % MOD * fact_inv[U::-1] % MOD
comb[1::2] *= -1

P = np.zeros(R + 1, dtype=np.int64)
for i, x in enumerate(comb, M):
    P[::i] += x
P[M:] -= P.copy()[:-M]
P %= MOD

Q = fact[N:N + R + 1] * fact_inv[:R + 1] % MOD * fact_inv[N] % MOD

R1 = R
total1 = fact[R1 + N] * fact_inv[R1] % MOD * fact_inv[N] % MOD
x1 = (Q[R1::-1] * P[:R1 + 1] % MOD).sum() % MOD
coef1 = fact[N] * fact_inv[M] % MOD * fact_inv[N - M] % MOD
fR = (total1 - x1 * coef1) % MOD

R2 = L - 1
total2 = fact[R2 + N] * fact_inv[R2] % MOD * fact_inv[N] % MOD
x2 = (Q[R2::-1] * P[:R2 + 1] % MOD).sum() % MOD
coef2 = fact[N] * fact_inv[M] % MOD * fact_inv[N - M] % MOD
fL = (total2 - x2 * coef2) % MOD

answer = (fR - fL) % MOD
print(answer)