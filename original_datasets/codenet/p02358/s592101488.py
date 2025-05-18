N = int(input())

XS = set(); YS = set()

P = []
for i in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    XS.add(x1); XS.add(x2)
    YS.add(y1); YS.add(y2)
    P.append((x1, y1, x2, y2))

X = sorted(XS); Y = sorted(YS)
MX = {x: i for i, x in enumerate(X)}
MY = {y: i for i, y in enumerate(Y)}

H = len(Y); W = len(X)
S = [[0]*(W+1) for i in range(H+1)]
for x1, y1, x2, y2 in P:
    p1 = MY[y1]; q1 = MX[x1]
    p2 = MY[y2]; q2 = MX[x2]

    S[p1][q1] += 1
    S[p1][q2] -= 1
    S[p2][q1] -= 1
    S[p2][q2] += 1

for i in range(H):
    for j in range(W):
        S[i][j+1] += S[i][j]
for j in range(W):
    for i in range(H):
        S[i+1][j] += S[i][j]
ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j]:
            ans += (Y[i+1] - Y[i]) * (X[j+1] - X[j])
print(ans)