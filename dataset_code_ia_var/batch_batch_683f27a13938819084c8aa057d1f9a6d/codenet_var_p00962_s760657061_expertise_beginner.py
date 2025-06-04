import heapq
from collections import deque
import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
E = []
G = []
RG = []
for i in range(n):
    G.append([])
    RG.append([])

for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    E.append((a, b, c))
    G[a].append((b, c, i))
    RG[b].append((a, c, i))

def dijkstra(graph, start):
    INF = 10**18
    dist = [INF] * n
    dist[start] = 0
    h = []
    heapq.heappush(h, (0, start))
    while h:
        d, u = heapq.heappop(h)
        if dist[u] < d:
            continue
        for v, w, idx in graph[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(h, (dist[v], v))
    return dist

D = dijkstra(G, 0)
RD = dijkstra(RG, 1)

G0 = []
for i in range(n):
    G0.append([])

used = set()
used.add(1)
myqueue = deque()
myqueue.append(1)
P = set()

while myqueue:
    v = myqueue.popleft()
    for w, c, i in RG[v]:
        if D[w] + c == D[v]:
            P.add(i)
            if w not in used:
                used.add(w)
                myqueue.append(w)
            G0[v].append((w, i))
            G0[w].append((v, i))

PB = set()
label = [None] * n
gen = [1]  # use list for mutability in dfs
cost = [0] * n

def dfs(u, parent, edge_idx):
    res = 0
    cnt_parent = 0
    for v, idx in G0[u]:
        if v == parent:
            cnt_parent += 1
            continue
        if label[v] is not None:
            if label[v] < label[u]:
                cost[v] += 1
                res += 1
        else:
            label[v] = gen[0]
            gen[0] += 1
            res += dfs(v, u, idx)
    res -= cost[u]
    if res == 0 and parent != -1 and cnt_parent == 1:
        PB.add(edge_idx)
    return res

label[0] = 0
dfs(0, -1, None)

ans = []
for i in range(m):
    if i in P:
        if i in PB:
            ans.append("SAD")
        else:
            ans.append("SOSO")
    else:
        a, b, c = E[i]
        if D[b] + c + RD[a] < D[1]:
            ans.append("HAPPY")
        else:
            ans.append("SOSO")
for s in ans:
    print(s)