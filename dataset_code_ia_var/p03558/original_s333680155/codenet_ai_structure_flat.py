import sys
sys.setrecursionlimit(2147483647)
INF = float("inf")
MOD = 10**9+7
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

k = int(input())
E = []
for i in range(k):
    tmp = []
    tmp.append(((i+1)%k, 1))
    tmp.append(((10*i)%k, 0))
    E.append(tmp)

dist = [INF]*k
dist[1] = 0
Q = deque()
Q.append(1)
while Q:
    v = Q.popleft()
    for nv, w in E[v]:
        if dist[nv] <= dist[v]+w:
            continue
        dist[nv] = dist[v]+w
        if w == 0:
            Q.appendleft(nv)
        else:
            Q.append(nv)
print(dist[0]+1)