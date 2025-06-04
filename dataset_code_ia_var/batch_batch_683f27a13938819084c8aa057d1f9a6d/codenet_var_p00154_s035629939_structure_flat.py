import sys
from array import array

while True:
    m = input()
    if m == 0:
        sys.exit(0)
    dp = [array('I', [0] * 1001) for _ in range(m + 1)]
    dp[0][0] = 1
    for i in range(m):
        v, c = map(int, raw_input().split())
        for j in range(1001):
            for k in range(c + 1):
                next_value = j + v * k
                if next_value > 1000:
                    continue
                dp[i + 1][next_value] += dp[i][j]
    n = input()
    for _ in range(n):
        x = input()
        print dp[m][x]