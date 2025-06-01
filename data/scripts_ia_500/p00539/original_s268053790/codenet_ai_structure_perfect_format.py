from collections import deque
import heapq

def dijkstra(s, g):
    color = [0] * n
    dis = {}
    for i in xrange(n):
        dis[i] = float('inf')
    dis[s] = 0
    heapq.heappush(pq, [0, s])
    while len(pq) != 0:
        t, u = heapq.heappop(pq)
        color[u] = 2
        if dis[u] < t:
            continue
        for v, cost in g[u]:
            if color[v] != 2:
                if dis[u] + cost < dis[v]:
                    dis[v] = dis[u] + cost
                    color[v] = 1
                    heapq.heappush(pq, [dis[v], v])
    return dis

n, m, c = map(int, raw_input().split())
g = [[] for _ in xrange(n)]
totalcost = 0
for i in xrange(m):
    a, b, d = map(int, raw_input().split())
    g[a - 1].append([b - 1, d])
    g[b - 1].append([a - 1, d])
    totalcost += d

pq = []
dis = dijkstra(0, g)
dis = sorted(dis.items(), key=lambda x: x[1])

ans = float('inf')
visited = [0] * n
for u, x in dis:
    visited[u] = 1
    for v, cost in g[u]:
        if visited[v] == 1:
            totalcost -= cost
    ans = min(ans, totalcost + c * x)
print ans