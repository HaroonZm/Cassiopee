while True:
    N = input()
    if N == 0:
        break
    data = [map(int,raw_input().split()) for _ in xrange(N)]
    data.sort(key = lambda x:-x[0])
    R,W = zip(*data)
    empty = max(0,R[0]-sum(R[1:]))
    #print "empty",empty
    dp = [False]*(empty+1)
    dp[0] = True
    ma = 0
    for w in W[-1:0:-1]:
        if empty < w:
            break
        for i in xrange(empty,-1,-1):
            if dp[i] and i+w <= empty:
                ma = max(ma, i+w)
                dp[i+w] = True
    #print filter(lambda x: dp[x], xrange(empty+1))
    print sum(R)+sum(W)+(empty-ma)