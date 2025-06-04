MOD = 10**9 + 7

n, k = map(int, input().split())

# dp[i][j] = number of ways to put i indistinguishable balls into j indistinguishable boxes
# with boxes allowed to be empty.
# This corresponds to the number of integer partitions of i into at most j parts.
# It can be computed using the recurrence:
# dp[i][j] = dp[i][j-1] + dp[i-j][j] if i >= j else dp[i][j-1]

dp = [[0]*(k+1) for _ in range(n+1)]
dp[0][0] = 1

for i in range(n+1):
    for j in range(1, k+1):
        dp[i][j] = dp[i][j-1]
        if i - j >= 0:
            dp[i][j] = (dp[i][j] + dp[i-j][j]) % MOD

print(dp[n][k] % MOD)