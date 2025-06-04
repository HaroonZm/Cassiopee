import sys
from functools import lru_cache
import numpy as np

MOD = 998244353
input = sys.stdin.readline

N, M = map(int, input().split())

def cumprod_mod(arr, mod=MOD):
    # Utilisation de la factorisation de plage (block-wise prefix product)
    L = len(arr)
    Lsq = int(L**0.5) + 1
    blk = np.resize(arr, Lsq * Lsq).reshape(Lsq, Lsq)
    np.multiply.accumulate(blk, axis=1, out=blk)
    np.multiply.accumulate(blk[:, -1], out=blk[:, -1])
    blk[1:] = (blk[1:] * blk[:-1, -1, None]) % mod
    out = blk.ravel()[:L]
    out %= mod
    return out

Nsq = int(N ** 0.5) + 1
a = np.zeros((Nsq, Nsq + 1), dtype=np.int64)
b = np.zeros_like(a)
a[0, 0] = 1

arrange = np.arange(Nsq + 1)
# On vectorise la récurrence modulaire
for n in arrange[1:]:
    a[0, n] = (-b[0, n - 1]) % MOD
    b[0, n] = (a[0, n - 1] + 3 * b[0, n - 1]) % MOD

u, v = a[0, Nsq], b[0, Nsq]
for n in range(1, Nsq):
    a[n] = (a[n - 1] * u - b[n - 1] * v) % MOD
    b[n] = (a[n - 1] * v + b[n - 1] * u + 3 * b[n - 1] * v) % MOD

a = a[:, :-1].ravel()
b = b[:, :-1].ravel()
G = (-a - 2 * b) % MOD
G = G[:N + 1]

A = (-G[N - 1] + -G[N] + 3 * G[N - 1]) % MOD
B = (- -G[N] + 3 * -G[N - 1]) % MOD
A = (A + B) % MOD
B = (-B) % MOD

@lru_cache(maxsize=None)
def fibonacci(n):
    # Renvoie (F(n), F(n+1)), adapté à la forme requise
    if n == 0:
        return (1, 0)
    if n == 1:
        return (0, 1)
    if n % 2 == 0:
        a, b = fibonacci(n // 2)
        asq, bsq = a * a % MOD, b * b % MOD
        ab = a * b % MOD
        f0 = (asq + bsq) % MOD
        f1 = (2 * ab + bsq) % MOD
        return (f0, f1)
    else:
        a, b = fibonacci(n // 2)
        asq, bsq = a * a % MOD, b * b % MOD
        ab = a * b % MOD
        f0 = (asq + bsq) % MOD
        f1 = (2 * ab + bsq) % MOD
        return (f1, (f0 + f1) % MOD)

x = (np.arange(N, dtype=np.int64) + M) % MOD
x[0] = 1
num = cumprod_mod(x)

x = np.arange(N, dtype=np.int64)
x[0] = 1
fact = cumprod_mod(x)

x = np.arange(N, 0, -1, dtype=np.int64)
x[0] = pow(int(fact[-1]), MOD - 2, MOD)
fact_inv = cumprod_mod(x)[::-1]

if N == 1:
    xres = 0
else:
    xres = np.dot((num * fact_inv)[:N - 1], G[N - 2::-1]) % MOD
y, z = fibonacci(M + 1)
answer = (z * A + y * B + xres) % MOD
print(answer)