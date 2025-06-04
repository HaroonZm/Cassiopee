import sys
sys.setrecursionlimit(10**7)

N, M, P = map(int, sys.stdin.readline().split())
edges = [tuple(map(lambda x: int(x)-1, sys.stdin.readline().split())) for _ in range(M)]
p = P / 100
q = 1 - p

adj = [[] for _ in range(N)]
for u,v in edges:
    adj[u].append(v)
    adj[v].append(u)

# On veut la probabilité que le graphe reste connexe après suppression aléatoire d'arêtes indépendamment avec probabilité p.

# Complexité: N<=14, M<=100. Pas possible de faire une DP sur tous les sous-ensembles d'arêtes (2^M).
# Une solution efficace est une méthode par Inclusion-Exclusion sur les composantes connexes, car N est petit.
# Le graphe est connexe au départ (non explicitement dit, mais sinon prob de connectivité est 0).
# On calcule la probabilité que le graphe ne soit pas connexe => il existe un cut-set (partition du graphe en deux non-vide parties sans edge traversant)
# Utilisation Inclusion-Exclusion sur tous les subsets des sommets (sauf trivial).

# Pour chaque S subset de V, 0 < |S| < N, on calcule le nombre d'arêtes crossing S et V\S.
# La probabilité que toutes ces edges soient absentes est q^(nombre_edges_crossing).
# L'ensemble des disconnects est l'union de ces événements sur tous S.
# On applique inclusion-exclusion:
# prob = 1 - sum_{non empty S proper subset V} (-1)^{|S|+1} * q^{cut_edges(S)}

# Mais cette formule n'est la forme directe que pour le complément du graphe connexe ?
# En effet, ici la probabilité que le sous-ensemble S soit une composante séparée est q^(cut_edges(S)), on doit ajuster l'exclusion-inclusion
# En fait, la formule classique est:
# prob(graph disconnected) = sum_{S subset of V, S != empty, S != V} q^{cut_edges(S)} * mu(S)
# mu est la fonction de Möbius sur la partition, ou on utilise la forme:
# prob_connexe = sum_{S subset V} (-1)^{|S|} q^{cut_edges(S)}  (où cut_edges(S) nombre d'arêtes entre S et V\S)

# On code cette formule: prob_connexe = sum_{S subset V} (-1)^{|S|} * q^{cut_edges(S)}

# Le problème: pour S = empty set, cut_edges=0, contribution = 1
# pour S = V, cut_edges=0, contribution = (-1)^N *1
# Donc on a:
# prob(graph connecté) = sum_{S subseteq V} (-1)^|S| * q^{edges_between(S,V\S)}

from math import comb

cut_edges = [0]*(1<<N)
# Pré-calculer pour chaque subset S le nombre d'arêtes entre S et V\S
for u,v in edges:
    for mask in range(1<<N):
        in_u = (mask >> u) & 1
        in_v = (mask >> v) & 1
        # edge is crossing if one in S and other not
        if in_u != in_v:
            cut_edges[mask] += 1

res = 0.0
for mask in range(1<<N):
    sign = -1 if bin(mask).count('1') & 1 else 1
    res += sign * (q**cut_edges[mask])

print(f"{res:.12f}")