from sys import stdin
from collections import defaultdict

N, M = map(int, stdin.readline().split())
edges = [tuple(map(int, stdin.readline().split())) for _ in range(M)]
edges = [(c, s-1, d-1) for s, d, c in edges]
edges.sort()

parent = list(range(N))
rank = [0] * N

def find(x):
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(x, y):
    x_root, y_root = find(x), find(y)
    if x_root == y_root: return False
    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    else:
        parent[y_root] = x_root
        if rank[x_root] == rank[y_root]:
            rank[x_root] += 1
    return True

mst_cost = None
cnt = 0
for c, s, d in edges:
    if union(s, d):
        cnt += 1
        if cnt == N - 1:
            mst_cost = c
            break

es = defaultdict(set)
cm = {}
for c, s, d in edges:
    if c <= mst_cost:
        es[c].add((s, d))
        cm[(s, d)] = c

def bridge(graph, N):
    index = [-1] * N
    low = [0] * N
    bridges = set()
    i = 0
    def dfs(u, parent, idx):
        nonlocal i
        index[u] = low[u] = i
        i += 1
        for v in graph[u]:
            if v == parent:
                continue
            if index[v] == -1:
                dfs(v, u, idx+1)
                low[u] = min(low[u], low[v])
                if low[v] > index[u]:
                    bridges.add(tuple(sorted((u, v))))
            else:
                low[u] = min(low[u], index[v])
    for v in range(N):
        if index[v] == -1:
            dfs(v, -1, 0)
    return bridges

G = [[] for _ in range(N)]
total_cnt = total_ans = 0
for c in sorted(es):
    for s, d in es[c]:
        G[s].append(d)
        G[d].append(s)
    br = bridge(G, N)
    relevant = br & es[c]
    total_cnt += len(relevant)
    total_ans += c * len(relevant)
print(total_cnt, total_ans)