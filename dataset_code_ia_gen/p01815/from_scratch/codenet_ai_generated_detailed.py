import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# Problème d'exploration de graphe non orienté où l'on ne peut pas retraverser immédiatement la même arête.
# On doit maximiser la somme des poids des sommets visités au moins une fois.
# On commence au sommet 1.

# Approche :
# - On considère un DP par sommet avec mémorisation.
# - Pour chaque sommet, on cherche la meilleure somme obtenable en partant de ce sommet,
#   sachant que l'on vient d'un certain sommet parent (pour éviter de reprendre la même arête).
# - On marque les sommets visités lors de la première visite pour ne pas recompter leur poids.
# - Comme on ne peut pas repasser par la même arête immédiatemment (interdiction d'aller-retour immédiat),
#   on interdit de revenir à partir du sommet parent.
# - On fait une DFS avec mémorisation pour chaque sommet, en évitant l'arête entrante.
# - On garde un tableau visited global pour marquer les sommets déjà visités (pour le comptage des points).
# 
# Complexité :
# - Chaque sommet et chaque arête sont visités une fois.
# - DP mémorisé par sommet.

N, M = map(int, input().split())
w = list(map(int, input().split()))

graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

visited = [False] * N  # marque si un sommet a été visité au moins une fois pour compter son poids

from functools import lru_cache

sys.setrecursionlimit(10**7)

@lru_cache(None)
def dfs(node, parent):
    # Si ce sommet n'a jamais été visité auparavant dans cet appel global, on ajoute son poids
    first_visit_gain = 0
    if not visited[node]:
        first_visit_gain = w[node]
        visited[node] = True

    max_extra = 0
    # Explorer tous les voisins sauf le parent (on ne peut pas reprendre l'arête directe de retour)
    for nxt in graph[node]:
        if nxt == parent:
            continue
        val = dfs(nxt, node)
        if val > max_extra:
            max_extra = val

    # Quand on remonte, on ne remet pas visited[node] à False car on veut garder la trace des visites uniques
    # De cette façon, on ne recompte jamais un sommet.
    return first_visit_gain + max_extra

# On start au sommet 0 (numéro 1)
res = dfs(0, -1)
print(res)