while 1:
    N,T,L,B = map(int, raw_input().split())
    if N == 0:
        break
    lose = []
    for _ in xrange(L):
        lose.append(int(raw_input()))
    back = []
    for _ in xrange(B):
        back.append(int(raw_input()))
    dp = []
    for _ in range(T+2):
        dp.append([0.0]*(N+1))
    dp[0][0] = 1.0
    p = 1.0/6.0
    for t in xrange(T):
        for i in xrange(N):
            if i in lose:
                tt = t-1
            else:
                tt = t
            for k in range(1, 7):
                j = i + k
                if j > N:
                    j = N - j % N
                if j in back:
                    dp[t+1][0] += p * dp[tt][i]
                else:
                    dp[t+1][j] += p * dp[tt][i]
        dp[t+1][N] += dp[t][N]
    print "%.6f" % dp[T][N]