MOD = 100000
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    dp = [[[0,0] for _ in range(h)] for _ in range(w)]
    dp[0][0] = [1,1]
    for i in range(w):
        for j in range(h):
            if i == 0 and j == 0:
                continue
            # From west (move east): allowed if previously moved north or start
            if i > 0:
                dp[i][j][0] = (dp[i-1][j][0] + dp[i-1][j][1]) % MOD
            # From south (move north): only if previous move was east
            if j > 0:
                dp[i][j][1] = dp[i][j-1][0] % MOD
    print((dp[w-1][h-1][0] + dp[w-1][h-1][1]) % MOD)