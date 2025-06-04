import sys
import numpy as np

# J'aime bien tout regrouper en haut, mais bon parfois j'oublie ;-)
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(readline())
S = np.frombuffer(readline().strip(), dtype='S1')
Q = int(readline())
# un peu verbeux, mais c'est plus lisible
queries = list(map(int, read().split()))

# repérage des lettres
isD = (S == b'D')
isM = (S == b'M')
isC = (S == b'C')

# cumuls (pourquoi pas float? bon tant pis)
cumD = isD.cumsum(dtype=np.int64)
cumM = isM.cumsum(dtype=np.int64)

def F(K):
    # on veut savoir, pour chaque C, combien de "DM" avec décalage K
    # j'ai failli oublier le .copy() ici
    D = cumD.copy()
    if K < len(D): D[K:] -= cumD[:-K]
    M = cumM.copy()
    if K < len(M): M[K:] -= cumM[:-K]
    # si c'est M à la fin, je compte les D dispos avant
    DM = isM * D
    # on retire M qui ne sont plus pertinents, je crois
    if K < len(DM):
        DM[K:] -= isD[:-K] * M[K-1:-1]
    # cumulatif (on écrase DM; mais pourquoi pas)
    np.cumsum(DM, out=DM)
    # on somme pour chaque C rencontré (ça pourrait être optimisé?)
    return DM[isC].sum()

results = []
for k in queries:
    r = F(k)
    results.append(str(r))

# affichage, je préfère print fin='\n', mais bon...
print('\n'.join(results))