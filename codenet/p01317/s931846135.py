from heapq import heappush, heappop
import sys, operator
INF = 10**18
def solve():
    readline = sys.stdin.readline
    write = sys.stdout.write
    N, M = map(int, readline().split())
    if N == M == 0:
        return False
    def dijkstra(N, s, G):
        dist = [INF]*N
        dist[s] = 0
        que = [(0, s)]
        while que:
            cost, v = heappop(que)
            if dist[v] < cost:
                continue
            for w, d in G[v]:
                if cost + d < dist[w]:
                    dist[w] = r = cost + d
                    heappush(que, (r, w))
        return dist
    rN = range(N)
    GL = [[] for i in rN]
    GS = [[] for i in rN]
    for i in range(M):
        x, y, t, sl = readline().split()
        x = int(x)-1; y = int(y)-1; t = int(t)
        if sl == 'L':
            GL[x].append((y, t))
            GL[y].append((x, t))
        else:
            GS[x].append((y, t))
            GS[y].append((x, t))
    EL = [dijkstra(N, i, GL) for i in rN]
    ES = [dijkstra(N, i, GS) for i in rN]

    R = int(readline())
    *Z, = map(int, readline().split())
    iv = [INF]*N
    S = [INF]*N; T = [0]*N
    D = [0]*N
    prv = Z[0]-1
    S[prv] = 0
    oadd = operator.add
    for z in Z[1:]:
        z -= 1
        A = EL[prv]; B = EL[z]
        v = A[z]
        D[:] = map(oadd, S, A)
        for j in rN:
            C = ES[j]
            b = B[j]
            T[j] = min(S[j] + v, min(map(oadd, D, C)) + b)
        S, T = T, S
        prv = z
    write("%d\n" % min(S))
    return True
while solve():
    ...