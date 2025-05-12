n = int(input())
nums = [int(i) for i in input().split()]
dp = [[0 for j in range(21)] for i in range(n - 1)]

dp[0][nums[0]] = 1
for i in range(0, n - 2):
    for j in range(0, 21):
        if j + nums[i + 1] <= 20:
            dp[i + 1][j + nums[i + 1]] += dp[i][j]
        if j - nums[i + 1] >= 0:
            dp[i + 1][j - nums[i + 1]] += dp[i][j]

print(dp[n - 2][nums[n - 1]])