from heapq import heappush, heappop, heapify
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    N, M, K = map(int, readline().split())
    INF = 10**18
    E = [[-INF]*N for i in range(N)]
    for i in range(M):
        a, b, c = map(int, readline().split())
        E[a][b] = max(E[a][b], c)
    G = [[] for i in range(N)]
    for v in range(N):
        for w in range(N):
            if E[v][w] >= 0:
                G[v].append((w, E[v][w]))
    T = 100
    dist = [[0]*(T+1) for i in range(N)]
    prv = [[None]*(T+1) for i in range(N)]
    que = []
    for i in range(N):
        que.append((0, i, 0))
    t0 = T+1
    while que:
        cost, v, t = heappop(que)
        cost = -cost
        if cost >= K and t < t0:
            t0 = t
        if cost < dist[v][t] or t == T:
            continue
        for w, d in G[v]:
            if dist[w][t+1] < cost + d:
                dist[w][t+1] = cost + d
                prv[w][t+1] = v
                heappush(que, (-(cost + d), w, t+1))
    if t0 != T+1:
        v0 = 0; d = 0
        for v in range(N):
            e = dist[v][t0]
            if d < e:
                d = e
                v0 = v
        res = [v0]
        v = v0; t = t0
        while t > 0:
            v = prv[v][t]; t -= 1
            res.append(v)
        res.reverse()
        write("%d\n" % t0)
        write(" ".join(map(str, res)))
        write("\n")
        return

    for v in range(N):
        E[v][v] = 0
    E2 = [[-INF]*N for i in range(N)]
    A = (K-1).bit_length()
    RS = [E]
    for k in range(A):
        F = [[-INF]*N for i in range(N)]
        for v in range(N):
            for w in range(N):
                E2[w][v] = E[v][w]
        ok = 0
        for i in range(N):
            Ei = E[i]
            for j in range(N):
                Ej = E2[j]
                F[i][j] = r = max((a+b for a, b in zip(Ei, Ej) if a >= 0 and b >= 0), default = -INF)
                if r >= K:
                    ok = 1
        RS.append(F)
        E = F
        if ok:
            A = k
            break

    D = [0]*N
    ans = 0
    for i in range(A, -1, -1):
        E = RS[i]
        D0 = [0]*N
        ok = 0
        for v in range(N):
            D0[v] = r = max((a + e[v] for a, e in zip(D, E) if e[v]), default = -INF)
            if r >= K:
                ok = 1
        if not ok:
            ans += 1 << i
            D = D0
    ans += 1
    if ans > K:
        write("-1\n")
    else:
        write("%d\n" % ans)
solve()