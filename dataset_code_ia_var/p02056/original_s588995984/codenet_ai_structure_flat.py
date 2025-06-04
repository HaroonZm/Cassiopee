import sys
from heapq import heappop, heappush

N, M ,K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))
J = list(map(int, input().split()))

Edge1 = [[] for _ in range(N)]
L = []
for _ in range(M):
    u, v, t = map(int, sys.stdin.readline().split())
    u -= 1
    v -= 1
    Edge1[u].append((v, t))
    Edge1[v].append((u, t))
    L.append((u, v, t))

inf = 10**18
dist = [inf] * N
Q = [(0, 0)]
decided = set()
for _ in range(N):
    while True:
        dn, vn = heappop(Q)
        if vn not in decided:
            decided.add(vn)
            dist[vn] = dn
            break
    for vf, df in Edge1[vn]:
        if vf not in decided:
            heappush(Q, (dn + df, vf))

Edge2 = [[] for _ in range(3*N)]
for u, v, t in L:
    Edge2[u].append((v, t))
    Edge2[v].append((u, t))
    Edge2[N+u].append((N+v, t))
    Edge2[N+v].append((N+u, t))
inf2 = 10**17
for i in range(N):
    Edge2[i].append((N+i, inf2 - P[i]))
    Edge2[N+i].append((2*N+i, inf2 - J[i] + dist[i]))

dist2 = [inf2 * 3] * (3*N)
Q2 = [(0, 0)]
decided2 = set()
for _ in range(3*N):
    while True:
        dn2, vn2 = heappop(Q2)
        if vn2 not in decided2:
            decided2.add(vn2)
            dist2[vn2] = dn2
            break
    for vf2, df2 in Edge2[vn2]:
        if vf2 not in decided2:
            heappush(Q2, (dn2 + df2, vf2))

Ans = [-10**20]*K
for i in range(N):
    Ans[C[i]-1] = max(Ans[C[i]-1], 2*inf2 - dist2[2*N+i])
for a in Ans:
    print(a)