n = int(input())
s = [input() for i in range(n)]
s = "".join(s).replace("-","")
n = len(s)
mod = 10**9+7
dp = [[0 for i in range(n+1)] for j in range(n+1)]
dp[0][0] = 1
for i in range(n):
  si = s[i]
  if si == "D":
    for j in range(1,n+1):
      dp[i+1][j] = (dp[i+1][j]+dp[i][j]*j)%mod
      dp[i+1][j-1] = (dp[i+1][j-1]+dp[i][j]*j**2)%mod
  else:
    for j in range(n):
      dp[i+1][j+1] = (dp[i+1][j+1]+dp[i][j])%mod
      dp[i+1][j] = (dp[i+1][j]+dp[i][j]*j)%mod
print(dp[n][0])