import sys
import heapq
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# Pour résoudre ce problème, il faut comparer les distances minimales entre l'intersection 1 (pizzeria)
# et l'intersection 2 (maison d'Alyssa) dans le graphe original, puis simuler 
# la situation où l'orientation d'une seule route est inversée.
#
# Approche:
# 1. Calculer la plus courte distance de 1 à tous les sommets (dist1) avec Dijkstra sur le graphe initial.
# 2. Calculer la plus courte distance de 2 à tous les sommets (dist2) avec Dijkstra sur le graphe inverse
#    (car on veut rapidement évaluer la distance depuis un sommet donné vers 2).
#
# Pour chaque arête i (a_i -> b_i) avec coût c_i qui est inversée le jour i:
# - On enlève temporairement cette arête (uniquement pour le calcul théorique)
# - On ajoute son inverse (b_i -> a_i) avec même coût c_i (qui sera la seule modification ce jour là)
#
# Le plus court chemin modifié peut être:
# - Plus court si on peut passer par b_i -> a_i -> ... -> 2 et atteindrons 1 depuis a_i auparavant
# - Plus long ou infini (plus de chemin), si on perd un chemin existant par a_i -> b_i
#
# On calcule donc pour ce jour la distance:
# min(
#   dist1[2],                                       # chemin initial sans modification
#   dist1[b_i] + c_i + dist2[a_i]                   # chemin utilisant la route inversée ce jour
# )
#
# - dist1[x] = distance de 1 à x dans graphe original
# - dist2[x] = distance de x à 2 dans graphe original (calculée comme distance de 2 à x dans graphe inverse)
#
# Cette formule vient de la décomposition des chemins:
# 1->b_i (distance dist1[b_i]) + c_i (arête inversée) + b_i->a_i (sens inversé) + a_i->2 (dist2[a_i])
# mais on exprime b_i->a_i par le chemin inversé: b_i -> a_i équivaut à a_i -> b_i inversé donc on calcule
# dist2[a_i] = distance de a_i à 2.
#
# Enfin on compare:
# - Si le nouveau minimum < dist1[2] : "HAPPY"
# - Si le nouveau minimum == dist1[2]: "SOSO"
# - Sinon (pas possible de rejoindre 2 ou plus long): "SAD"

def dijkstra(start, graph, n):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        cur_d, u = heapq.heappop(heap)
        if dist[u] < cur_d:
            continue
        for v, cost in graph[u]:
            nd = cur_d + cost
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist

def main():
    n, m = map(int, input().split())
    edges = []
    graph = [[] for _ in range(n + 1)]
    rev_graph = [[] for _ in range(n + 1)]  # graphe avec arêtes inversées pour dijkstra depuis 2
    
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
        graph[a].append((b, c))
        rev_graph[b].append((a, c))
    
    # Distance depuis 1 vers tous les sommets
    dist1 = dijkstra(1, graph, n)
    # Distance depuis 2 vers tous les sommets dans le graphe original,
    # donc distance de chaque sommet vers 2 dans le graphe original
    dist2 = dijkstra(2, rev_graph, n)
    
    dist_orig = dist1[2]  # distance originale de 1 à 2
    
    for i in range(m):
        a, b, c = edges[i]
        # Calcul du cout en prenant en compte inversion de l'arête i
        # Nouveau chemin possible: 1->b + c + a->2
        # => dist1[b] + c + dist2[a]
        # Si ce chemin est meilleur alors HAPPY,
        # sinon comparer avec chemin origine
        
        if dist1[b] == float('inf') or dist2[a] == float('inf'):
            # Impossible de faire un chemin via cette inversion
            new_dist = float('inf')
        else:
            new_dist = dist1[b] + c + dist2[a]
        
        if new_dist < dist_orig:
            print("HAPPY")
        elif new_dist == dist_orig:
            print("SOSO")
        else:
            print("SAD")

if __name__ == "__main__":
    main()