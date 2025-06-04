import sys
input = sys.stdin.buffer.readline
N, M = map(int, input().split())
P = []
for _ in range(N):
    P.append(list(map(int, input().split())))
X = sorted(set([p[0] for p in P]))
Y = sorted(set([p[1] for p in P]))
cs = [[0]*len(Y) for _ in range(len(X))]
for p in P:
    i = X.index(p[0])
    j = Y.index(p[1])
    cs[i][j] += 1
for i in range(len(X)):
    for j in range(len(Y)):
        if i > 0:
            cs[i][j] += cs[i-1][j]
        if j > 0:
            cs[i][j] += cs[i][j-1]
        if i > 0 and j > 0:
            cs[i][j] -= cs[i-1][j-1]
res = (X[-1] - X[0]) * (Y[-1] - Y[0])
for l in range(len(X)):
    for r in range(l, len(X)):
        for d in range(len(Y)):
            for u in range(d, len(Y)):
                total = cs[r][u]
                if l > 0:
                    total -= cs[l-1][u]
                if d > 0:
                    total -= cs[r][d-1]
                if l > 0 and d > 0:
                    total += cs[l-1][d-1]
                if total >= M:
                    area = (X[r] - X[l]) * (Y[u] - Y[d])
                    res = min(res, area)
print(res)