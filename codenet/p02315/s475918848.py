N, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(W + 1)]

for a in A:
  for j in range(W, a[1] - 1, -1):
    dp[j] = max(dp[j], dp[j - a[1]] + a[0])
print(max(dp))