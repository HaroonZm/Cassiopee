import sys

dp = [[0]*37 for _ in range(5)]
dp[0][0] = 1
for i in range(1,5):
    for s in range(37):
        for k in range(10):
            if s - k >= 0:
                dp[i][s] += dp[i-1][s-k]

for line in sys.stdin:
    n = int(line)
    print(dp[4][n] if n <= 36 else 0)