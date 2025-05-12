def d_init(n):
  c = 0
  A = D.items()[:]
  for i, e in A:
    c += 1
    for j, f in A[c:]:
      a = abs(e-f)
      D[(i, j)] = a
      D[(j, i)] = a
  return

def solve(p, v, w):
  if v == (1<<n)-1: return 0, N[p]
  a, b = dp[p][v]
  if a >= 0: return a, b

  T = 1e10
  for i in range(n):
    i1 = 1<<i
    if (v & i1) == 0:
      a, b = solve(i, v|i1, w + W[i])
      a += D[(i, p)] * w
      if T > a:
        T = a
        R = b
  R = N[p] + R
  dp[p][v] = [T, R]
  return T, R

N = {}
D = {}
W = {}
n = input()
dp = [[[-1, []] for _ in [0]*(1<<n)] for _ in [0]*n]
for i in range(n):
  a, b, c = map(int, raw_input().split())
  N[i] = [a]
  D[i] = b/2000.0
  W[i] = c*20
d_init(n)

minT = 1e10
R = []
for i, e in W.items():
  a, b = solve(i, 1<<i, e+70.0)
  if minT > a:
    minT = a
    R = b

for e in R:
  print str(e),