DIV = 100000
while 1:
    n, m, s = map(int, raw_input().split())
    if n == 0: break
    dp = [[0]*(s+1) for i in range(n*n+1)]
    dp[0][0] = 1
    for i in range(1, n*n+1):
        for j in range(s+1):
            if j - i >= 0: dp[i][j] = (dp[i][j] + dp[i-1][j-i] + dp[i][j-i]) % DIV
            if j - m - 1 >= 0: dp[i][j] = (dp[i][j] - dp[i-1][j-m-1] + DIV) % DIV
    print dp[n*n][s]