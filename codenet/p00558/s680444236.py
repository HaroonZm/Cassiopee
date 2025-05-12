from heapq import heappush, heappop
N, M, X = map(int, input().split())
T = [int(input()) for i in range(N)]
G = [[] for i in range(N)]
for i in range(M):
    A, B, D = map(int, input().split())
    G[A-1].append((B-1, D))
    G[B-1].append((A-1, D))
INF = 10**9
dist = [[INF]*(2*X+1) for i in range(N)]
dist[0][-X] = 0

que = [(0, 0, -X)]
while que:
    cost, u, t = heappop(que)
    if dist[u][t] < cost:
        continue
    for v, d in G[u]:
        t1 = max(0, t - d) if t > 0 else min(0, t + d)
        if (t1 < 0 and T[v] == 2) or (t1 > 0 and T[v] == 0):
            continue
        t1 = [-X, t1, X][T[v]]
        if cost + d < dist[v][t1]:
            dist[v][t1] = cost + d
            heappush(que, (cost + d, v, t1))
print(min(dist[N-1]))