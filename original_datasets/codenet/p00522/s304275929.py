INF = 10 ** 20

def main():
  m, n = map(int, input().split())
  manju_lst = [int(input()) for i in range(m)]
  manju_lst.sort(reverse=True)
  
  acc = 0
  cum_sum = [0]
  for manju in manju_lst:
    acc += manju
    cum_sum.append(acc)
  
  clst = []
  elst = []
  
  for i in range(n):
    c, e = map(int, input().split())
    clst.append(c)
    elst.append(e)
  
  dp = [[INF] * (m + 1) for _ in range(n + 1)]
  for i in range(n + 1):
    dp[i][0] = 0
  #dp[x][y]...x種類目までの箱でy個まで売る時の最小コスト
  #dp[x][y] = min(dp[x - 1][y], dp[x - 1][y - cx] + ex) if (y - cx >= 0) else min(dp[x - 1][y], (dp[x - 1][y + 1] if (y + 1 <= m) else ex))
  
  for x in range(1, n + 1):
    cx = clst[x - 1]
    ex = elst[x - 1]
    predp = dp[x - 1]
    for y in range(m, 0, -1):
      predp_y = predp[y]
  
      if y >= cx:
        comp = predp[y - cx] + ex
      elif y + 1 <= m:
        comp = dp[x][y + 1]
      else:
        comp = ex
  
      if predp_y <= comp:
        dp[x][y] = predp_y
      else:
        dp[x][y] = comp
  
  dpn = dp[n]
  print(max([cum_sum[x] - dpn[x] for x in range(m + 1)]))

main()