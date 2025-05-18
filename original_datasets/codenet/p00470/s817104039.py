while True:
    w, h = map(int, raw_input().split())
    if w | h == 0:
        break
    dp = [[[0] * (w + 1) for _ in xrange(h + 1)] for _ in xrange(4)]    
    #0:u -> u, 1: u -> r, 2: r -> u, 3: r -> r
    dp[0][1][0] = dp[3][0][1] = 1
    for y in xrange(h):
        for x in xrange(w):
            dp[0][y + 1][x] += dp[0][y][x] + dp[2][y][x]
            dp[1][y][x + 1] += dp[0][y][x]
            dp[2][y + 1][x] += dp[3][y][x]
            dp[3][y][x + 1] += dp[1][y][x] + dp[3][y][x]
    print sum(dp[i][h-1][w-1] for i in xrange(4)) % 100000