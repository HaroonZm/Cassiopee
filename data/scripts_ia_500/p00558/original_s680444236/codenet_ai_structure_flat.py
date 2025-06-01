from heapq import heappush, heappop
N, M, X = map(int, input().split())
T = []
for i in range(N):
    T.append(int(input()))
G = []
for i in range(N):
    G.append([])
for i in range(M):
    A, B, D = map(int, input().split())
    G[A-1].append((B-1, D))
    G[B-1].append((A-1, D))
INF = 10**9
dist = []
for i in range(N):
    dist.append([INF]*(2*X+1))
dist[0][-X] = 0
que = [(0, 0, -X)]
while len(que) > 0:
    elem = heappop(que)
    cost = elem[0]
    u = elem[1]
    t = elem[2]
    if dist[u][t] < cost:
        continue
    edges = G[u]
    for i in range(len(edges)):
        v = edges[i][0]
        d = edges[i][1]
        if t > 0:
            t1 = t - d
            if t1 < 0:
                t1 = 0
        else:
            t1 = t + d
            if t1 > 0:
                t1 = 0
        if (t1 < 0 and T[v] == 2) or (t1 > 0 and T[v] == 0):
            continue
        if T[v] == 0:
            t1 = -X
        elif T[v] == 1:
            t1 = t1
        else:
            t1 = X
        if cost + d < dist[v][t1]:
            dist[v][t1] = cost + d
            heappush(que, (cost + d, v, t1))
res = INF
for val in dist[N-1]:
    if val < res:
        res = val
print(res)