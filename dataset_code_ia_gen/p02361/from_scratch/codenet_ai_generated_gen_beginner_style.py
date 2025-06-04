import sys
import heapq

input = sys.stdin.readline

V, E, r = map(int, input().split())

graph = [[] for _ in range(V)]
for _ in range(E):
    s, t, d = map(int, input().split())
    graph[s].append((t, d))

INF = 10**15
dist = [INF] * V
dist[r] = 0

q = []
heapq.heappush(q, (0, r))

while q:
    current_dist, current_vertex = heapq.heappop(q)
    if dist[current_vertex] < current_dist:
        continue
    for neighbor, cost in graph[current_vertex]:
        new_dist = current_dist + cost
        if new_dist < dist[neighbor]:
            dist[neighbor] = new_dist
            heapq.heappush(q, (new_dist, neighbor))

for d in dist:
    if d == INF:
        print("INF")
    else:
        print(d)