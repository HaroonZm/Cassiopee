import sys
import heapq
from collections import deque

input = sys.stdin.readline
N, M, K, S = map(int, input().split())
P, Q = map(int, input().split())
zombies = [int(input()) for _ in range(K)]

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# Distance to nearest zombie for each town, initialize with -1 (unvisited)
dist = [-1] * (N + 1)
que = deque()

# Start BFS from all zombie towns
for z in zombies:
    dist[z] = 0
    que.append(z)

while que:
    cur = que.popleft()
    if dist[cur] == S:
        continue
    for nxt in graph[cur]:
        if dist[nxt] == -1:
            dist[nxt] = dist[cur] + 1
            que.append(nxt)

# Determine cost for staying at each town
# 1 and N are never stayed in, cost zero assigned here
cost = [0] * (N + 1)
for i in range(2, N):
    if dist[i] != -1 and dist[i] <= S:
        cost[i] = Q
    else:
        cost[i] = P

# Use Dijkstra to find minimal total cost from 1 to N
# Cost when "arriving" at town, i.e. paying at that town
INF = 10**15
dp = [INF] * (N + 1)
dp[1] = 0
hq = [(0, 1)]
while hq:
    c, v = heapq.heappop(hq)
    if dp[v] < c:
        continue
    if v == N:
        print(c)
        break
    for nv in graph[v]:
        nc = c + cost[nv]
        if dp[nv] > nc:
            dp[nv] = nc
            heapq.heappush(hq, (nc, nv))