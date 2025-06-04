mod = 1000000
n, m = map(int, input().split())
dp = [[0] * 5 for _ in range(n)]
dp[0] = [1, 1, 1, 1, 0]
a = 1
if m == 1:
    print((a << n) % mod)
else:
    for i in range(1, n):
        dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4]) % mod
        dp[i][1] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % mod
        dp[i][2] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3]) % mod
        dp[i][3] = (dp[i - 1][0] + dp[i - 1][3]) % mod
        dp[i][4] = (dp[i - 1][2] + dp[i - 1][4]) % mod
    print(sum(dp[n - 1][:4]) % mod)