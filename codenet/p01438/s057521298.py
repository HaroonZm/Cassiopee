from collections import defaultdict
while 1:
    n = int(raw_input())
    if n == 0: break
    L = [0]*n
    D = [0]*n
    for man in xrange(n):
        m,l = map(int,raw_input().split())
        L[man] = l
        t = 0
        for date in xrange(m):
            s,e = map(int,raw_input().split())
            for s in xrange(s-6,e-6):
                t |= 1 << s
        D[man] = t

    dp = [defaultdict(int) for i in xrange(n)]
    dp[0][D[0]] = L[0]
    for i in xrange(1,n):
        for bit in dp[i-1].keys():
            if bit&D[i] == 0:
                dp[i][bit|D[i]] = max(dp[i][bit|D[i]], dp[i-1][bit]+L[i])
            dp[i][bit] = max(dp[i][bit],dp[i-1][bit])
        dp[i][D[i]] = max(dp[i][D[i]], L[i])
        
    ans = max(max(dp[i].values()) for i in xrange(n))
    print ans