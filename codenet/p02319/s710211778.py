N, W = map(int, input().split())
I = [list(map(int, input().split())) for _ in range(N)]
MAX_V = sum(v for v, _ in I)

dp = [W+1] * (MAX_V + 1)
dp[0] = 0
for v, w in I:
    for j in range(MAX_V, v-1, -1):
        dp[j] = min(dp[j-v] + w, dp[j])
        
for i in range(MAX_V, -1, -1):
  if dp[i] <= W:
    print(i)
    break