import heapq
from collections import deque

N, M, X = map(int, input().split())
H = [0]
for i in range(N):
    H.append(int(input()))

adj_list = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, c = map(int, input().split())
    if H[u] >= c:
        adj_list[u].append((v, c))
    if H[v] >= c:
        adj_list[v].append((u, c))

INF = float('inf')
visited = [False] * (N + 1)
costs = [INF] * (N + 1)

q = [(0, 1, X)]
costs[1] = 0
last_position = 0

while q:
    cost, n, h = heapq.heappop(q)
    visited[n] = True
    if n == N:
        last_position = h
        break
    for nei, nc in adj_list[n]:
        if visited[nei]:
            continue
        if h - nc < 0:
            climbUp = (nc - h)
            if climbUp > H[n]:
                continue
            nextCost = cost + climbUp + nc
            nextH = 0
        elif h - nc > H[nei]:
            climbDown = (h - (H[nei] + nc))
            if climbDown < 0:
                continue
            nextCost = cost + climbDown + nc
            nextH = H[nei]
        else:
            nextCost = cost + nc
            nextH = h - nc
        if nextCost < costs[nei]:
            costs[nei] = nextCost
            heapq.heappush(q, (nextCost, nei, nextH))

if costs[N] == INF:
    print(-1)
else:
    print(costs[N] + H[N] - last_position)