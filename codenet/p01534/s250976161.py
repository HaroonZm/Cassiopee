INF = 10 ** 20
n, m = map(int, input().split())
dp = [[[-INF] * 9 for _ in range(m + 1)] for _ in range(n + 1)]
dp[0][m][0] = 0
for i in range(n):
  a, b, c = map(int, input().split())
  for rest in range(m + 1):
    for l1 in range(9):
      for l2 in range(min(9, rest + 1)):
        if l1 == 0 and l2 == 0:add = c
        elif l2 == 0:
          if b <= 0:add = max(b, c)
          else:add = max(b * l1, c)
        elif l1 == 0:
          if a <= 0:add = max(a, c)
          else:add = max(a * l2, c)
        else:
          if a <= 0 and b <= 0:add = max(a, b, c)
          elif a <= 0:add = max(b * l1, c)
          elif b <= 0:add = max(a * l2, c)
          elif a <= b:add = max(b * l1 + a * min(l2, 8 - l1), c)
          else:add = max(a * l2 + b * min(l1, 8 - l2), c)
        dp[i + 1][rest - l2][l2] = max(dp[i + 1][rest - l2][l2], dp[i][rest][l1] + add)

ans = -INF
for y in range(m + 1):
  for x in range(9):
    ans = max(ans, dp[n][y][x])
print(ans)