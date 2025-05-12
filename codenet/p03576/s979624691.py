import sys
input = sys.stdin.buffer.readline
N, M = map(int, input().split())
P = []
for _ in range(N):
  P.append(list(map(int, input().split())))
X = sorted(set([p[0] for p in P]))
Y = sorted(set([p[1] for p in P]))

res = (X[-1] - X[0]) * (Y[-1] - Y[0])
cs = [[0] * (len(Y)) for _ in range(len(X))]

for i in range(len(X)):
  for j in range(len(Y)):
    for p in P:
      if X[0] <= p[0] <= X[i] and Y[0] <= p[1] <= Y[j]:
        cs[i][j] += 1
for l in range(len(X) - 1):
  for r in range(l + 1, len(X)):
    for d in range(len(Y) - 1):
      for u in range(d + 1, len(Y)):
        a = cs[r][u]
        if l > 0:
          a -= cs[l - 1][u]
        if d > 0:
          a -= cs[r][d - 1]
        if l > 0 and d > 0:
          a += cs[l - 1][d - 1]
        if a >= M:
          #print(X[l], X[r], Y[d], Y[u], abs(X[r] - X[l]) * abs(Y[u] - Y[d]), a, l, r, d, u)
          res = min(res, abs(X[r] - X[l]) * abs(Y[u] - Y[d]))
print(res)