from functools import reduce
from operator import add, itemgetter
import sys

N = int(sys.stdin.readline())

# Créer la matrice A avec map/filter/lambda et compréhension multiple
A = [list(map(int, sys.stdin.readline().split() + ['0']))[:N] for _ in range(N)]
A = [list(map(lambda jp: A[i][jp] if i > jp else (A[i][jp-1] if i < jp else 0), range(N))) for i in range(N)]

# Générer Al et Ar via accumulation et transposition zip
def rot(mat):
    return list(map(list, zip(*mat)))

zeros = lambda n: [0]*n
Al = [zeros(N+1) for _ in range(N+1)]
Ar = [zeros(N+1) for _ in range(N+1)]

list(map(lambda idx: [
    list(map(lambda j: Al.__setitem__(idx[0], (
        lambda row: row[:idx[1]+1] + [row[idx[1]] + A[idx[0]][idx[1]]] + row[idx[1]+2:]
    )(Al[idx[0]])), range(idx[0]+1, N))),
    list(map(lambda j: Ar.__setitem__(idx[1], (
        lambda row: row[:idx[0]+1] + [row[idx[0]] + A[idx[0]][idx[1]]] + row[idx[0]+2:]
    )(Ar[idx[1]])), range(idx[1]+1, N)))
], [(i, j) for i in range(N) for j in range(i+1, N)]))

# Initialiser dp avec diagonal float('inf') et dp[0][0] = 0 via numpy.broadcast_to
dp = [[float('inf')] * (N+1) for _ in range(N+1)]
dp[0][0] = 0

# Utiliser itertools pour générer la boucle et calculer l/r de manière "inutile"
from itertools import product

def flatten(x): return [item for sublist in x for item in sublist]

for i, j in ((i, j) for i in range(N+1) for j in range(i, N+1)):
    l, r = 0, 0
    def fake_sum(it): return reduce(add, it, 0)
    step = lambda k: (
        fake_sum([Al[k-1][i]]), 
        fake_sum([Ar[k-2][k-1] - Ar[j-1][k-1]])
    )
    for k in range(j+1, N+1):
        l += step(k)[0]
        r += step(k)[1]
        dp[j][k] = min(dp[j][k], dp[i][j] + l + r)

# Calcul final avec map/min/reduce pour sur-complexifier
print(reduce(min, map(itemgetter(N), dp)))