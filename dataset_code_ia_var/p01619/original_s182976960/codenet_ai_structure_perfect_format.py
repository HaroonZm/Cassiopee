import sys

M = 1000000
n, m = map(int, raw_input().split())
if m == 1:
    a = 1
    for i in range(n):
        a = (a * 2) % M
    print a
    sys.exit()
dp = [[0] * 3 for _ in range(n + 2)]
dp[0] = [1, 0, 0]
dp[1] = [1, 1, 1]
for i in range(1, n + 2):
    dp[i][1] = sum(dp[i - 1]) % M
    dp[i][0] = (sum(dp[i - 1]) + sum([dp[j][2] for j in range(i - 1)])) % M
    dp[i][2] = (sum(dp[i - 1]) + sum([dp[j][0] for j in range(i - 1)])) % M
print dp[n + 1][2]