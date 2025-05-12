m = 998244353
S = map(int, raw_input())
N = len(S)
pr = [0]*(N*2)
pb = [0]*(N*2)
pr[0] = 2-S[0]
pb[0] = S[0]
for i in xrange(1, N):
  pr[i] = pr[i-1]+(2-S[i])
  pb[i] = pb[i-1]+S[i]
for i in xrange(N, N*2):
  pr[i] = pr[i-1]
  pb[i] = pb[i-1]
dp = []
for i in xrange(N*2+1):
  dp.append([0]*(N*2+1))
dp[0][0]=1
for i in xrange(1, N*2+1):
  si = 0
  for b in xrange(i+1):
    r = i-b
    if pr[i-1]<r or pb[i-1]<b:
      continue
    if r>0:
      dp[r][b] = (dp[r][b]+dp[r-1][b]) % m
    if b>0:
      dp[r][b] = (dp[r][b]+dp[r][b-1]) % m
    si = (si+dp[r][b]) % m
print si