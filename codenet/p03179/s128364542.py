import numpy as np
from itertools import accumulate
MOD = 10**9+7
n = int(input())
S = input()
dp = np.ones(n, dtype=np.int64)
for s in S:
  if s == "<":
    dp = np.cumsum(dp[::-1][:-1])[::-1]%MOD
  else:
    dp = np.cumsum(dp[:-1])%MOD
ans = dp[0]
print(ans)