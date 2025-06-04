import sys
from heapq import heapify, heappop, heappush

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

def dijkstra(start):
    INF = 10 ** 15
    dist = [INF] * (N + 1)
    dist[start] = 0
    que = [(0, start)]
    while que:
        d, prev = heappop(que)
        if dist[prev] < d:
            continue
        for nxt in graph[prev]:
            d1 = d + 1
            if dist[nxt] > d1:
                dist[nxt] = d1
                heappush(que, (d1, nxt))
    return dist

N = ir()
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = lr()
    graph[a].append(b)
    graph[b].append(a)

dist = dijkstra(1)
dist = sorted([(x, i) for i, x in enumerate(dist)], reverse=True)
new_root = dist[1][1]
dist = dijkstra(new_root)
diameter = max(dist[1:]) + 1
bl = diameter % 3 != 2
print('First' if bl else 'Second')