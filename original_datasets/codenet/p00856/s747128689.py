while 1:
    N,T,L,B = map(int,raw_input().split())
    if N == 0: break
    lose = [int(raw_input()) for i in xrange(L)]
    back = [int(raw_input()) for i in xrange(B)]

    dp = [[0.0]*(N+1) for i in xrange(T+2)]
    dp[0][0] = 1.0
    ans = 0.0
    p = 1.0/6.0
    for t in xrange(T):
        for i in xrange(N):
            tt = t-1 if i in lose else t
            for j in xrange(i+1,i+7):
                if j > N: j = N-j%N
                if j in back:
                    dp[t+1][0] += p*dp[tt][i]
                else:
                    dp[t+1][j] += p*dp[tt][i]
        dp[t+1][N] += dp[t][N]
    print "%.6f"%dp[T][N]