import sys

def main():
    sys.setrecursionlimit(int(1e5))
    nvertices, nedges = map(int, input().split())
    Adj = [[] for _ in range(nvertices)]
    AdjRev = [[] for _ in range(nvertices)]
    for _ in range(nedges):
        u, v = map(int, input().split())
        Adj[u].append(v)
        AdjRev[v].append(u)
    lst = []
    visited = [False] * nvertices
    for u in range(nvertices):
        if not visited[u]:
            dfs_first(u, Adj, visited, lst)
    lst.reverse()
    ids = [-1] * nvertices
    visited = [False] * nvertices
    id = 0
    for u in lst:
        if not visited[u]:
            dfs_second(u, AdjRev, visited, id, ids)
            id += 1
    Q = int(input())
    for _ in range(Q):
        u, v = map(int, input().split())
        print(1 if ids[u] == ids[v] else 0)

def dfs_first(u, Adj, visited, lst):
    visited[u] = True
    for v in Adj[u]:
        if not visited[v]:
            dfs_first(v, Adj, visited, lst)
    lst.append(u)

def dfs_second(u, Adj, visited, id, ids):
    ids[u] = id
    visited[u] = True
    for v in Adj[u]:
        if not visited[v]:
            dfs_second(v, Adj, visited, id, ids)

main()