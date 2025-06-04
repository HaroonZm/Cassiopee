from heapq import heappush, heappop
N, M, C = map(int, input().split())
G = [[] for i in range(N)]
E = []
for i in range(M):
    a, b, d = map(int, input().split()); a -= 1; b -= 1
    G[a].append((b, d))
    G[b].append((a, d))
    E.append((a, b, d))

INF = 10**18
dist = [INF]*N
dist[0] = 0
que = [(0, 0)]
while que:
    cost, v = heappop(que)
    if dist[v] < cost:
        continue
    for w, d in G[v]:
        if cost + d < dist[w]:
            dist[w] = cost + d
            heappush(que, (cost + d, w))

*I, = range(N)
I.sort(key = dist.__getitem__)
K = [0]*N
for i, e in enumerate(I):
    K[e] = i

Q = [0]*N
su = 0
for a, b, d in E:
    if K[a] < K[b]:
        Q[b] += d
    else:
        Q[a] += d
    su += d

ans = 10**18
cu = 0
for v in I:
    x = dist[v]
    cu += Q[v]
    ans = min(ans, C*x + (su - cu))
print(ans)