import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import time,random

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
mod2 = 998244353
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

n = int(sys.stdin.readline())
wa = []
for _ in range(n):
    wa.append(list(map(int, sys.stdin.readline().split())))
ea = []
for _ in range(n):
    ea.append(list(map(int, sys.stdin.readline().split())))
fa = []
for _ in range(n):
    fa.append([c == 'o' for c in sys.stdin.readline().strip()])

s = n*2
t = n*2+1
graph = [[] for _ in range(n*2+2)]

class Edge:
    def __init__(self, t, f, r, ca, co):
        self.to = t
        self.fron = f
        self.rev = r
        self.cap = ca
        self.cost = co

sz = n*2+2

for i in range(n):
    graph[s].append(Edge(i, s, len(graph[i]), 1, 0))
    graph[i].append(Edge(s, i, len(graph[s])-1, 0, 0))
    graph[i+n].append(Edge(t, i+n, len(graph[t]), 1, 0))
    graph[t].append(Edge(i+n, t, len(graph[i+n])-1, 0, 0))
    fs = set([j for j in range(n) if fa[i][j]])
    fc = sum([ea[i][j] for j in fs])
    for j in range(n):
        if j in fs:
            graph[i].append(Edge(j+n, i, len(graph[j+n]), 1, fc-ea[i][j]))
            graph[j+n].append(Edge(i, j+n, len(graph[i])-1, 0, -(fc-ea[i][j])))
        else:
            graph[i].append(Edge(j+n, i, len(graph[j+n]), 1, fc+wa[i][j]))
            graph[j+n].append(Edge(i, j+n, len(graph[i])-1, 0, -(fc+wa[i][j])))

def min_path(graph, sz, s, t):
    dist = [inf] * sz
    route = [None] * sz
    que = collections.deque()
    inq = [False] * sz
    dist[s] = 0
    que.append(s)
    inq[s] = True
    while que:
        u = que.popleft()
        inq[u] = False
        for idx, e in enumerate(graph[u]):
            if e.cap == 0:
                continue
            v = e.to
            if dist[v] > dist[u] + e.cost:
                dist[v] = dist[u] + e.cost
                route[v] = (u, idx)
                if not inq[v]:
                    que.append(v)
                    inq[v] = True
    if dist[t] == inf:
        return inf, 0
    flow = inf
    v = t
    while v != s:
        u, idx = route[v]
        e = graph[u][idx]
        if flow > e.cap:
            flow = e.cap
        v = u
    c = 0
    v = t
    while v != s:
        u, idx = route[v]
        e = graph[u][idx]
        e.cap -= flow
        graph[e.to][e.rev].cap += flow
        c += e.cost * flow
        v = u
    return dist[t], flow

total_cost = 0
flow = n
while flow > 0:
    c, f = min_path(graph, sz, s, t)
    if f == 0:
        total_cost = inf
        break
    f = min(flow, f)
    total_cost += c * f
    flow -= f

ra = [[False]*n for _ in range(n)]
for gr in graph:
    for g in gr:
        if g.fron >= n or g.cap > 0:
            continue
        if g.to>=n and g.to<t and g.fron<n:
            ra[g.fron][g.to-n] = True

rr = []
for i in range(n):
    for j in range(n):
        if fa[i][j] == ra[i][j]:
            continue
        if fa[i][j]:
            rr.append("{} {} erase".format(i+1, j+1))
        else:
            rr.append("{} {} write".format(i+1, j+1))

def JA(a, sep):
    return sep.join(map(str, a))

print(JA([total_cost, len(rr)] + rr, "\n"))