import numpy as np
n, w = map(int, input().split())
v_max = 1000
num_v = v_max*n
INF = 10**9+1
dp = np.full(num_v+1, INF, dtype=int)
dp[0] = 0
for i in range(1,n+1):
  wn, vn = map(int, input().split())
  dp[vn:] = np.minimum(dp[vn:], dp[:-vn]+wn)
for i in range(len(dp)-1, -1, -1):
  if dp[i] <= w:
    print(i)
    break