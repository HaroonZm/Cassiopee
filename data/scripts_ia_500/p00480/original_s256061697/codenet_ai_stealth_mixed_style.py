n = int(input())
nums = list(map(int, input().split()))

dp = []
for _ in range(n-1):
    dp.append([0]*21)
dp[0][nums[0]] = 1

i = 0
while i < n-2:
    for j in range(21):
        val = nums[i+1]
        if j + val <= 20:
            dp[i+1][j+val] = dp[i+1][j+val] + dp[i][j]
        if j - val >= 0:
            dp[i+1][j-val] += dp[i][j]
    i += 1

print(dp[-1][nums[-1]])