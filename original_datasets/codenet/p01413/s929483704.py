import sys
readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    N, M, W, T = map(int, readline().split())
    cur = 0
    n_map = {}
    ws = [0]*M; P = [0]*M
    for i in range(M):
        s, v, p = readline().split()
        n_map[s] = i
        ws[i] = int(v)
        P[i] = int(p)

    ts = [[] for i in range(N)]
    X = [0]*N; Y = [0]*N
    for i in range(N):
        l, x, y = map(int, readline().split())
        X[i] = x; Y[i] = y
        r = 0
        t = ts[i]
        for j in range(l):
            r, q = readline().split(); q = int(q)
            k = n_map[r]
            if P[k] <= q:
                continue
            t.append((k, P[k] - q))

    E = [[0]*N for i in range(N)]
    E1 = [0]*N
    for i in range(N):
        for j in range(i):
            E[i][j] = E[j][i] = abs(X[i] - X[j]) + abs(Y[i] - Y[j])
        E1[i] = abs(X[i]) + abs(Y[i])
    INF = 10**18
    SN = 1 << N
    D0 = [[0]*N for i in range(SN)]

    dp1 = [0]*(T+1)
    for s in range(1, SN):
        d1 = INF
        for i in range(N):
            bi = (1 << i)
            r = INF
            if s & bi:
                si = s ^ bi
                if si == 0:
                    r = E1[i]
                else:
                    for j in range(N):
                        if i == j or s & (1 << j) == 0:
                            continue
                        r = min(r, D0[si][j] + E[j][i])
            D0[s][i] = r
            d1 = min(d1, r + E1[i])

        vs = [-1]*M
        for i in range(N):
            if s & (1 << i):
                for k, d in ts[i]:
                    vs[k] = max(vs[k], d)
        dp0 = [0]*(W+1)
        for i in range(M):
            if vs[i] == -1:
                continue
            w = ws[i]; v = vs[i]
            for j in range(W-w+1):
                dp0[j + w] = max(dp0[j] + v, dp0[j + w])
        v1 = max(dp0)

        for j in range(T-d1+1):
            dp1[j + d1] = max(dp1[j] + v1, dp1[j + d1])
    write("%d\n" % max(dp1))
solve()