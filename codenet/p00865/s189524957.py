while 1:
    n,m,k = map(int,raw_input().split())
    if n == 0: break
    dp = [[0]*(m*n+1) for i in xrange(n)]
    dp[0][1:m+1] = [1]*m
    
    for i in xrange(1,n):
        for j in xrange(1,m*n+1):
            dp[i][j] = sum(dp[i-1][max(j-m,0):j])
    s = sum(dp[n-1])
    ans = 0
    for i in xrange(1,m*n+1):
        ans += 1.0*dp[n-1][i]/s * max(1,i-k)
    print "%.10f"%ans