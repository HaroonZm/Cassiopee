from collections import deque
from heapq import heappush, heappop
N, M, K, S = map(int, input().split())
P, Q = map(int, input().split())
C = [int(input())-1 for _ in range(K)]
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
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
        if D[w] == N:
            D[w] = d+1
            que.append(w)

INF = 10**18
dist = [INF]*N
dist[0] = 0
que = [(0, 0)]
cnt = 0
while que:
    cost, v = heappop(que)
    if dist[v] < cost:
        continue
    cnt += 1
    for w in G[v]:
        if D[w] == 0:
            continue
        nd = Q if D[w] <= S else P
        ncost = cost + nd
        if ncost < dist[w]:
            dist[w] = ncost
            heappush(que, (ncost, w))
print(dist[-1] - (Q if D[-1] <= S else P))