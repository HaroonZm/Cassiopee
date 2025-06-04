n = int(input())
w = list(map(int, input().split()))
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i+1] = prefix[i] + w[i]

dp = [[0] * n for _ in range(n)]

for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length -1
        cost = prefix[j+1] - prefix[i]
        dp[i][j] = 10**15
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + cost)

print(dp[0][n-1])