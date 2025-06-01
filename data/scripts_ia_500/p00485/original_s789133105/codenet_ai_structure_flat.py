import sys
from heapq import heappush, heappop
from itertools import combinations

n, m, k = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    f, t, c = map(int, input().split())
    adj[f].append((t, c))
    adj[t].append((f, c))

malls = [int(input()) for _ in range(k)]
for f, t in combinations(malls, 2):
    adj[f].append((t, 0))
    adj[t].append((f, 0))

WHITE, GRAY, BLACK = 0, 1, 2
color = [WHITE] * (n+1)
d = [float('inf')] * (n+1)
s = malls[0]
d[s] = 0
pq = []
heappush(pq, (0, s))
while pq:
    cost, u = heappop(pq)
    color[u] = BLACK
    if d[u] < cost:
        continue
    for v, cc in adj[u]:
        if color[v] == BLACK:
            continue
        if d[v] > d[u] + cc:
            d[v] = d[u] + cc
            heappush(pq, (d[v], v))
            color[v] = GRAY

ans = []
for n_ in range(1, n+1):
    tmp = []
    for j in adj[n_]:
        tmp.append((d[n_] + j[1] + d[j[0]]) / 2)
    if tmp:
        ans.append(max(tmp))
print(int(max(ans) + 0.5))