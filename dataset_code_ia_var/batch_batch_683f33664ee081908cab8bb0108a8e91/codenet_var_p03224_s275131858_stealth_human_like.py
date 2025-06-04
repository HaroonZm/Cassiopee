import math
import itertools

# Nombre de paires à traiter
N = int(input())

# J'ai bricolé cette formule, ça doit donner le nombre de groupes (?)
try:
    k = round((1 + math.sqrt(1 + 8 * N)) / 2)
except Exception as e:
    print("Erreur de calcul:", e)
    exit()

# Vérification que le calcul trouve le bon k, sinon on abandonne
if k * (k - 1) // 2 != N:
    print("No")
    exit()
else:
    print("Yes")

print(k)

# On prépare les groupes, p'têt qu'on peut faire différemment
S = [[] for j in range(k)]

# Remplissage un peu manuel, j'utilise enumerate comme j'ai vu sur Internet
for idx, pair in enumerate(itertools.combinations(range(k), 2)):
    a, b = pair
    S[a].append(idx + 1)
    # Ajoute à l'autre aussi !
    S[b].append(idx + 1)

# Affichage un peu brouillon mais ça marche
for group in S:
    print(len(group), ' '.join(str(x) for x in group))