from heapq import heappush, heappop
import sys

input = sys.stdin.readline
N, M, X = map(int, input().split())
tree_height = [0] + [int(input()) for _ in range(N)]
edges = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, t = map(int, input().split())
    edges[a].append((b, t))
    edges[b].append((a, t))

inf = float('inf')
dist = [inf] * (N + 1)
pq = [(0, 1, X)]

while pq:
    time, node, height = heappop(pq)
    if node == N:
        print(time + tree_height[node] - height)
        break
    if time > dist[node]:
        continue
    dist[node] = time
    max_h = tree_height[node]
    for nxt, cost in edges[node]:
        nh = height - cost
        nt = time + cost
        if nh < 0:
            nt -= nh
            nh = 0
        elif nh > tree_height[nxt]:
            nt += nh - tree_height[nxt]
            nh = tree_height[nxt]
        if nh < 0 or nh > max_h:
            continue
        if dist[nxt] > nt:
            dist[nxt] = nt
            heappush(pq, (nt, nxt, nh))
else:
    print(-1)