import sys
from heapq import heappush, heappop
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
E = [tuple(map(int, input().split())) for _ in range(m)]
E = [(a-1, b-1, c) for a, b, c in E]

G = [[] for _ in range(n)]
RG = [[] for _ in range(n)]
for i, (a, b, c) in enumerate(E):
    G[a].append((b, c, i))
    RG[b].append((a, c, i))

def dijkstra(graph, src):
    dist = [float('inf')] * n
    dist[src] = 0
    heap = [(0, src)]
    while heap:
        d_u, u = heappop(heap)
        if d_u > dist[u]: continue
        for v, w, _ in graph[u]:
            alt = d_u + w
            if alt < dist[v]:
                dist[v] = alt
                heappush(heap, (alt, v))
    return dist

D = dijkstra(G, 0)
RD = dijkstra(RG, 1)

G0 = [[] for _ in range(n)]
used = {1}
deq = deque([1])
P = set()
while deq:
    v = deq.popleft()
    for w, c, i in RG[v]:
        if D[w] + c == D[v]:
            P.add(i)
            if w not in used:
                used.add(w)
                deq.append(w)
            G0[v].append((w, i))
            G0[w].append((v, i))

PB = set()
label = [None] * n
cost = [0] * n

def dfs(u, p, edge_idx, level):
    label[u] = level
    res = 0
    parent_cnt = int(p != -1)
    for v, i in G0[u]:
        if v == p:
            continue
        if label[v] is not None:
            if label[v] < label[u]:
                cost[v] += 1
                res += 1
        else:
            res += dfs(v, u, i, level + 1)
    res -= cost[u]
    if res == 0 and p != -1 and parent_cnt == 1:
        PB.add(edge_idx)
    return res

dfs(0, -1, None, 0)

result = []
append = result.append
for i, (a, b, c) in enumerate(E):
    if i in P:
        append("SAD" if i in PB else "SOSO")
    elif D[b] + c + RD[a] < D[1]:
        append("HAPPY")
    else:
        append("SOSO")
print('\n'.join(result))