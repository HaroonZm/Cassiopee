import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, Q = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

depth = [0]*(N+1)
dist = [0]*(N+1)
parent = [0]*(N+1)

def dfs(now, par):
    for nxt, w in graph[now]:
        if nxt != par:
            depth[nxt] = depth[now]+1
            dist[nxt] = dist[now]+w
            parent[nxt] = now
            dfs(nxt, now)

dfs(1, -1)

def lca(u,v):
    while depth[u] > depth[v]:
        u = parent[u]
    while depth[v] > depth[u]:
        v = parent[v]
    while u != v:
        u = parent[u]
        v = parent[v]
    return u

def distance(u,v):
    l = lca(u,v)
    return dist[u] + dist[v] - 2*dist[l]

for _ in range(Q):
    a,b,c = map(int, input().split())
    d_ab = distance(a,b)
    d_bc = distance(b,c)
    d_ca = distance(c,a)
    # trying meeting at a,b,c or the city on paths between
    # the minimal max travel distance is (d_ab + d_bc + d_ca)//2 or one of distances
    # But with beginner approach, just try the three meeting cities
    res = min( max(distance(a,a), max(distance(b,a),distance(c,a))),
               max(distance(a,b), max(distance(b,b),distance(c,b))),
               max(distance(a,c), max(distance(b,c),distance(c,c))))
    # The above is just trying meeting at a,b,c themselves
    print(res)