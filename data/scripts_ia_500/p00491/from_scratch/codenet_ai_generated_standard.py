N,K=map(int,input().split())
fixed=[0]*(N+1)
for _ in range(K):
 A,B=map(int,input().split())
 fixed[A]=B
MOD=10000
dp=[[[0]*4 for _ in range(3)] for _ in range(N+1)]
# dp[day][consecutive_count-1][last_pasta]=ways
for pasta in range(1,4):
 if fixed[1] and fixed[1]!=pasta:
  continue
 dp[1][0][pasta]=1
for day in range(2,N+1):
 for cnt in range(3):
  for last in range(1,4):
   if dp[day-1][cnt][last]==0:
    continue
   for curr in range(1,4):
    if fixed[day] and fixed[day]!=curr:
     continue
    if curr==last:
     if cnt==2:
      continue
     dp[day][cnt+1][curr]=(dp[day][cnt+1][curr]+dp[day-1][cnt][last])%MOD
    else:
     dp[day][0][curr]=(dp[day][0][curr]+dp[day-1][cnt][last])%MOD
ans=sum(dp[N][cnt][p] for cnt in range(3) for p in range(1,4))%MOD
print(ans)