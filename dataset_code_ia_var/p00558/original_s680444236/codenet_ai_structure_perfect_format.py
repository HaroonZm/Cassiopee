from heapq import heappush, heappop

N, M, X = map(int, input().split())
T = [int(input()) for _ in range(N)]
G = [[] for _ in range(N)]
for _ in range(M):
    A, B, D = map(int, input().split())
    G[A - 1].append((B - 1, D))
    G[B - 1].append((A - 1, D))

INF = 10 ** 9
dist = [[INF] * (2 * X + 1) for _ in range(N)]
dist[0][X] = 0

que = [(0, 0, 0)]
while que:
    cost, u, t = heappop(que)
    if dist[u][t + X] < cost:
        continue
    for v, d in G[u]:
        t1 = t
        if t > 0:
            t1 = max(0, t - d)
        else:
            t1 = min(0, t + d)
        if (t1 < 0 and T[v] == 2) or (t1 > 0 and T[v] == 0):
            continue
        t2 = 0
        if T[v] == 0:
            t2 = -X
        elif T[v] == 1:
            t2 = t1
        else:
            t2 = X
        if -X <= t2 <= X and cost + d < dist[v][t2 + X]:
            dist[v][t2 + X] = cost + d
            heappush(que, (cost + d, v, t2))
print(min(dist[N - 1]))