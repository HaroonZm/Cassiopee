import sys
import heapq

input = sys.stdin.readline

N, M, X = map(int, input().split())
H = [0] + [int(input()) for _ in range(N)]

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, T = map(int, input().split())
    graph[A].append((B, T))
    graph[B].append((A, T))

# dist[node] = minimal time to reach the top of node (height H[node])
dist = [float('inf')] * (N + 1)
# initialize dist to climb from X to H[1] on tree 1
dist[1] = abs(H[1] - X)

hq = [(dist[1], 1)]
while hq:
    time, node = heapq.heappop(hq)
    if dist[node] < time:
        continue
    if node == N:
        print(time)
        break
    for nxt, t in graph[node]:
        # after jump, height = current height - t
        h_after_jump = H[node] - t
        # jump possible if 0 <= h_after_jump <= H[nxt]
        if 0 <= h_after_jump <= H[nxt]:
            # cost to climb from h_after_jump to H[nxt]
            cost = time + t + (H[nxt] - h_after_jump)
            if cost < dist[nxt]:
                dist[nxt] = cost
                heapq.heappush(hq, (cost, nxt))
else:
    print(-1)