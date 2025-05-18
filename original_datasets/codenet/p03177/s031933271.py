import sys
input = sys.stdin.readline
N, K = map(int, input().split())
mod = 10 ** 9 + 7
d = [list(map(int, input().split())) for _ in range(N)]
ln = K.bit_length()

def ArrayMultiple(a, b, mod):
  n = len(a)
  c = [[0] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      for k in range(n):
        c[i][j] += a[i][k] * b[k][j]
        c[i][j] %= mod
  return c

bn = list(bin(K)[2: ])
bn.reverse()
res = [[int(i == x) for i in range(N)] for x in range(N)]
for i in range(ln):
  if int(bn[i]):
    res = ArrayMultiple(res, d, mod)
  d = ArrayMultiple(d, d, mod)
rres = 0
for r in res:
  for x in r:
    rres += x
    rres %= mod
print(rres)