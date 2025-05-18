MOD = 10**9+7
n = int(input())
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
dp[0][0] = 1
for i in range(1, n+1):
	s = input()
	for j in range(n+1):
		if s == "U":
			if j > 0:
				dp[i][j] += dp[i-1][j-1]
			dp[i][j] += j * dp[i-1][j]
		elif s == "-":
			dp[i][j] += dp[i-1][j]
		else:
			if j < n:
				dp[i][j] += (j+1) * (j+1) * dp[i-1][j+1]
			dp[i][j] += j * dp[i-1][j]
		dp[i][j] %= MOD
print(dp[n][0])