while 1:
    N = int(input())
    if N == 0:
        break
    P = [list(map(int, input().split())) for i in range(N)]
    M = 366
    E = [[] for i in range(M)]
    dp = [[0]*(M+1) for i in range(M+1)]
    for t, (i, j, w) in enumerate(P):
        E[i-1].append((t, j, w))
    for i in range(M):
        Ei = E[i]
        for j in range(i, M):
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i+1][j], dp[i][j+1])
        for j in range(M-1, i, -1):
            v = dp[i+1][j+1]
            for _, k, w in Ei:
                if k < j:
                    dp[k+1][j+1] = max(dp[k+1][j+1], v + w)
                else:
                    dp[j+1][k+1] = max(dp[j+1][k+1], v + w)
        v = dp[i+1][i+1]
        for t1, k1, w1 in Ei:
            dp[i+1][k1+1] = max(dp[i+1][k1+1], v + w1)
            for t2, k2, w2 in Ei:
                if t1 <= t2:
                    break
                if k1 < k2:
                    dp[k1+1][k2+1] = max(dp[k1+1][k2+1], v + w1 + w2)
                else:
                    dp[k2+1][k1+1] = max(dp[k2+1][k1+1], v + w1 + w2)
    print(max(max(dpi) for dpi in dp))