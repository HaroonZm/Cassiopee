n = int(input())
c = [input() for i in range(n)]
MOD = 10 ** 9 + 7

dp = [[0] * (n + 1) for i in range(n + 1)]
dp[0][0] = 1

for i , char in enumerate(c):
    if char == "-":
        for j in range(n + 1):
            if j + 1 < n + 1:
                dp[i + 1][j + 1] += dp[i][j]
                dp[i + 1][j + 1] %= MOD

    if char == "U":
        for j in range(n + 1):
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= MOD
            if j + 1 < n + 1:
                dp[i + 1][j + 1] += dp[i][j] * (i - j)
                dp[i + 1][j + 1] %= MOD

    if char == "D":   
        for j in range(n + 1):
            if j + 1 < n + 1:
                dp[i + 1][j + 1] += dp[i][j] * (i - j)
                dp[i + 1][j + 1] %= MOD
            if j + 2 < n + 1:
                dp[i + 1][j + 2] += dp[i][j] * (i - j) ** 2
                dp[i + 1][j + 2] %= MOD

print(dp[-1][-1])