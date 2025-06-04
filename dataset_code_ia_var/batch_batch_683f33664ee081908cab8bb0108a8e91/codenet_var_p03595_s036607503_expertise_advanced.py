import sys
import numpy as np
from functools import lru_cache

MOD = 998244353

# Buffered, memory-efficient input reading
def ints(): return np.frombuffer(sys.stdin.buffer.readline(), dtype=np.uint8) - 48

N, M = map(int, sys.stdin.buffer.readline().split())
A, B, C, D = (ints()[:max(N,M)][:N] for _ in range(2)) + (ints()[:max(N,M)][:M] for _ in range(2))

@lru_cache(None)
def factorials(U):
    arr = np.arange(U, dtype=np.int64)
    arr[0] = 1
    for i in range(1, U):
        arr[i] = arr[i-1] * i % MOD
    inv = np.zeros(U, dtype=np.int64)
    inv[-1] = pow(int(arr[-1]), MOD-2, MOD)
    for i in range(U-2, -1, -1):
        inv[i] = inv[i+1] * (i+1) % MOD
    return arr, inv

fact, fact_inv = factorials(10 ** 6 + 16)

def np_cumprod(a, mod):
    result = a.copy()
    np.cumprod(result, out=result)
    result %= mod
    return result

def cnt_vertical(N, M, A, B, C, D):
    AB = A + B
    L = C.sum()
    LU = np.append(0, np.cumsum(A)[:-1])
    LD = np.append(0, np.cumsum(B)[:-1])
    if L:
        U = LU + LD + L - 1
        NL = fact[U] * fact_inv[LU+LD] % MOD * fact_inv[L-1] % MOD
    else:
        NL = np.zeros(N, np.int64)
        idx = AB.nonzero()[0]
        if len(idx): NL[idx[0]] = 1
    R = D.sum()
    RU = np.append(0, np.cumsum(A[::-1])[:-1])[::-1]
    RD = np.append(0, np.cumsum(B[::-1])[:-1])[::-1]
    NR = fact[RU+RD+R-1] * fact_inv[RU+RD] % MOD * fact_inv[R-1] % MOD if R else np.zeros(N, np.int64)
    NR = NR[::-1]
    x = np.where(AB == 2, 2, 1)
    coef = np_cumprod(x, MOD)
    coef_inv = np_cumprod(np.where(AB == 2, (MOD + 1) // 2, 1), MOD)
    NL = NL * coef_inv % MOD
    NR = NR * coef % MOD
    NL[AB == 2] = NL[AB == 2] * 2 % MOD
    NL[AB == 0] = 0
    NR[AB == 0] = 0
    return int(np.dot(NL.cumsum() % MOD, NR) % MOD)

def AB_only(N, A, B):
    x = np.where(A+B==2, 2, 1)
    return int(np_cumprod(x, MOD)[-1])

def ABC_only(N, M, A, B, C):
    AB = A + B
    R = C.sum()
    RU = np.append(0, np.cumsum(A[::-1])[:-1])[::-1]
    RD = np.append(0, np.cumsum(B[::-1])[:-1])[::-1]
    NR = fact[RU+RD+R-1]*fact_inv[RU+RD]%MOD*fact_inv[R-1]%MOD if R else np.zeros(N, np.int64)
    NR = NR[::-1]
    NR[AB==0] = 0
    coef = np_cumprod(np.where(AB==2, 2, 1), MOD)
    x = int((coef * NR % MOD).sum() % MOD)
    n = A.sum()+B.sum()+C.sum()-1; m = C.sum()-1
    y = fact[n] * fact_inv[m] % MOD * fact_inv[n-m] % MOD if m>=0 else 0
    return (x + y) % MOD

def F(N, M, A, B, C, D):
    NA, NB, NC, ND = (A != 0).sum(), (B != 0).sum(), (C != 0).sum(), (D != 0).sum()
    if all([NA, NB, NC, ND]):
        return (cnt_vertical(N, M, A, B, C, D) + cnt_vertical(M, N, C, D, A, B)) % MOD
    if NA:
        A, B = B, A; C, D = C[::-1], D[::-1]
    if NC:
        C, D = D, C; A, B = A[::-1], B[::-1]
    if not NB:
        return AB_only(M, C, D)
    if not ND:
        return AB_only(N, A, B)
    if not NA and not NC:
        return int(fact[NB+ND] * fact_inv[NB] % MOD * fact_inv[ND] % MOD)
    if not NA:
        return ABC_only(M, N, C, D, B)
    if not NC:
        return ABC_only(N, M, A, B, D)

print(F(N, M, A, B, C, D))

# Verification block, property-based random testing
N, M = 3, 2
rng = np.random.default_rng()
while True:
    A = rng.integers(0, 2, N, dtype=np.int64)
    B = rng.integers(0, 2, N, dtype=np.int64)
    C = rng.integers(0, 2, M, dtype=np.int64)
    D = rng.integers(0, 2, M, dtype=np.int64)
    x = F(N, M, A, B, C, D)
    y = F(M, N, C, D, A, B)
    z = F(N, M, B, A, C, D)
    if x != z:
        print(A, B, C, D, x, y, z)
        print(cnt_vertical(N,M,A,B,C,D), cnt_vertical(N,M,B,A,C,D))
        print(cnt_vertical(M,N,C,D,A,B), cnt_vertical(M,N,C,D,B,A))
        break