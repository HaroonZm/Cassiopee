import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

import numpy as np

N, M, L, R = map(int, input().split())

MOD = 10 ** 9 + 7

U = 6 * 10 ** 5 + 100
fact = [1] * (U + 1)
n = 1
while n <= U:
    fact[n] = fact[n - 1] * n % MOD
    n += 1

fact_inv = [1] * (U + 1)
fact_inv[U] = pow(fact[U], MOD - 2, MOD)
n = U
while n > 0:
    fact_inv[n - 1] = fact_inv[n] * n % MOD
    n -= 1

fact = np.array(fact, dtype=np.int64)
fact_inv = np.array(fact_inv, dtype=np.int64)

U2 = N - M
comb = fact[U2] * fact_inv[:U2 + 1] % MOD * fact_inv[U2::-1] % MOD
comb[1::2] *= (-1)

P = np.zeros(R + 1, dtype=np.int64)
i = M
for idx, x in enumerate(comb[M:U2 + 1], M):
    P[::idx] += comb[idx]

P_old = P.copy()
P[M:] -= P_old[:-M]
P %= MOD

Q = fact[N:N + R + 1] * fact_inv[:R + 1] % MOD * fact_inv[N] % MOD

R1 = R
t1 = fact[R1 + N] * fact_inv[R1] % MOD * fact_inv[N] % MOD
x1 = (Q[R1::-1] * P[:R1 + 1] % MOD).sum() % MOD
coef1 = fact[N] * fact_inv[M] % MOD * fact_inv[N - M] % MOD
ret1 = (t1 - x1 * coef1) % MOD

R2 = L - 1
t2 = fact[R2 + N] * fact_inv[R2] % MOD * fact_inv[N] % MOD
x2 = (Q[R2::-1] * P[:R2 + 1] % MOD).sum() % MOD
coef2 = fact[N] * fact_inv[M] % MOD * fact_inv[N - M] % MOD
ret2 = (t2 - x2 * coef2) % MOD

answer = (ret1 - ret2) % MOD
print(answer)