from collections import deque
from heapq import heappush, heappop
N, M, K, S = map(int, input().split())
P, Q = map(int, input().split())
C = [int(input())-1 for i in range(K)]
G = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split()); a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)

D = [N]*N
que = deque()
for c in C:
    D[c] = 0
    que.append(c)
while que:
    v = que.popleft()
    d = D[v]
    for w in G[v]:
        if D[w] != N:
            continue
        D[w] = d+1
        que.append(w)

INF = 10**18
dist = [INF]*N
dist[0] = 0
que = [(0, 0)]
while que:
    cost, v = heappop(que)
    if dist[v] < cost:
        continue
    c += 1
    for w in G[v]:
        if D[w] == 0:
            continue
        if D[w] <= S:
            if cost + Q < dist[w]:
                dist[w] = cost + Q
                heappush(que, (cost + Q, w))
        else:
            if cost + P < dist[w]:
                dist[w] = cost + P
                heappush(que, (cost + P, w))
print(dist[N-1] - (Q if D[N-1] <= S else P))