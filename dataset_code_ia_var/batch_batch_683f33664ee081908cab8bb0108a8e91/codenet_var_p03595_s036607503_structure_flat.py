import sys
import numpy as np

MOD = 998244353

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, M = map(int, readline().split())
A = np.array(list(readline().rstrip()), dtype=np.int64) - 48
B = np.array(list(readline().rstrip()), dtype=np.int64) - 48
C = np.array(list(readline().rstrip()), dtype=np.int64) - 48
D = np.array(list(readline().rstrip()), dtype=np.int64) - 48

U = 10**6
x = np.arange(U, dtype=np.int64)
x[0] = 1
L = len(x)
Lsq = int(L ** 0.5 + 1)
arr = np.resize(x, Lsq ** 2).reshape(Lsq, Lsq)
for n in range(1, Lsq):
    arr[:, n] *= arr[:, n - 1]
    arr[:, n] %= MOD
for n in range(1, Lsq):
    arr[n] *= arr[n - 1, -1]
    arr[n] %= MOD
fact = arr.ravel()[:U]

x = np.arange(U, 0, -1, dtype=np.int64)
x[0] = pow(int(fact[-1]), MOD - 2, MOD)
L = len(x)
Lsq = int(L ** 0.5 + 1)
arr = np.resize(x, Lsq ** 2).reshape(Lsq, Lsq)
for n in range(1, Lsq):
    arr[:, n] *= arr[:, n - 1]
    arr[:, n] %= MOD
for n in range(1, Lsq):
    arr[n] *= arr[n - 1, -1]
    arr[n] %= MOD
fact_inv = arr.ravel()[:U][::-1]

def flat_cumprod(arr, MOD):
    L = len(arr)
    Lsq = int(L ** 0.5 + 1)
    arr = np.resize(arr, Lsq ** 2).reshape(Lsq, Lsq)
    for n in range(1, Lsq):
        arr[:, n] *= arr[:, n - 1]
        arr[:, n] %= MOD
    for n in range(1, Lsq):
        arr[n] *= arr[n - 1, -1]
        arr[n] %= MOD
    return arr.ravel()[:L]

NA = np.count_nonzero(A)
NB = np.count_nonzero(B)
NC = np.count_nonzero(C)
ND = np.count_nonzero(D)

def do_cnt_vertical(N, M, A, B, C, D):
    AB = A + B
    L = C.sum()
    LU = A.cumsum() - A
    LD = B.cumsum() - B
    if L >= 1:
        NL = fact[LU + LD + L - 1] * fact_inv[LU + LD] % MOD * fact_inv[L - 1] % MOD
    else:
        NL = np.zeros(N, dtype=np.int64)
        idx = np.where(AB > 0)[0][0]
        NL[idx] = 1
    R = D.sum()
    RU = A[::-1].cumsum() - A[::-1]
    RD = B[::-1].cumsum() - B[::-1]
    NR = fact[RU + RD + R - 1] * fact_inv[RU + RD] % MOD * fact_inv[R - 1] % MOD
    NR = NR[::-1]
    x = np.full(N, 1, np.int64)
    x[AB == 2] = 2
    coef = flat_cumprod(x, MOD)
    x = np.full(N, 1, np.int64)
    x[AB == 2] = (MOD + 1) // 2
    coef_inv = flat_cumprod(x, MOD)
    NL *= coef_inv
    NR *= coef
    NL %= MOD
    NR %= MOD
    NL[AB == 2] *= 2
    NL[NL >= MOD] -= MOD
    NL[AB == 0] = 0
    NR[AB == 0] = 0
    NL_cum = NL.cumsum() % MOD
    return (NL_cum * NR % MOD).sum() % MOD

def do_AB_only(N, A, B):
    x = np.ones(N, dtype=np.int64)
    x[A + B == 2] = 2
    return flat_cumprod(x, MOD)[-1]

def do_ABC_only(N, M, A, B, C):
    AB = A + B
    R = C.sum()
    RU = A[::-1].cumsum() - A[::-1]
    RD = B[::-1].cumsum() - B[::-1]
    NR = fact[RU + RD + R - 1] * fact_inv[RU + RD] % MOD * fact_inv[R - 1] % MOD
    NR = NR[::-1]
    NR[AB == 0] = 0
    x = np.full(N, 1, np.int64)
    x[AB == 2] = 2
    coef = flat_cumprod(x, MOD)
    x_sum = (coef * NR % MOD).sum() % MOD
    n = A.sum() + B.sum() + C.sum() - 1
    m = C.sum() - 1
    y = fact[n] * fact_inv[m] % MOD * fact_inv[n - m] % MOD
    return (x_sum + y) % MOD

if NA != 0 and NB != 0 and NC != 0 and ND != 0:
    answer = (do_cnt_vertical(N, M, A, B, C, D) + do_cnt_vertical(M, N, C, D, A, B)) % MOD
