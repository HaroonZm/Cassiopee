N,M = map(int,input().split())
C = list(map(int,input().split()))
INF = float('inf')
dp = [INF] * (N+1)
dp[0] = 0
for i in range(M):
  c = C[i]
  for j in range(N+1):
    if j >= c:
      dp[j] = min(dp[j], dp[j-c]+1)

print(dp[N])