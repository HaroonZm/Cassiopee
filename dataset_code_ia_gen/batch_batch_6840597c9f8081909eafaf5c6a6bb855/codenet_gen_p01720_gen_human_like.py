import sys
from collections import deque

input = sys.stdin.readline

N, M, s, t = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(start):
    dist = [-1] * (N + 1)
    dist[start] = 0
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for nv in graph[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                queue.append(nv)
    return dist

dist_s = bfs(s)
dist_t = bfs(t)
original_distance = dist_s[t]

count = 0
# For pairs of vertices (u,v) without an edge, check if adding edge reduces distance by 1
# Instead of checking all pairs (N^2), we use BFS distances:
# If dist_s[u] + 1 + dist_t[v] < original_distance or dist_s[v] + 1 + dist_t[u] < original_distance,
# then adding edge {u,v} reduces shortest path length.
# But dist_s[u] + 1 + dist_t[v] == original_distance - 1 means count++.

# To efficiently check whether edge exists, build a set for each adjacency
edge_set = [set() for _ in range(N + 1)]
for u in range(1, N + 1):
    for v in graph[u]:
        edge_set[u].add(v)

for u in range(1, N + 1):
    for v in range(u + 1, N + 1):
        if v in edge_set[u]:
            continue
        # Check conditions
        if dist_s[u] == -1 or dist_t[v] == -1:
            continue
        if dist_s[v] == -1 or dist_t[u] == -1:
            continue
        # Check if adding edge {u,v} shortens path by 1
        if dist_s[u] + 1 + dist_t[v] == original_distance - 1 or dist_s[v] + 1 + dist_t[u] == original_distance - 1:
            count += 1

print(count)