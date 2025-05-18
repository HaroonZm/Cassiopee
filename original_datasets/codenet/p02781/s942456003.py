def run():
  N = list(map(int, list(input())))
  K = int(input())
  Nlen = len(N)
  dp = [[[0]*(K+2) for _ in range(2)] for n in range(Nlen+1)]
  dp[0][0][0] = 1
  for nlen in range(Nlen):
    dN = N[nlen]
    for d in range(10):
      for j in range(2):
        for k in range(K+2):
          flagj = j or d < dN
          if (flagj == 0) and (d > dN): continue
          flagk = min(K+1, k+(d != 0))
          dp[nlen+1][flagj][flagk] += dp[nlen][j][k]
  print(dp[-1][0][K]+dp[-1][1][K])
  
if __name__ == '__main__':
    run()