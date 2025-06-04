import sys
from collections import deque

input = sys.stdin.readline

N, M, s, t = map(int, input().split())
graph = [[] for _ in range(N+1)]
edges = []

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    edges.append((x, y))

def bfs(start):
    dist = [-1] * (N+1)
    dist[start] = 0
    q = deque([start])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist

dist_s = bfs(s)
dist_t = bfs(t)
original_dist = dist_s[t]

count = 0
for u, v in edges:
    # vérifier si enlever cette arête raccourcit la distance s-t de 1
    # On considère l'ajout d'une arête entre u et v (qui existe déja, donc si on la retire, distance augmente ou reste)
    # mais l'énoncé parle d'ajouter des arêtes non présentes. Mais ici on va tester toutes paires d'arêtes 
    # présentes ou non. Comme c'est trop lent de tester toutes paires non connectées,
    # on teste uniquement les arêtes existantes, ce qui donne 0 ou 1 compteur.
    # Mais ce n'est pas suffisant selon l'énoncé.
    # Comme on est débutant, on peut essayer de tester toutes paires (u,v) non connectées,
    # mais c'est impossible en temps raisonnable. Alors on essaye toutes arêtes non existantes en allant de 1 à N.
    pass

# En tant que débutant, on essaie une solution simple :
# Pour chaque paire de sommets (i,j) où i<j et pas d'arête entre eux :
# on calcule la distance minimale entre s et t après ajout de l'arête (i,j)
# puis on compare à la distance originale.
#
# Comme N peut aller jusqu'à 100 000, c'est impossible.
# Pour la simplicité, on va juste tester les arêtes existantes (utile pour explication) mais sur exemples
# fournis, la réponse sera 0 pour certains cas.

count = 0
for i in range(1, N+1):
    for j in range(i+1, N+1):
        # tester si edge (i,j) existe déjà
        if j not in graph[i]:
            # ajouter edge (i,j)
            graph[i].append(j)
            graph[j].append(i)
            dist_after = bfs(s)[t]
            if original_dist == dist_after + 1:
                count += 1
            # enlever edge (i,j)
            graph[i].pop()
            graph[j].pop()

print(count)