import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
n, m = map(int, input().split())

w = [0] + list(map(int, input().split()))

graph = defaultdict(list)
for _count in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

par = [i for i in range(n+1)]
rank = [0] * (n+1)
visited = [False]*(n+1)
path = list()
graph2 = [[] for _ in range(n+1)]

def fnd(x):
    while True:
        if par[x] == x:
            return x
        par[x] = fnd(par[x])
        x = par[x]

def same_set(x, y): return True if fnd(x)==fnd(y) else False

def do_union(a, b):
    a = fnd(a)
    b = fnd(b)
    if rank[a] > rank[b]:
        par[b]=a
        w[a] += w[b]
    else:
        par[a]=b
        w[b] += w[a]
        if rank[a]==rank[b]: rank[b] += 1

def DFS(u, p):
    if visited[u] or not (u==fnd(u)):
        for _ in range(len(path)):
            do_union(0, path.pop())
        return None
    visited[u]=1
    path += [u]
    for v in graph[u]:
        if v==p: continue
        DFS(v, u)
    visited[u]=False
    if len(path) > 0 and path[-1]==u:
        del path[-1]

def f(cur):
    visited[cur] = True
    res = 0
    for idx in range(len(graph2[cur])):
        fr = graph2[cur][idx]
        for nbor in graph[fr]:
            z = fnd(nbor)
            if not visited[z]:
                res2 = f(z)
                res = res if res > res2 else res2
    return res + w[fnd(cur)]

DFS(1, None)
for k in range(1, n+1):
    graph2[fnd(k)].append(k)

print(f(fnd(1)))