else:
    if NA != 0:
        NA, NB = NB, NA
        A, B = B, A
        C = C[::-1].copy(); D = D[::-1].copy()
    if NC != 0:
        NC, ND = ND, NC
        C, D = D, C
        A = A[::-1].copy(); B = B[::-1].copy()
    if NB == 0:
        answer = do_AB_only(M, C, D)
    elif ND == 0:
        answer = do_AB_only(N, A, B)
    elif NA == 0 and NC == 0:
        answer = fact[NB + ND] * fact_inv[NB] % MOD * fact_inv[ND] % MOD
    elif NA == 0:
        answer = do_ABC_only(M, N, C, D, B)
    elif NC == 0:
        answer = do_ABC_only(N, M, A, B, D)

print(answer)

N = 3
M = 2
while True:
    A = np.random.randint(0, 2, N).astype(np.int64)
    B = np.random.randint(0, 2, N).astype(np.int64)
    C = np.random.randint(0, 2, M).astype(np.int64)
    D = np.random.randint(0, 2, M).astype(np.int64)
    x = 0
    y = 0
    z = 0
    if np.count_nonzero(A) != 0 and np.count_nonzero(B) != 0 and np.count_nonzero(C) != 0 and np.count_nonzero(D) != 0:
        x = (do_cnt_vertical(N, M, A, B, C, D) + do_cnt_vertical(M, N, C, D, A, B)) % MOD
        z = (do_cnt_vertical(N, M, B, A, C, D) + do_cnt_vertical(M, N, C, D, B, A)) % MOD
    else:
        NA, NB = np.count_nonzero(A), np.count_nonzero(B)
        NC, ND = np.count_nonzero(C), np.count_nonzero(D)
        AA, BB, CC, DD = A.copy(), B.copy(), C.copy(), D.copy()

        if NA != 0:
            NA, NB = NB, NA
            AA, BB = BB, AA
            CC = CC[::-1].copy(); DD = DD[::-1].copy()
        if NC != 0:
            NC, ND = ND, NC
            CC, DD = DD, CC
            AA = AA[::-1].copy(); BB = BB[::-1].copy()
        if NB == 0:
            x = do_AB_only(M, CC, DD)
        elif ND == 0:
            x = do_AB_only(N, AA, BB)
        elif NA == 0 and NC == 0:
            x = fact[NB + ND] * fact_inv[NB] % MOD * fact_inv[ND] % MOD
        elif NA == 0:
            x = do_ABC_only(M, N, CC, DD, BB)
        elif NC == 0:
            x = do_ABC_only(N, M, AA, BB, DD)

        # Second permuted pattern
        NA, NB = np.count_nonzero(B), np.count_nonzero(A)
        NC, ND = np.count_nonzero(C), np.count_nonzero(D)
        AA, BB, CC, DD = B.copy(), A.copy(), C.copy(), D.copy()

        if NA != 0:
            NA, NB = NB, NA
            AA, BB = BB, AA
            CC = CC[::-1].copy(); DD = DD[::-1].copy()
        if NC != 0:
            NC, ND = ND, NC
            CC, DD = DD, CC
            AA = AA[::-1].copy(); BB = BB[::-1].copy()
        if NB == 0:
            z = do_AB_only(M, CC, DD)
        elif ND == 0:
            z = do_AB_only(N, AA, BB)
        elif NA == 0 and NC == 0:
            z = fact[NB + ND] * fact_inv[NB] % MOD * fact_inv[ND] % MOD
        elif NA == 0:
            z = do_ABC_only(M, N, CC, DD, BB)
        elif NC == 0:
            z = do_ABC_only(N, M, AA, BB, DD)

    y = 0
    NA, NB = np.count_nonzero(C), np.count_nonzero(D)
    NC, ND = np.count_nonzero(A), np.count_nonzero(B)
    AA, BB, CC, DD = C.copy(), D.copy(), A.copy(), B.copy()
    if NA != 0 and NB != 0 and NC != 0 and ND != 0:
        y = (do_cnt_vertical(M, N, AA, BB, CC, DD) + do_cnt_vertical(N, M, CC, DD, AA, BB)) % MOD
    else:
        if NA != 0:
            NA, NB = NB, NA
            AA, BB = BB, AA
            CC = CC[::-1].copy(); DD = DD[::-1].copy()
        if NC != 0:
            NC, ND = ND, NC
            CC, DD = DD, CC
            AA = AA[::-1].copy(); BB = BB[::-1].copy()
        if NB == 0:
            y = do_AB_only(N, CC, DD)
        elif ND == 0:
            y = do_AB_only(M, AA, BB)
        elif NA == 0 and NC == 0:
            y = fact[NB + ND] * fact_inv[NB] % MOD * fact_inv[ND] % MOD
        elif NA == 0:
            y = do_ABC_only(N, M, CC, DD, BB)
        elif NC == 0:
            y = do_ABC_only(M, N, AA, BB, DD)
    if x != z:
        break

A, B, C, D

x, y, z

do_cnt_vertical(N, M, A, B, C, D), do_cnt_vertical(N, M, B, A, C, D)

do_cnt_vertical(M, N, C, D, A, B), do_cnt_vertical(M, N, C, D, B, A)