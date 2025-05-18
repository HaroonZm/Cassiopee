import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    N, M, K = map(int, readline().split())
    G = [[] for i in range(N)]
    INF = 10**18
    for i in range(M):
        a, b, c = map(int, readline().split())
        if c == 0:
            c = -INF
        G[a-1].append((b-1, c))
        G[b-1].append((a-1, c))
    def calc(K, U, l):
        if not l:
            X = [-INF]*(K+1)
            S0 = [-INF]*(K+1)
            S1 = [-INF]*(K+1)
            S0[0] = S1[1] = 0
            for i in range(1, K):
                e = U[i]
                for j in range(K-1, -1, -1):
                    S1[j+1] = max(S0[j], S1[j] + e)
                    S0[j] = max(S0[j], S1[j])
            for i in range(K+1):
                X[i] = max(S0[i], S1[i])
        else:
            X = calc(K-1, U[1:], 0) + [-INF]
            S0 = [-INF]*K
            S1 = [-INF]*K
            S0[0] = 0; S1[1] = U[1]
            for i in range(2, K):
                e = U[i]
                for j in range(K-2, -1, -1):
                    S1[j+1] = max(S0[j], S1[j] + e)
                    S0[j] = max(S0[j], S1[j])
            e = U[0]
            for i in range(K):
                X[i+1] = max(X[i+1], S0[i], S1[i] + e)
        return X
    used = [0]*N
    sg = 0
    dp = [-INF]*(N+1)
    dp[0] = 0
    for i in range(N):
        if used[i]:
            continue
        if len(G[i]) == 0:
            used[i] = 1
            for i in range(N-1, -1, -1):
                dp[i+1] = max(dp[i+1], dp[i])
            continue
        if len(G[i]) == 1:
            used[i] = 2
            v, c = G[i][0]
            r = [i]
            u = [0, c]
            while len(G[v]) == 2:
                r.append(v)
                used[v] = 2
                w1, w2 = G[v]
                if used[w1[0]]:
                    v, c = w2
                    u.append(c)
                else:
                    v, c = w1
                    u.append(c)
            r.append(v)
            used[v] = 2
            L = len(r)
            s = calc(L, u, 0)
            for i in range(N-L, -1, -1):
                for j in range(1, L+1):
                    dp[i+j] = max(dp[i+j], dp[i] + s[j])
    for i in range(N):
        if used[i]:
            continue
        r = []
        u = []
        v = i
        while 1:
            r.append(v)
            used[v] = 3
            w1, w2 = G[v]
            if used[w1[0]] and used[w2[0]]:
                break
            if used[w1[0]]:
                v, c = w2
                u.append(c)
            else:
                v, c = w1
                u.append(c)
        if G[i][0][0] == r[-1]:
            c = G[i][0][1]
        else:
            c = G[i][1][1]
        u = [c] + u
        L = len(r)
        s = calc(L, u, 1)
        for i in range(N-L, -1, -1):
            for j in range(1, L+1):
                dp[i+j] = max(dp[i+j], dp[i] + s[j])
    if dp[K] < -10**9:
        write("Impossible\n")
    else:
        write("%d\n" % dp[K])
solve()