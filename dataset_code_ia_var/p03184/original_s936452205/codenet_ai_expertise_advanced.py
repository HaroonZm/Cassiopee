import sys
import numpy as np
from functools import lru_cache

input = sys.stdin.readline
sys.setrecursionlimit(1 << 25)

MOD = 10**9 + 7

# Lecture des entrées avec posttraitement numpy vectorisé
H, W, N = map(int, input().split())
coords = np.fromstring(sys.stdin.read(), sep=' ', dtype=np.int64)
coords = np.concatenate((coords, [H, W]))  # but final à la fin
R, C = coords.reshape(-1, 2).T

# Tri des coordonnées par (R, C), laissant la destination à la fin
ind = np.lexsort((C, R))
R, C = R[ind], C[ind]

def fast_cumprod(a):
    """Cumprod numpy rapide en bloc, modulo MOD"""
    n = len(a)
    blksz = int(n**0.5) + 1
    m = blksz * blksz
    b = np.ones(m, dtype=np.int64)
    b[:n] = a
    b = b.reshape(blksz, blksz)
    b = np.cumprod(np.cumprod(b, axis=1), axis=0) % MOD
    return b.ravel()[:n]

U = max(H, W, max(R)+max(C)) + N + 10
x = np.arange(U, dtype=np.int64)
x[0] = 1
fact = fast_cumprod(x)
x_inv = np.arange(U, 0, -1, dtype=np.int64)
x_inv[0] = pow(int(fact[-1]), MOD-2, MOD)
fact_inv = fast_cumprod(x_inv)[::-1]

dp = fact[R + C - 2]
dp = (dp * fact_inv[R - 1]) % MOD
dp = (dp * fact_inv[C - 1]) % MOD

for i in range(N + 1):
    r, c = R[i], C[i]
    mask = (R <= r) & (C <= c) & ((R + C) < (r + c))
    if not np.any(mask):
        continue
    dx, dy = r - R[mask], c - C[mask]
    comb = fact[dx + dy]
    comb = (comb * fact_inv[dx]) % MOD
    comb = (comb * fact_inv[dy]) % MOD
    dp[i] = (dp[i] - np.dot(dp[mask], comb)) % MOD

print(dp[-1])