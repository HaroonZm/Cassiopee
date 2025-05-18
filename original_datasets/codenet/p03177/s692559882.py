def power(x,n,mod):
  digit = len(str(bin(n)))-2
  a = len(x)
  dp = [x]*digit
  for i in range(1,digit):
    dp[i] = dot(dp[i-1],dp[i-1],mod)
  ans = [[0]*a for _ in range(a)]
  for i in range(a):
    ans[i][i] = 1
  for i in range(digit):
    if 1<<i & n:
      ans = dot(dp[i],ans,mod)
  return ans

def dot(A,B,mod):
  p = len(A)
  q = len(A[0])
  r = len(B)
  s = len(B[0])
  if q!=r:
    print('掛け算できません')
    return
  ans = [[0]*s for _ in range(p)]
  for i in range(p):
    for j in range(s):
      for k in range(q):
        ans[i][j] += A[i][k]*B[k][j]
        ans[i][j] %= mod
  return ans

def solve():
  N, K = map(int, input().split())
  mat = [list(map(int, input().split())) for _ in range(N)]
  init = [[0]*N for _ in range(N)]
  for i in range(N):
    init[i][i] = 1
  mod = 10**9+7
  dp = dot(init,power(mat,K,mod),mod)
  ans = sum(map(sum,dp))%mod
  return ans
print(solve())