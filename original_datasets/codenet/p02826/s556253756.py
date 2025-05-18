import numpy as np 
n,m=map(int, input().split())
coef = np.minimum(np.arange(n,1,-1),np.arange(1,n))
dp = np.zeros(n, dtype=np.int64)
dp[0] = 1
for c in coef:
    ndp = dp.copy()
    for i in range(c, n, c):
        ndp[i:] += dp[:n-i]
    dp = ndp % m #更新する

print((dp*np.arange(n, 0, -1) % m).sum() % m)