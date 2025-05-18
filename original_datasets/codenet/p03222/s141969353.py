H,W,K = [int(x) for x in input().split()]
dp=[[0]*W for _ in range(H+1)]
dp[0][0]=1
for i in range(H):
  for j in range(W):
    for bit in range(1<<(W-1)):
      flag = 1
      for k in range(W-2):
        if (bit&1<<k) and (bit&1<<k+1):
          flag = 0
      if flag!=1:
        continue
      nj = j
      if (bit&1<<j):
        nj = 1+j
      if j>0 and (bit&1<<(j-1)):
        nj = j-1
      dp[i+1][nj] +=dp[i][j]
      dp[i+1][nj] %=(10**9+7)
print(dp[H][K-1])