# Implémentation de l'algorithme de Dijkstra pour trouver le plus court chemin depuis la source 0 vers tous les sommets.
# Approach:
# - On lit le graphe sous forme d'une liste d'adjacence où chaque sommet u contient une liste des tuples (v, c)
#   représentant les arcs sortants avec leur poids associé.
# - On utilise une file de priorité (heapq) pour toujours extraire le sommet avec la distance actuelle la plus courte.
# - On met à jour les distances lorsque l'on trouve un chemin plus court vers un sommet.
# - Puis on affiche la distance de chaque sommet par rapport à la source 0.

import sys
import heapq

def dijkstra(n, graph, source=0):
    # Initialisation des distances : infini sauf la source à 0
    dist = [float('inf')] * n
    dist[source] = 0

    # File de priorité contenant les paires (distance, sommet)
    heap = [(0, source)]

    while heap:
        current_dist, u = heapq.heappop(heap)

        # Si cette distance est plus grande que celle déjà trouvée, on skip
        if current_dist > dist[u]:
            continue

        # Exploration des voisins
        for v, weight in graph[u]:
            new_dist = current_dist + weight
            # Si on trouve un chemin plus court vers v, on le met à jour
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(heap, (new_dist, v))

    return dist

def main():
    input = sys.stdin.readline
    n = int(input())
    graph = [[] for _ in range(n)]

    # Lecture du graphe
    for _ in range(n):
        line = list(map(int, input().split()))
        u = line[0]
        k = line[1]
        # Chaque paire (v_i, c_i) commence à l'indice 2
        for i in range(k):
            v = line[2 + 2*i]
            c = line[3 + 2*i]
            graph[u].append((v, c))

    dist = dijkstra(n, graph, source=0)

    # Affichage du résultat
    for u in range(n):
        print(u, dist[u])

if __name__ == "__main__":
    main()