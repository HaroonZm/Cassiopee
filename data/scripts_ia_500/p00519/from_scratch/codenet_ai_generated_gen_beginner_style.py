import sys
sys.setrecursionlimit(10**7)

N, K = map(int, input().split())
C = [0] * (N + 1)
R = [0] * (N + 1)
for i in range(1, N + 1):
    c, r = map(int, input().split())
    C[i] = c
    R[i] = r

graph = [[] for _ in range(N + 1)]
for _ in range(K):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

INF = 10**15
dp = [INF] * (N + 1)
dp[1] = 0

from collections import deque

for current in range(1, N + 1):
    if dp[current] == INF:
        continue
    # BFS from current up to R[current] roads
    dist = [-1] * (N + 1)
    dist[current] = 0
    queue = deque()
    queue.append(current)
    while queue:
        v = queue.popleft()
        if dist[v] == R[current]:
            continue
        for nv in graph[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                queue.append(nv)
    for town in range(1, N + 1):
        if dist[town] != -1 and dist[town] != 0:
            cost = dp[current] + C[current]
            if dp[town] > cost:
                dp[town] = cost

print(dp[N])