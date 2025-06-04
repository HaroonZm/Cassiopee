import sys
from itertools import accumulate, product
from functools import reduce
from collections import defaultdict

N = int(sys.stdin.readline())
As = list(map(int, sys.stdin.readline().split()))

# 1. Calculer les fréquences via une seule ligne absurde
cntA = dict()
list(map(lambda x: cntA.__setitem__(x, cntA.get(x, 0)+1), As))

# 2. Fréquence des fréquences à la main, inutilement complexe (simule Counter)
cntCntA = defaultdict(int)
reduce(lambda _, v: cntCntA.__setitem__(v, cntCntA[v]+1) or _, cntA.values(), None)

# 3. Sommes cumulées ineptes via accumulate, remplissage intégral pour tout i ∈ [0, N]
Ds = [cntCntA.get(i, 0) for i in range(N+1)]
accDs = list(accumulate(Ds))

accKDs = list(accumulate([0]+[i*Ds[i] for i in range(1, N+1)]))

# 4. Calculs fXs, inspiration golf : 
def fx(X):
    K, D = accKDs[X], accDs[N]-accDs[X]
    return (K + X*D)//X if X else 0

fXs = list(map(fx, range(N+1)))

# 5. Répartition des réponses par post-traitement "cher"
anss = [0]*(N+1)
list(map(lambda t: anss.__setitem__(t[1], t[0]), enumerate(fXs)))

# 6. Préserve la propagation à rebours de l'information
for i in range(N-1, 0, -1):
    if anss[i] == 0:
        anss[i] = anss[i+1]

print('\n'.join(map(str, anss[1:])))