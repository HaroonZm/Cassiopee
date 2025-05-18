def main():
  n, t, s = map(int, input().split())
  A = []
  B = []
  for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
  
  """
  dp[x + 1][y] ... 店xまででで時刻yまでの最大値
  dp[x + 1][y] = max(dp[x][y], dp[x + 1][y - 1], dp[x][y - B[x]] + A[x]) (not y - B[x] < s < y)
  dp[x + 1][y] = max(dp[x][y], dp[x + 1][y - 1])
  """

  dp = [[0] * (t + 1) for _ in range(n + 1)]
  for x in range(n):
    bx = B[x]
    ax = A[x]
    dpx = dp[x]
    dpx1 = dp[x + 1]
    for y in range(1, t + 1):
      if 0 <= y - bx and (not (y - bx < s < y)):
        dpx1[y] = max(dpx[y], dpx1[y - 1], dpx[y - bx] + ax)
      else:
        dpx1[y] = max(dpx[y], dpx1[y - 1])
   
  print(dp[n][t])
 
main()