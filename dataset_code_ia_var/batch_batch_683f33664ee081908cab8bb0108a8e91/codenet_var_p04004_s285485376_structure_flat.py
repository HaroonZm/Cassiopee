import sys
import numpy as np

read = sys.stdin.buffer.read

N, M, K = map(int, read().split())
MOD = 10**9 + 7
U = 10 ** 6

a2 = 2
a3 = 3
a2_inv = pow(a2, MOD - 2, MOD)
a3_inv = pow(a3, MOD - 2, MOD)

B = U.bit_length()
power2 = np.empty(1 + (1 << B), np.int64)
power2[0] = 1
power2[1] = a2
for n in range(B):
    power2[1 << n: 1 << (n + 1)] = power2[: 1 << n] * (a2 * power2[(1 << n) - 1] % MOD) % MOD
power2 = power2[:U]

power2_inv = np.empty(1 + (1 << B), np.int64)
power2_inv[0] = 1
power2_inv[1] = a2_inv
for n in range(B):
    power2_inv[1 << n:1 << (n + 1)] = power2_inv[:1 << n] * (a2_inv * power2_inv[(1 << n) - 1] % MOD) % MOD
power2_inv = power2_inv[:U]

power3 = np.empty(1 + (1 << B), np.int64)
power3[0] = 1
power3[1] = a3
for n in range(B):
    power3[1 << n:1 << (n + 1)] = power3[:1 << n] * (a3 * power3[(1 << n) - 1] % MOD) % MOD
power3 = power3[:U]

power3_inv = np.empty(1 + (1 << B), np.int64)
power3_inv[0] = 1
power3_inv[1] = a3_inv
for n in range(B):
    power3_inv[1 << n:1 << (n + 1)] = power3_inv[:1 << n] * (a3_inv * power3_inv[(1 << n) - 1] % MOD) % MOD
power3_inv = power3_inv[:U]

_x = np.arange(U, dtype=np.int64)
_x[0] = 1
# cumprod:
L = len(_x)
Lsq = int(L ** 0.5 + 1)
t = np.resize(_x, Lsq ** 2).reshape(Lsq, Lsq)
for n in range(1, Lsq):
    t[:, n] *= t[:, n - 1]; t[:, n] %= MOD
for n in range(1, Lsq):
    t[n] *= t[n - 1, -1]; t[n] %= MOD
fact = t.ravel()[:L]

_x = np.arange(U, 0, -1, dtype=np.int64)
_x[0] = pow(int(fact[-1]), MOD - 2, MOD)
L = len(_x)
Lsq = int(L ** 0.5 + 1)
t = np.resize(_x, Lsq ** 2).reshape(Lsq, Lsq)
for n in range(1, Lsq):
    t[:, n] *= t[:, n - 1]; t[:, n] %= MOD
for n in range(1, Lsq):
    t[n] *= t[n - 1, -1]; t[n] %= MOD
fact_inv = t.ravel()[:L][::-1]

x = np.zeros(N + M, np.int64)
x[1:] = (-1) * power2[:N + M - 1] * power3_inv[K + 1:N + M + K] % MOD
x[1:] *= fact[K + 1:N + M + K] * fact_inv[K] % MOD * fact_inv[1:N + M] % MOD
x %= MOD
x[0] = 3 * (1 - power3_inv[K + 1]) % MOD * power2_inv[1] % MOD
np.cumsum(x, out=x)
x %= MOD
x *= power3[:N + M] * power2_inv[:N + M] % MOD
x %= MOD

coef = fact[N - 1:N + M] * fact_inv[:M + 1] % MOD * fact_inv[N - 1] % MOD
coef *= power3[K:K + M + 1][::-1]
coef %= MOD
answer = (coef * x[N - 1:N + M] % MOD).sum() % MOD
print(answer)