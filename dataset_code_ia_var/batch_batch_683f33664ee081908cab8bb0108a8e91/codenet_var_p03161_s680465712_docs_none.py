import numpy as np

n, k = list(map(int, input().split()))
h = np.array(list(map(int, input().split())))
dp = np.zeros(n)

for i in range(1, n):
    s = min(k, i)
    dp[i] = np.min(dp[i-s:i] + np.abs(h[i] - h[i-s:i]))

print(int(dp[-1]))