import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())
edges = [[] for _ in range(N+1)]

for _ in range(N):
    u, v = map(int, sys.stdin.readline().split())
    edges[u].append(v)
    edges[v].append(u)

Q = int(sys.stdin.readline())
queries = [tuple(map(int, sys.stdin.readline().split())) for _ in range(Q)]

# On va utiliser un algo de recherche de ponts dans le graphe pour trouver les arêtes qui sont des ponts
# Puis construire un graphe des composantes 2-edge-connected et répondre aux questions par la distance entre composants

time = 0
low = [0]*(N+1)
disc = [0]*(N+1)
stack = []
visited = [False]*(N+1)
bridges = set()

def dfs(u, p):
    global time
    time += 1
    low[u] = disc[u] = time
    visited[u] = True
    for w in edges[u]:
        if w == p:
            continue
        if not visited[w]:
            dfs(w, u)
            low[u] = min(low[u], low[w])
            if low[w] > disc[u]:
                # u-w est un pont
                if u < w:
                    bridges.add((u, w))
                else:
                    bridges.add((w, u))
        else:
            low[u] = min(low[u], disc[w])

dfs(1, -1)

# Construire un graphe contracté dans lequel chaque composante 2-edge-connected est un noeud
comp_id = [0]*(N+1)
current_comp = 0
visited2 = [False]*(N+1)

def dfs_comp(u):
    stack = [u]
    comp = []
    visited2[u] = True
    while stack:
        cur = stack.pop()
        comp.append(cur)
        comp_id[cur] = current_comp
        for w in edges[cur]:
            if visited2[w]:
                continue
            a,b = (cur, w) if cur<w else (w, cur)
            if (a,b) in bridges:
                continue
            visited2[w] = True
            stack.append(w)
    return comp

for i in range(1, N+1):
    if not visited2[i]:
        current_comp +=1
        dfs_comp(i)

# Le graphe des composantes est un arbre, chaque arête correspond à un pont dans le graphe original
tree = [[] for _ in range(current_comp+1)]
for u,v in bridges:
    cu = comp_id[u]
    cv = comp_id[v]
    tree[cu].append(cv)
    tree[cv].append(cu)

# Préparation pour répondre aux queries :
# On veut la distance (nombre d'arêtes) entre les composantes de a_i et b_i dans cet arbre.
# On va faire un LCA avec levelling pour calculer la distance rapidement.

LOG = 20
parent = [[-1]*(current_comp+1) for _ in range(LOG)]
depth = [0]*(current_comp+1)
visited3 = [False]*(current_comp+1)

def dfs_lca(u):
    visited3[u] = True
    for w in tree[u]:
        if visited3[w]:
            continue
        depth[w] = depth[u]+1
        parent[0][w] = u
        dfs_lca(w)

dfs_lca(1)

for k in range(1, LOG):
    for v in range(1, current_comp+1):
        if parent[k-1][v] != -1:
            parent[k][v] = parent[k-1][parent[k-1][v]]

def lca(u, v):
    if depth[u] < depth[v]:
        u, v = v, u
    diff = depth[u] - depth[v]
    for k in range(LOG):
        if diff & (1 << k):
            u = parent[k][u]
    if u == v:
        return u
    for k in range(LOG-1, -1, -1):
        if parent[k][u] != -1 and parent[k][u] != parent[k][v]:
            u = parent[k][u]
            v = parent[k][v]
    return parent[0][u]

for a, b in queries:
    ca = comp_id[a]
    cb = comp_id[b]
    l = lca(ca, cb)
    dist = depth[ca] + depth[cb] - 2*depth[l]
    print(dist)