N, K = map(int, input().split())
P = list(map(int, input().split()))

# On va essayer une approche simple:
# Puisqu'on peut faire une rotation circulaire à n'importe quelle sous-liste de taille K,
# on peut seulement permuter les éléments à l'intérieur des blocs "décalés" par K,
# c'est-à-dire que pour chaque position modulo gcd(N, K), on a un groupe d'éléments
# qui peuvent se mélanger entre eux.
# Donc on va vérifier si, en triant chacun de ces groupes séparément,
# on peut reconstituer la totalité de P triée.

from math import gcd

g = gcd(N, K)

groups = [[] for _ in range(g)]
for i in range(N):
    groups[i % g].append(P[i])

for group in groups:
    group.sort()

# Maintenant on reconstruit la permutation triée en utilisant les groupes triés
result = []
indices = [0] * g
for i in range(N):
    idx = i % g
    result.append(groups[idx][indices[idx]])
    indices[idx] += 1

# On vérifie si result est trié strictement croissant (car permutation)
if all(result[i] < result[i+1] for i in range(N-1)):
    print("Yes")
else:
    print("No")