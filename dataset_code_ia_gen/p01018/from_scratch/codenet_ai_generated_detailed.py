import sys
import heapq

def warping_girl():
    # Lecture des données d'entrée
    L, n = map(int, sys.stdin.readline().split())
    warps = []
    for _ in range(n):
        P, D, T = map(int, sys.stdin.readline().split())
        warps.append((P, D, T))
    
    # On crée une liste de positions importantes : 
    # la position 0 (départ), la position L (arrivée), ainsi que toutes les positions de départs et destinations des warps.
    positions = set([0, L])
    for P, D, T in warps:
        positions.add(P)
        positions.add(P + D)
    
    # Trie des positions importantes
    sorted_positions = sorted(positions)
    # On crée un dictionnaire pour retrouver l'indice d'une position dans sorted_positions
    pos_index = {pos: i for i, pos in enumerate(sorted_positions)}
    
    # Nombre de positions importantes
    m = len(sorted_positions)
    
    # Création du graphe sous forme de liste d'adjacence
    # Chaque noeud est une position importante
    # Arêtes : marcher d'une position importante à l'autre (temps = distance),
    # ou warper de P à P+D (temps = T).
    graph = [[] for _ in range(m)]
    
    # Ajout des arêtes marcher:
    # On peut marcher entre position i et i+1 (car positions triées)
    for i in range(m - 1):
        dist = sorted_positions[i+1] - sorted_positions[i]
        # marche de i -> i+1 (temps = dist)
        graph[i].append((i+1, dist))
        # on ne peut pas revenir en arrière donc pas d'arête i+1 -> i
    
    # Ajout des arêtes warps:
    for P, D, T in warps:
        start_idx = pos_index[P]
        end_pos = P + D
        end_idx = pos_index[end_pos]
        # warp de start_idx vers end_idx en T minutes
        graph[start_idx].append((end_idx, T))
    
    # Utilisation de Dijkstra pour trouver le temps minimum pour aller à la position L
    dist = [float('inf')] * m
    dist[pos_index[0]] = 0
    heap = [(0, pos_index[0])]
    
    while heap:
        current_time, u = heapq.heappop(heap)
        if dist[u] < current_time:
            continue
        # Si on atteint la position L, on peut retourner le résultat direct
        if sorted_positions[u] == L:
            print(current_time)
            return
        for v, cost in graph[u]:
            new_time = current_time + cost
            if new_time < dist[v]:
                dist[v] = new_time
                heapq.heappush(heap, (new_time, v))
    
    # Au cas où (normalement pas nécessaire), on affiche la dist pour la position L
    print(dist[pos_index[L]])

if __name__ == "__main__":
    warping_girl()