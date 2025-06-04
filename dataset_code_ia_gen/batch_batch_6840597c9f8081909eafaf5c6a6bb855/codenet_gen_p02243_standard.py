import sys
import heapq

input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n):
    data = list(map(int, input().split()))
    u, k = data[0], data[1]
    for i in range(k):
        v, c = data[2 + 2*i], data[3 + 2*i]
        graph[u].append((v, c))

dist = [float('inf')] * n
dist[0] = 0
heap = [(0, 0)]
while heap:
    cur_d, u = heapq.heappop(heap)
    if dist[u] < cur_d:
        continue
    for v, w in graph[u]:
        nd = cur_d + w
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(heap, (nd, v))

for i in range(n):
    print(i, dist[i])