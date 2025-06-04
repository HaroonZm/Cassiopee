import sys
sys.setrecursionlimit(10**7)

n, m, k = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

# On doit trouver le minimum de sommets (stations) pour couvrir toutes les arêtes
# C'est un problème de vertex cover minimum dans un graphe général, qui est NP-difficile
# Ici on limite la recherche à K stations
# On peut essayer une approche naïve car K est petit (<=32)
# Mais n est grand, donc pas de recherche exhaustive complète possible
# Approche simple: trouver le nombre minimal de sommets nécessaires pour couvrir toutes les arêtes via un algorithme glouton approximatif

edges = set()
for u in range(n):
    for v in graph[u]:
        if u < v:
            edges.add((u, v))

edges = list(edges)
covered = [False]*len(edges)
selected = set()

while True:
    if all(covered):
        break
    # compte combien d'arêtes restent à couvrir pour chaque sommet
    counts = [0]*n
    for i, (u, v) in enumerate(edges):
        if not covered[i]:
            counts[u] += 1
            counts[v] += 1
    # sélectionne le sommet couvrant le plus d'arêtes non couvertes
    max_cover = max(counts)
    if max_cover == 0:
        break
    v = counts.index(max_cover)
    selected.add(v)
    # marque les arêtes couvertes par ce sommet
    for i, (u, w) in enumerate(edges):
        if not covered[i] and (u == v or w == v):
            covered[i] = True

if len(selected) <= k:
    print(len(selected))
else:
    print("Impossible")