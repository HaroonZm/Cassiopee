import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, Q = map(int, input().split())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    u,v,w = map(int, input().split())
    tree[u].append((v,w))
    tree[v].append((u,w))

LOG = 17
while (1<<LOG) <= N:
    LOG += 1

parent = [[-1]*(N+1) for _ in range(LOG)]
depth = [0]*(N+1)
dist = [0]*(N+1)

def dfs(u, p):
    for v, w in tree[u]:
        if v==p:
            continue
        depth[v] = depth[u] + 1
        dist[v] = dist[u] + w
        parent[0][v] = u
        dfs(v,u)

dfs(1,-1)

for k in range(LOG-1):
    for v in range(1,N+1):
        if parent[k][v]<0:
            parent[k+1][v] = -1
        else:
            parent[k+1][v] = parent[k][parent[k][v]]

def lca(u,v):
    if depth[u]>depth[v]:
        u,v = v,u
    # depth[u] <= depth[v]
    for k in range(LOG):
        if ((depth[v]-depth[u]) >> k) &1:
            v = parent[k][v]
    if u==v:
        return u
    for k in reversed(range(LOG)):
        if parent[k][u]!=parent[k][v]:
            u = parent[k][u]
            v = parent[k][v]
    return parent[0][u]

def distance(u,v):
    w = lca(u,v)
    return dist[u] + dist[v] - 2*dist[w]

for _ in range(Q):
    a,b,c = map(int, input().split())

    # On a tree, the meeting point minimizing max distance to a,b,c
    # is one of the three nodes: a,b,c,m where m is the median on the path.
    # Actually, the min max distance is min over meeting city x of max(dist(a,x), dist(b,x), dist(c,x))
    # in tree, it is minimum over x in {a,b,c, LCA(a,b), LCA(b,c), LCA(c,a)}.
    candidates = [a,b,c]
    candidates.append(lca(a,b))
    candidates.append(lca(b,c))
    candidates.append(lca(c,a))

    res = 10**15
    for x in candidates:
        mx = max(distance(a,x), distance(b,x), distance(c,x))
        if mx < res:
            res = mx
    print(res)