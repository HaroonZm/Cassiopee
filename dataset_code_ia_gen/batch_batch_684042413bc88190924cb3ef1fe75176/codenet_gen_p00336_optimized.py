t=input()
b=input()
mod=10**9+7
dp=[0]*(len(b)+1)
dp[0]=1
for c in t:
 for i in range(len(b)-1,-1,-1):
  if c==b[i]:
   dp[i+1]=(dp[i+1]+dp[i])%mod
print(dp[len(b)]%mod)