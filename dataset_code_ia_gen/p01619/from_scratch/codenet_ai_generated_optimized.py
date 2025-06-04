N,M=map(int,input().split())
MOD=10**6
if M==1:
 dp=[0]*(N+2)
 dp[1]=2
 dp[2]=4
 for i in range(3,N+1):
  dp[i]=(dp[i-1]+dp[i-2]+dp[i-2])%MOD
 print(dp[N]%MOD)
else:
 dp=[0]*(N+2)
 dp[1]=4
 dp[2]=12
 for i in range(3,N+1):
  dp[i]=(dp[i-1]+dp[i-1]+dp[i-2]+dp[i-2]+dp[i-2])%MOD
 print(dp[N]%MOD)