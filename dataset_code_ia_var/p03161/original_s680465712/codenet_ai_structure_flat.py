import numpy as np

n_k = input().split()
n = int(n_k[0])
k = int(n_k[1])
h_list = input().split()
h = np.array([int(x) for x in h_list])
dp = np.zeros(n)
i = 1
while i < n:
    s = k if k < i else i
    prev_range = dp[i-s:i]
    h_range = h[i-s:i]
    diffs = np.abs(h[i] - h_range)
    values = prev_range + diffs
    dp[i] = np.min(values)
    i += 1
print(int(dp[-1]))