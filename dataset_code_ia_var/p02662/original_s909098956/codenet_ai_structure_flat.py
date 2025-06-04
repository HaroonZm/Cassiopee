import numpy as np
import sys
input = sys.stdin.readline

n_s = input().split()
n = int(n_s[0])
s = int(n_s[1])
A = np.array([int(i) for i in input().split()])

MOD = 998244353

dp = np.zeros(s + 1, dtype="int32")
dp[0] = 1

i = 0
while i < n:
    a = A[i]
    p = (dp * 2) % MOD
    p %= MOD
    if a <= s:
        p[a:] += dp[:-a]
    dp = p % MOD
    i += 1

print(dp[s])