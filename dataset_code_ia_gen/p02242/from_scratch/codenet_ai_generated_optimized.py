import sys
import heapq

input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n):
    data = list(map(int, input().split()))
    u, k = data[0], data[1]
    edges = data[2:]
    for i in range(k):
        v, c = edges[2*i], edges[2*i+1]
        graph[u].append((v, c))

dist = [float('inf')] * n
dist[0] = 0
pq = [(0, 0)]
while pq:
    d, u = heapq.heappop(pq)
    if d > dist[u]:
        continue
    for v, w in graph[u]:
        nd = d + w
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))

for i, d in enumerate(dist):
    print(i, d)