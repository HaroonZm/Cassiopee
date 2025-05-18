N, M = map(int, input().split())
keys = []
for _ in range(M):
  a, b = map(int, input().split())
  c = list(map(int, input().split()))
  s = 0
  for cc in c:
    cc -= 1
    s |= 1<<cc
  keys += [(s, a)]

dp = [float('inf')]*(1<<N)
dp[0] = 0
for s in range(1<<N):
  for i in range(M):
    t = s | keys[i][0]
    dp[t] = min(dp[t], keys[i][1]+dp[s])

if dp[-1] == float('inf'):
  print(-1)
else:
  print(dp[-1])