def d_init(n):
  c = 0
  A = D.items()[:]
  for i, e in A:
    c += 1
    for j, f in A[c:]:
      tmp = abs(e-f)
      D[(i, j)] = tmp
      D[(j, i)] = tmp
  return

def solve(idx, visited, weight):
  if visited == (1<<n)-1: return 0, name[idx]
  tmp1, tmp2 = dp[idx][visited]
  if tmp1 != 1e12: return tmp1, tmp2

  x1 = 1e12
  for i in range(n):
    i1 = 1<<i
    if (visited & i1) == 0:
      tmp1, tmp2 = solve(i, visited|i1, weight + W[i])
      tmp1 += D[(i, idx)] /2000.0*(weight+70.0)
      if x1 > tmp1:
        x1 = tmp1
        x2 = tmp2
  x2 = name[idx] + x2
  dp[idx][visited] = [x1, x2]
  return x1, x2

name = {}
D = {}
W = {}
n = input()
dp = [[[1e12,[]] for _ in [0]*(1<<n)] for _ in [0]*n]
for i in range(n):
  a, b, c = map(int, raw_input().split())
  name[i] = [a]
  D[i] = b
  W[i] = c*20
d_init(n)

ans1 = 1e12
route = []
for i, e in W.items():
  tmp1, tmp2 = solve(i, 1<<i, e)
  if ans1 > tmp1:
    ans1 = tmp1
    route = tmp2

for e in route[:-1]:
  print str(e),
print str(route[-1])