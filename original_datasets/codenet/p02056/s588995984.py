import sys
from heapq import heappop as hpp, heappush as hp
def dijkstra(N, s, Edge):
    inf = 10**18
    dist = [inf] * N
    Q = [(0, s)]
    decided = set()
    for _ in range(N):
        while True:
            dn, vn = hpp(Q)
            if vn not in decided:
                decided.add(vn)
                dist[vn] = dn
                break
        for vf, df in Edge[vn]:
            if vf not in decided:
                hp(Q, (dn + df, vf))
    return dist

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

dist = dijkstra(N, 0, Edge1)

Edge2 = [[] for _ in range(3*N)]

for u, v, t in L:
    Edge2[u].append((v, t))
    Edge2[v].append((u, t))
    Edge2[N+u].append((N+v, t))
    Edge2[N+v].append((N+u, t))
inf = 10**17
for i in range(N):
    Edge2[i].append((N+i, inf - P[i]))
    Edge2[N+i].append((2*N+i, inf - J[i] + dist[i]))

dist2 = dijkstra(3*N, 0, Edge2)
Ans = [-10**20]*K
for i in range(N):
    Ans[C[i]-1] = max(Ans[C[i]-1], 2*inf - dist2[2*N+i])
for a in Ans:
    print(a)