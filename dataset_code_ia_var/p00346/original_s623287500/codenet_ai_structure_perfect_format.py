from heapq import heappush, heappop
from collections import deque

n, r = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(r):
    s, t, d = map(int, input().split())
    G[s - 1].append((t - 1, d))
    G[t - 1].append((s - 1, d))

INF = 10 ** 18

def dijkstra(s):
    dist = [INF] * n
    dist[s] = 0
    que = [(0, s)]
    while que:
        cost, u = heappop(que)
        if dist[u] < cost:
            continue
        for v, w in G[u]:
            if cost + w < dist[v]:
                dist[v] = cost + w
                heappush(que, (cost + w, v))
    ma = max(dist)
    assert ma != INF
    goal = [i for i in range(n) if dist[i] == ma]
    used = set(goal)
    deq = deque(goal)
    while deq:
        u = deq.popleft()
        for v, w in G[u]:
            if dist[v] + w == dist[u] and v not in used:
                used.add(v)
                deq.append(v)
    return ma, used

A = [dijkstra(i) for i in range(n)]
B = max(ma for ma, _ in A)
ans = set(range(n))
for ma, used in A:
    if ma == B:
        ans -= used
print(len(ans))
for e in sorted(ans):
    print(e + 1)