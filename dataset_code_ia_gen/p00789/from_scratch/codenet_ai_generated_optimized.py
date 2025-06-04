coins = [i*i for i in range(1,18)]
max_amount = 300
dp = [0]*(max_amount+1)
dp[0] = 1
for c in coins:
    for i in range(c, max_amount+1):
        dp[i] += dp[i-c]
import sys
for line in sys.stdin:
    n = int(line)
    if n == 0:
        break
    print(dp[n])