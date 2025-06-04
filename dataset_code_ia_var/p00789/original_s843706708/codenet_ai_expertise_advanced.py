from sys import stdin

from itertools import islice

dp = [1] + [0] * 300
squares = [c**2 for c in range(1, 18)]
for sq in squares:
    for i in range(300 - sq + 1):
        dp[i + sq] += dp[i]
for line in islice(stdin, None):
    n = int(line)
    if n == 0: break
    print(dp[n])