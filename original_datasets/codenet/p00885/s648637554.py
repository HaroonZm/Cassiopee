INF = 10**9
while 1:
    n = input()
    if not n:
        break
    dp = [INF]*4
    dp[0] = 0
    pos = 0; time = 0
    k = -1
    ps = []; ts = []
    for i in xrange(n):
        p, t = map(int, raw_input().split())
        ps.append(p); ts.append(t)
    for i in xrange(n):
        p, t = ps[i], ts[i]
        d = abs(p - pos)
        can = False
        r = INF
        for j in xrange(3, -1, -1):
            if j<3:
                dp[j+1] = INF
            if dp[j] == INF:
                continue
            if j<3 and d*(j+1) <= t - time:
                can = True
                dp[j+1] = dp[j] + d
            if pos*(j+1) + p <= t - time:
                r = min(r, dp[j] + pos + p)
                can = True
        dp[1] = r
        dp[0] = INF
        if not can:
            k = i+1
            break
        pos, time = p, t
    if k!=-1:
        print "NG", k
        continue
    print "OK", (min(dp[1:]) + p)