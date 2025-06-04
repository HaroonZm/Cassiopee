import sys
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())

edges = [[] for _ in range(n)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append((b, c))
    edges[b].append((a, c))

s = list(map(int, input().split()))

# Calculer toutes les distances entre les nodes avec DFS (peu optimal mais simple)
def dfs(start):
    dist = [-1]*n
    dist[start] = 0
    stack = [start]
    while stack:
        u = stack.pop()
        for v, w in edges[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + w
                stack.append(v)
    return dist

distances = []
for i in range(n):
    distances.append(dfs(i))

max_cost_first = 0
# Choisir source et destination pour la première livraison afin de maximiser s_source * dist(source,dest)
for src in range(n):
    for dest in range(n):
        if src != dest:
            cost = s[src] * distances[src][dest]
            if cost > max_cost_first:
                max_cost_first = cost
                best_src = src
                best_dest = dest

# Après la 1ère livraison, les noeuds sur le chemin entre best_src et best_dest ont le cache du s_source

# Trouver le chemin entre best_src et best_dest en DFS simple
parent = [-1]*n
def find_path(u, goal):
    stack = [u]
    visited = [False]*n
    visited[u] = True
    while stack:
        node = stack.pop()
        if node == goal:
            break
        for nxt, _ in edges[node]:
            if not visited[nxt]:
                visited[nxt] = True
                parent[nxt] = node
                stack.append(nxt)

find_path(best_src, best_dest)

path = []
cur = best_dest
while cur != -1:
    path.append(cur)
    cur = parent[cur]
path = path[::-1]

cached_nodes = set(path)

max_cost_after = 0
# Pour les livraisons suivantes, la source peut être n'importe quel noeud qui a le cache
# Choisir destination et donnée pour maximiser s_data * distance(min_cache_node, destination)
for data_node in range(n):
    for dest in range(n):
        # Trouver la distance minimale entre dest et n'importe quel noeud dans cached_nodes
        min_dist = 10**15
        for cached in cached_nodes:
            if distances[cached][dest] < min_dist:
                min_dist = distances[cached][dest]
        cost = s[data_node] * min_dist
        if cost > max_cost_after:
            max_cost_after = cost

# Si m=1, alors le coût max est celui de la première livraison,
# sinon, c'est max_cost_after * (m-1) + max_cost_first

if m == 1:
    print(max_cost_first)
else:
    print(max_cost_first + max_cost_after * (m-1))