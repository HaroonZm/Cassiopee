from heapq import heappop, heappush
import sys

N, M, X = map(int, input().split())
tree_height = [0] + [int(sys.stdin.readline()) for _ in range(N)]
edges = [[] for _ in range(N + 1)]
for a, b, t in (map(int, l.split()) for l in sys.stdin):
    edges[a].append((b, t))
    edges[b].append((a, t))

vertices = [float("inf")] * (N + 1)
pq = [(0, 1, X)]
while pq:
    time, v, height = heappop(pq)
    if v == N:
        print(time + (tree_height[v] - height))
        exit()
    if time > vertices[v]:
        continue
    max_height = tree_height[v]
    for to, dist in edges[v]:
        if max_height - dist < 0:
            continue
        new_height = height - dist
        new_time = time + dist
        if new_height < 0:
            new_time = new_time - new_height
            new_height = 0
        elif new_height > tree_height[to]:
            new_time = new_time + (new_height - tree_height[to])
            new_height = tree_height[to]
        if vertices[to] > new_time:
            vertices[to] = new_time
            heappush(pq, (new_time, to, new_height))
print(-1)