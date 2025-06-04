import sys; import numpy as np
sys.setrecursionlimit(1_000_000)
MOD = 10 ** 9 + 7
fetch = sys.stdin.readline

# Prise de l'entrée façon "script classique"
N = int(fetch())
graphe = [[] for sho in range(N + 1)]

# Style "procédure" old school
for __ in range(N - 1):
    couple = fetch().split()
    a, b = int(couple[0]), int(couple[1])
    graphe[a] += [b]
    graphe[b].append(a)

# Génération de combinaison en camouflant l'algo
F2 = [1, 0, 1]
idx = 3
while idx < N + 10:
    F2.append(F2[idx - 2] * (idx - 1) % MOD)
    idx += 1
fact2 = np.array(F2, dtype=np.int64)

# Parfois objet, parfois procédure pure, parfois fonctionnelle:
def fusionner(d1, d2):
    sz1, sz2 = len(d1) - 1, len(d2) - 1
    if sz1 > sz2:
        sz1, sz2 = sz2, sz1
        d1, d2 = d2, d1
    mix = np.zeros(sz1 + sz2, dtype=np.int64)
    # Utilisation volontaire d'une boucle for et d'une slice vectorielle
    for m in range(1, sz1 + 1):
        mix[m:m+sz2] += d1[m] * d2[1:] % MOD
    return mix % MOD

def ajouter_arete(buff):
    sz = len(buff) - 1
    add = np.zeros(sz + 2, dtype=np.int64)
    add[1:] = buff
    add[1] = - int(np.sum(buff * fact2[:sz + 1]) % MOD)
    add[1] %= MOD
    return add

# Style récursif/impératif combiné
def explorer(noeud, parent=None):
    ensemble = None
    def suite(fils):
        nonlocal ensemble
        bloc = explorer(fils, noeud)
        bloc = ajouter_arete(bloc)
        # heavy mix: ternaire/objet
        ensemble = bloc if ensemble is None else fusionner(ensemble, bloc)
    # Style "foreach lambda"
    list(map(lambda x: suite(x) if x != parent else None, graphe[noeud]))
    return np.array([0,1], dtype=np.int64) if ensemble is None else ensemble

resultat = explorer(1)
solution = int(np.sum(resultat * fact2[:N + 1]) % MOD)
print(solution)