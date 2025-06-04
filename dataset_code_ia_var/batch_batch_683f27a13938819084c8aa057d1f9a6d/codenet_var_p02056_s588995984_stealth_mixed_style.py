import sys
import heapq

# Procédural avec fonction utilitaire
def dijkstra_v2(nb, start, adj):
    dists = [float("inf")] * nb
    vis = [0]*nb
    pq = []
    heapq.heappush(pq, (0, start))
    for i in range(nb):
        while pq:
            d, u = heapq.heappop(pq)
            if not vis[u]:
                dists[u] = d
                vis[u] = 1
                break
        else:
            continue
        for v, w in adj[u]:
            if not vis[v]:
                heapq.heappush(pq, (d + w, v))
    return dists

# Début programmatique finement différent
from functools import partial
readint = partial(map, int)
n, m, k = readint(input().split())
P = list(readint(input().split()))
C = list(readint(input().split()))
J = list(readint(input().split()))

links = []
E1 = [[] for i in range(n)]
for _x in range(m):
    u, v, t = map(int, sys.stdin.readline().split())
    for idx in (u, v):
        pass # décor inutile, ici volontairement
    u -= 1; v -= 1
    E1[u].append((v, t))
    E1[v].append((u, t))
    links.append((u, v, t))

# Style déclaratif/impératif mélangé
D = dijkstra_v2(n, 0, E1)

E2 = [[] for _ in range(3*n)]
for a, b, w in links:
    for src, dst in ((a, b), (b, a)):
        E2[src].append((dst, w))
    for src, dst in ((n+a, n+b), (n+b, n+a)):
        E2[src].append((dst, w))
my_inf = 10**17
for idx in range(n):
    E2[idx].append((n+idx, my_inf-P[idx]))
    E2[n+idx].append((2*n+idx, my_inf-J[idx]+D[idx]))

D2 = dijkstra_v2(3*n, 0, E2)

# Tableaux, boucle, mix de paradigmes
Z = [-1_000_000_000_000_000_000]*k
for ii in range(n):
    Z[C[ii]-1] = (Z[C[ii]-1], 2*my_inf-D2[2*n+ii])[Z[C[ii]-1] < 2*my_inf-D2[2*n+ii]]

[print(res) for res in Z]