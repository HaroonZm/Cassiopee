def submit():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    modp = 10 ** 9 + 7
    dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(n):
        for j in range(1, k + 1):
            if j - 1 - a[i] >= 0:
                dp[i + 1][j] = dp[i][j] + dp[i + 1][j - 1] - dp[i][j - 1 - a[i]]
            else:
                dp[i + 1][j] = dp[i][j] + dp[i + 1][j - 1]
            dp[i + 1][j] %= modp
    print(dp[n][k])

submit()