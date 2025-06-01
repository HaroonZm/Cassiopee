from heapq import heappush, heappop
from sys import stdin
input = stdin.readline

N, M, X = map(int, input().split())
T = list(map(int, (input() for _ in range(N))))
G = [[] for _ in range(N)]
for _ in range(M):
    A, B, D = map(int, input().split())
    G[A-1].append((B-1, D))
    G[B-1].append((A-1, D))

INF = 10**9
offset = X
dist = [[INF] * (2 * X + 1) for _ in range(N)]
dist[0][offset] = 0

heap = [(0, 0, offset)]
while heap:
    cost, u, t = heappop(heap)
    if cost > dist[u][t]:
        continue
    for v, d in G[u]:
        # Calculate new time index with sign logic
        delta = -d if t > offset else d
        t1 = t + delta
        # Clamp t1 within [0, 2*X]
        t1 = max(0, min(2 * X, t1))
        sign = (t1 - offset) > 0 # True if positive time
        if (sign and T[v] == 0) or (not sign and T[v] == 2):
            continue
        # Override t1 depending on T[v]
        t1 = [0, offset, 2 * X][T[v]]
        if cost + d < dist[v][t1]:
            dist[v][t1] = cost + d
            heappush(heap, (cost + d, v, t1))

print(min(dist[-1]))