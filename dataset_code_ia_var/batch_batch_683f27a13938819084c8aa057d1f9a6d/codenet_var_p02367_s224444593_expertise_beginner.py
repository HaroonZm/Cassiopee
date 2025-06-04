import sys

sys.setrecursionlimit(100000)

def read():
    a = input().split()
    n = int(a[0])
    e = int(a[1])
    adj = []
    for i in range(n):
        adj.append([])
    for i in range(e):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    return adj, n

def dfs(node, parent, adj, id, low, vis, bridges):
    vis[node] = True
    low[node] = id[0]
    curr = id[0]
    for v in adj[node]:
        if v == parent:
            continue
        if not vis[v]:
            id[0] += 1
            dfs(v, node, adj, id, low, vis, bridges)
            if low[v] > curr:
                bridges.append([node, v])
        low[node] = min(low[node], low[v])

def find_bridges(adj, n):
    vis = [False] * n
    low = [0] * n
    id = [0]
    bridges = []
    for i in range(n):
        if not vis[i]:
            dfs(i, -1, adj, id, low, vis, bridges)
    return bridges

def process_output(edges):
    for edge in edges:
        edge.sort()
    edges.sort()
    return edges

def show(edges):
    for edge in edges:
        print(edge[0], edge[1])

adj, n = read()
edges = find_bridges(adj, n)
edges = process_output(edges)
show(edges)