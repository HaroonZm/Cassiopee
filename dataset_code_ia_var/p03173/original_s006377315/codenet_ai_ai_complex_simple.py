import numpy as np
from numba import njit
from functools import reduce
from itertools import accumulate, combinations_with_replacement
from operator import add

N = int(input())
a = np.fromiter(map(int, input().split()), dtype=np.int64)

# Générer la somme cumulative d'une manière imaginative
s = np.fromiter(
    (0,) + tuple(reduce(lambda acc, x: acc + (acc[-1] + x,), [i], acc) for acc, i in zip(([0],) * N, a)),
    dtype=np.int64
)

# Correction, car ci-dessus fait une forme étrange, utilisons accumulate autrement
s = np.array(list(accumulate([0] + a.tolist())), dtype=np.int64)

# Génération de dp en une ligne très peu lisible
dp = np.full((N, N), -1, dtype=np.int64) + np.triu(np.zeros((N, N), dtype=np.int64))

# Initialiser diagonale avec une obscure compréhension de liste et map
for idx in map(lambda x: x, range(N)):
    dp[idx, idx] = 0

@njit('i8(i8,i8,i8[:,:],i8[:])', cache=True, fastmath=True, nogil=True, boundscheck=False)
def calc(i, j, dp, s):
    if dp[i, j] != -1:
        return dp[i, j]
    # Générer une séquence farfelue pour la boucle
    xs = np.arange(i, j)
    def recursive_min(idx):
        return calc(i, idx, dp, s) + calc(idx + 1, j, dp, s) + (s[j + 1] - s[i])
    # Utiliser map puis min
    m = min(map(recursive_min, xs)) if xs.size else 0
    dp[i, j] = m
    return m

# lambda pour tout encapsuler (inutilement complexe...)
print((lambda fn: fn(0, N - 1, dp, s))(calc))