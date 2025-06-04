import sys
import math

# 計算用のメモ化リスト
dp = [0] * 31
dp[0] = 1
for i in range(1, 31):
    dp[i] = dp[i-1]
    if i-2 >= 0:
        dp[i] += dp[i-2]
    if i-3 >= 0:
        dp[i] += dp[i-3]

for line in sys.stdin:
    n = int(line.strip())
    if n == 0:
        break
    total_ways = dp[n]
    days = math.ceil(total_ways / 10)
    years = (days + 364) // 365
    print(years)