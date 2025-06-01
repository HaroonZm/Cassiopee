import heapq
from sys import stdin

input = stdin.readline

N, M, X = map(int, input().split())
H = [0, *map(int, (input() for _ in range(N)))]

adj_list = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, c = map(int, input().split())
    if H[u] >= c:
        adj_list[u].append((v, c))
    if H[v] >= c:
        adj_list[v].append((u, c))

INF = float('inf')
costs = [INF] * (N+1)
costs[1] = 0

# heap elements: (cost, node, current_height)
heap = [(0, 1, X)]

while heap:
    cost, node, h = heapq.heappop(heap)
    if cost > costs[node]:
        continue
    if node == N:
        last_position = h
        break

    for nei, nc in adj_list[node]:
        diff = h - nc
        if diff < 0:
            climb_up = -diff
            if climb_up > H[node]:
                continue
            next_cost = cost + climb_up + nc
            next_h = 0
        elif diff > H[nei]:
            climb_down = diff - H[nei]
            if climb_down < 0:
                continue
            next_cost = cost + climb_down + nc
            next_h = H[nei]
        else:
            next_cost = cost + nc
            next_h = diff

        if next_cost < costs[nei]:
            costs[nei] = next_cost
            heapq.heappush(heap, (next_cost, nei, next_h))
else:
    print(-1)
    exit()

print(costs[N] + H[N] - last_position)