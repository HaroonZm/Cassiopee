n = int(input())
nums = list(map(int, input().split()))
dp = []
for i in range(n - 1):
    row = []
    for j in range(21):
        row.append(0)
    dp.append(row)

dp[0][nums[0]] = 1

for i in range(n - 2):
    for j in range(21):
        if dp[i][j] > 0:
            if j + nums[i + 1] <= 20:
                dp[i + 1][j + nums[i + 1]] += dp[i][j]
            if j - nums[i + 1] >= 0:
                dp[i + 1][j - nums[i + 1]] += dp[i][j]

print(dp[n - 2][nums[n - 1]])