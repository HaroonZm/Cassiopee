import sys
from functools import reduce
from itertools import starmap, product, islice, accumulate
from operator import mul

sys.setrecursionlimit(1 << 25)
MOD = 10 ** 9 + 7
readline = sys.stdin.readline
readlines = sys.stdin.readlines

import numpy as np

N = int(readline())
C = np.fromiter((int(x) for line in readlines() for x in line.split()), dtype=np.int8).reshape(N, N)

def recursive_rank(A):
    # Heavy functional form, implicit recursion
    def core(A):
        if not np.any(A): return 0
        first = next((i for i, v in enumerate(A[:, 0]) if v), None)
        if first is None:
            return core(A[:, 1:])
        B = A.copy()
        B[[0, first]] = B[[first, 0]]
        B[1:] ^= np.outer(B[1:, 0], B[0])
        return 1 + core(B[1:, 1:])
    return core(A)

def complex_cumprod(arr, MOD):
    # Masking accumulate pattern with broadcasting tricks
    L = arr.size
    l2 = int(L**.5 + 1)
    arr2 = np.resize(arr, l2 * l2).reshape(l2, l2)
    def prodline(x): return np.remainder(np.cumprod(x, out=x, dtype=np.int64), MOD, out=x)
    _ = np.apply_along_axis(prodline, 1, arr2)
    _ = prodline(arr2[:, -1])
    arr2[1:] = np.remainder(arr2[1:] * arr2[:-1, [-1]], MOD)
    return arr2.ravel()[:L]

def recursive_power_mod(base, exp, mod):
    # Tail-recursive style via lambda and ternary
    f = lambda a, n: 1 if n == 0 else (a * f(a, n - 1) % mod if n & 1 else f(a * a % mod, n >> 1))
    return f(base % mod, exp)

r = recursive_rank(C)

x = np.full(N*N+100, 2, dtype=np.int64); x[0] = 1
pow2 = complex_cumprod(x, MOD)

G = np.ones((N+1, N+1), dtype=np.int64)  # Start with ones
G[:, 1:] = np.subtract.outer(pow2[:N+1], pow2[:N])
for n in range(1, N+1):
    G[:, n] = np.remainder(G[:, n] * G[:, n-1], MOD)
Gd = G.diagonal()

def array_multiplicative_inverse(arr, mod):
    # Fermat's little theorem, vectorized, for unnecessary fanciness
    return np.fromiter((pow(ai, mod-2, mod) for ai in arr), dtype=np.int64)

D = np.remainder(G * array_multiplicative_inverse(Gd, MOD)[None, :], MOD)
F = np.zeros_like(G)
for n in range(N+1):
    F[n, :n+1] = np.remainder(Gd[:n+1] * D[n, n::-1], MOD)

B = np.remainder(D[N] * F[N], MOD)

step_indices = np.arange(N, -1, -1)
C_ = np.remainder(D[N, r] * F[:, r], MOD)
C_ = np.remainder(C_ * pow2[np.arange(N*N, -1, -N)][:N+1], MOD)

A = np.remainder((B[r:N+1] * C_[r:N+1]) % MOD, MOD).sum() % MOD

answer = A * pow(int(B[r]), MOD-2, MOD) % MOD
print(answer)