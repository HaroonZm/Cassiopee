import sys
import heapq
from functools import partial

input = sys.stdin.readline

n, m, s, t = map(int, input().split())
edges = [([], []) for _ in range(n)]
encode = lambda cost, v: (cost << 20) | v
decode = lambda x: (x >> 20, x & ((1 << 20) - 1))

for _ in range(m):
    u, v, a, b = map(int, input().split())
    u -= 1; v -= 1
    edges[u][0].append((a, v))
    edges[v][0].append((a, u))
    edges[u][1].append((b, v))
    edges[v][1].append((b, u))

def dijkstra(graph, start):
    dist = [float('inf')] * n
    visited = [False] * n
    hq = [(0, start)]
    dist[start] = 0
    while hq:
        d, u = heapq.heappop(hq)
        if visited[u]: continue
        visited[u] = True
        for cost, v in graph[u]:
            nd = d + cost
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(hq, (nd, v))
    return dist

d1 = dijkstra([g[0] for g in edges], s - 1)
d2 = dijkstra([g[1] for g in edges], t - 1)
acc = float('inf')
result = []
for x, y in zip(reversed(d1), reversed(d2)):
    acc = min(acc, x + y)
    result.append(acc)
for val in reversed(result):
    print(10**15 - val)