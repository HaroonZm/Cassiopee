def main():
  MOD = 1000000007
  n, l = map(int, input().split())
  xlst = map(int, input().split())
  alst = map(int, input().split())
  can_use = []
  for x, a in zip(xlst, alst):
    if a == 0:s = {x}
    else:s = {k for k in range(x, l, a)}
    can_use.append(s)
  
  dp = [[0] * l for _ in range(n)]
  for j in range(l):
    dp[0][j] = dp[0][j - 1] + int(j in can_use[0])
  
  for i in range(1, n):
    acc = 0
    dpi = dp[i]
    dpi1 = dp[i - 1]
    st = can_use[i]
    for j in range(1, l):
      if j in st:acc = (acc + dpi1[j - 1]) % MOD
      dpi[j] = acc
  print(dp[n - 1][l - 1])

main()