def get_pro(w, v):
  """
  dp[a][b] ... a番目、金額bまでで作れる最高の利益
  dp[a][b] = max(dp[a - 1][b], dp[a - 1][b - w * k] + v * k)
  """
  dp = [0] * (x + 1)
  for a in range(n):
    wa = wlst[a]
    va = vlst[a]
    for b in range(wa, x + 1):
      dp[b] = max(dp[b], dp[b - wa] + va)
  return dp[x]

n, d, x = map(int, input().split())
plst = [list(map(int, input().split())) for _ in range(d)]
for i in range(d - 1):
  vlst = [plst[i + 1][j] - plst[i][j] for j in range(n)]
  wlst = [plst[i][j] for j in range(n)]
  x += get_pro(wlst, vlst)
print(x)