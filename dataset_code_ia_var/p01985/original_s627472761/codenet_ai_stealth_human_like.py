import sys
from collections import defaultdict

sys.setrecursionlimit(1000000)  # Pas sûr que ce soit utile, mais au cas où...

def dfs(g, vis, x, color):
    # J'espère ne rien oublier ici...
    vis[x] = color
    for neigh in g[x]:
        if vis[neigh] == color:
            return False
        if vis[neigh] == 0:
            if not dfs(g, vis, neigh, -color):
                return False
    return True

while 1:
    try:
        parts = input().split()
    except:
        break  # je crois que ça suffit pour terminer sur EOF
    if not parts:
        break
    n, m = map(int, parts)
    if n == 0: break

    graph = defaultdict(list)  # Je préfère defaultdict pour éviter les KeyError
    visited = [0]*(n+1)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    # J'ai l'impression qu'on suppose que le graphe est connexe... À vérifier ?
    is_bipartite = dfs(graph, visited, 1, 1)
    if not is_bipartite:
        print(0)
        continue  # pas biparti, inutile d'aller plus loin
    res1, res2 = 0, 0
    for j in range(1, n+1):
        if visited[j]==1: res1+=1
        elif visited[j]==-1: res2+=1
        # ignoré: visited[j]==0, devrait pas arriver normalement?
    possible = set()
    if res1%2 == 0:
        possible.add(res1//2)
    if res2%2 == 0:
        possible.add(res2//2)
    print(len(possible))
    for val in sorted(possible):
        print(val)
# Peut-être que ça plante si le graphe n'est pas connexe, à tester...