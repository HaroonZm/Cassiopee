inf = 1 << 28
while 1:
    n = int(raw_input())
    if n == 0: break
    pt = [map(int,raw_input().split()) for i in xrange(n)]
    p = [0]+[ele[0] for ele in pt]
    t = [0]+[ele[1] for ele in pt]

    dp = [[inf]*4 for i in xrange(n+1)]
    dp[0][0] = 0
    
    for i in xrange(1,n+1):
        for j in xrange(1,4):
            if (j+1)*p[i-1]+p[i] <= t[i]-t[i-1]:
                dp[i][1] = min(dp[i][1], dp[i-1][j]+p[i-1]+p[i])
            if abs(p[i-1]-p[i])*j <= t[i]-t[i-1]:
                dp[i][j] = min(dp[i][j], dp[i-1][j-1]+abs(p[i-1]-p[i]))
        if min(dp[i]) == inf:
            print "NG",i
            break
    else:
        for j in xrange(1,4):
            dp[-1][j] += p[-1]
        print "OK",min(dp[n])