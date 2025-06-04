N = int(input())
XS = set()
YS = set()
P = []
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    XS.add(x1)
    XS.add(x2)
    YS.add(y1)
    YS.add(y2)
    P.append((x1, y1, x2, y2))
X = sorted(XS)
Y = sorted(YS)
MX = {}
for i in range(len(X)):
    MX[X[i]] = i
MY = {}
for i in range(len(Y)):
    MY[Y[i]] = i
H = len(Y)
W = len(X)
S = []
for i in range(H+1):
    S.append([0]*(W+1))
for k in range(len(P)):
    x1, y1, x2, y2 = P[k]
    p1 = MY[y1]
    q1 = MX[x1]
    p2 = MY[y2]
    q2 = MX[x2]
    S[p1][q1] += 1
    S[p1][q2] -= 1
    S[p2][q1] -= 1
    S[p2][q2] += 1
i = 0
while i < H:
    j = 0
    while j < W:
        S[i][j+1] += S[i][j]
        j += 1
    i += 1
j = 0
while j < W:
    i = 0
    while i < H:
        S[i+1][j] += S[i][j]
        i += 1
    j += 1
ans = 0
i = 0
while i < H:
    j = 0
    while j < W:
        if S[i][j]:
            ans += (Y[i+1] - Y[i]) * (X[j+1] - X[j])
        j += 1
    i += 1
print(ans)