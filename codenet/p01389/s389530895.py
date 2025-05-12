h, w = map(int, input().split())
INF = 10 ** 20
dp = [[INF] * (w + 1)] + [[INF] + [0] * w for _ in range(h)]
dp[0][1] = 0
for y in range(1, h + 1):
  line = list(map(int, list(input())))
  for x in range(1, w + 1):
    dp[y][x] = min(dp[y - 1][x], dp[y][x - 1]) + line[x - 1]
print(dp[h][w])