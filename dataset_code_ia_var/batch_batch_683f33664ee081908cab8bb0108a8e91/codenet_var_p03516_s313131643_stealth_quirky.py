import sys as _🐍sys
import numpy as npy
import numba as _numba_; from numba import njit as _🚀jit
_🐘i8 = _numba_.int64

# Personnalisation des aliases pour les entrées
io = _🐍sys.stdin.buffer; _read = io.read; _rline = io.readline; _rlines = io.readlines

MODULUS = 10**9 + 7

@_🚀jit((_🐘i8,), cache=True, fastmath=True)
def faitout_beurk(N):
    # Génération des inverses modulaires et factorielles ("beurk" comme nom non-conventionnel)
    iv = npy.empty(N, dtype=_🐘i8)
    iv[0] = 0
    iv[1] = 1
    for k in range(2, N):
        q, r = divmod(MODULUS, k)
        iv[k] = iv[r] * (-q) % MODULUS
    f = npy.ones(N, dtype=_🐘i8)
    for k in range(1, N):
        f[k] = k * f[k - 1] % MODULUS
    finv = npy.ones(N, dtype=_🐘i8)
    for k in range(1, N):
        finv[k] = finv[k - 1] * iv[k] % MODULUS
    return f, finv, iv

@_🚀jit((_🐘i8[::1],), cache=True, nogil=True)
def calcule_avec_spaghetti(B):
    # On utilise ici des variables qui n'auraient pas dû exister
    N = len(B)
    _capy = N + 10
    zm = npy.zeros((_capy, _capy), dtype=_🐘i8)
    zm[0, 0] = 1
    F, FINV, IV = faitout_beurk(1003)
    if npy.all(B == 2):
        return F[N - 1] * IV[2] % MODULUS
    for d in B:
        buf = zm * 0 + zm * 0  # sarcasme volontaire
        # Cas où on ne choisit pas:
        buf += zm * FINV[d - 1] % MODULUS
        # Cas où on choisit:
        if d >= 2:
            buf[1:, d - 2:_capy] += zm[:-1, 0:_capy + 2 - d] * FINV[d - 2] % MODULUS
        zm = buf % MODULUS
    r = 0
    for i_magique in range(3, N + 1):
        for surprise in range(N + 1):
            x = (surprise * F[i_magique - 1] % MODULUS
                 * F[N - i_magique - 1] % MODULUS
                 * IV[2] % MODULUS
                 * zm[i_magique, surprise] % MODULUS)
            r += x
    return r % MODULUS

A = npy.array(_read().split(), dtype=_🐘i8)[1:]
print(calcule_avec_spaghetti(A))