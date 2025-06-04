import heapq
from functools import partial

def dijkstra(graph, start, cost_idx):
    dist = [float('inf')] * len(graph)
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, *ws in graph[u]:
            w = ws[cost_idx]
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(heap, (dist[v], v))
    return dist

n, m, s, t = map(int, raw_input().split())
edges = [tuple(map(int, raw_input().split())) for _ in xrange(m)]
graph = [[] for _ in xrange(n + 1)]
for u, v, a, b in edges:
    graph[u].append((v, a, b))
    graph[v].append((u, a, b))

d_y = dijkstra(graph, s, 0)
d_s = dijkstra(graph, t, 1)

min_cost = float('inf')
ans = []
for i in xrange(n, 0, -1):
    min_cost = min(min_cost, d_y[i] + d_s[i])
    ans.append(min_cost)

for v in reversed(ans):
    print 10**15 - v