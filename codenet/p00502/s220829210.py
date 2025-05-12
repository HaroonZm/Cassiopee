def run():
  D, N = map(int, input().split())
  d_li = [int(input()) for d in range(D)]
  clothe_li = [list(map(int, input().split())) for n in range(N)]
  dp = [[0]*N for d in range(D)]
  #init
  d = d_li[0]
  for n, (a, b, c) in enumerate(clothe_li):
    if (a <= d) and (d <= b):
      dp[0][n] = 1
  #loop
  for i in range(1, D):
    d = d_li[i]
    #print(dp)
    for pre_n in range(N):
      if dp[i-1][pre_n] == 0: continue
      for n, (a, b, c) in enumerate(clothe_li):
        if (a <= d) and (d <= b):
          #print(c)
          dp[i][n] = max(dp[i][n], 
                         dp[i-1][pre_n] + abs(clothe_li[pre_n][2] - c))
  print(max(dp[-1])-1) 
    
if __name__ == '__main__':
  run()