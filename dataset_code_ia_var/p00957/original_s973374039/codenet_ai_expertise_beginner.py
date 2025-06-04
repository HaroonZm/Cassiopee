import sys

l, k = map(int, sys.stdin.readline().split())
dp = []
for i in range(101):
    dp.append([0, 0])

dp[0][1] = 1
ans = 0

for i in range(1, l + 1):
    dp[i][0] = dp[i - 1][1]
    if i - k >= 0:
        dp[i][0] = dp[i][0] + dp[i - k][1]
    dp[i][1] = dp[i - 1][0]
    ans = ans + dp[i][0]

print(ans)