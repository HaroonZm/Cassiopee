from collections import deque

N = int(input())
X = [[] for i in range(N)]
for i in range(N-1):
    x, y = map(int, input().split())
    X[x-1].append(y-1)
    X[y-1].append(x-1)

P = [-1] * N
Q = deque([0])
T = []
while Q:
    i = deque.popleft(Q)
    T.append(i)
    for a in X[i]:
        if a != P[i]:
            P[a] = i
            X[a].remove(i)
            deque.append(Q, a)

BUA = [0] * N # Bottom Up : i以下をすべてまわる
BUB = [0] * N # Bottom Up : i以下をすべてまわってiに戻る
TDA = [0] * N # Top Down : iの上をすべてまわる
TDB = [0] * N # Top Down : iの上をすべてまわってiに戻る
for i in T[::-1]:
    if len(X[i]) == 0:
        BUA[i] = 0
        BUB[i] = 0
        continue
    s = 0
    ma = 0
    for j in X[i]:
        s += BUB[j] + 2
        ma = max(ma, BUB[j] - BUA[j] + 1)
    BUA[i] = s - ma
    BUB[i] = s

for i in T:
    B = [0] * (len(X[i]) + 1)
    C = [0] * (len(X[i]) + 1)
    for k, j in enumerate(X[i]):
        B[k+1] = B[k] + BUB[j] + 2
        C[k+1] = max(C[k], BUB[j] - BUA[j] + 2)
    s = 0
    ma = 0
    for k in range(len(X[i]))[::-1]:
        j = X[i][k]
        TDB[j] = TDB[i] + s + B[k] + 2
        TDA[j] = min(TDB[j] - max(ma, C[k]), TDA[i] + s + B[k] + 1)
        s += BUB[j] + 2
        ma = max(ma, BUB[j] - BUA[j] + 2)

for t in [min(a+d, b+c) for a, b, c, d in zip(BUA, BUB, TDA, TDB)]:
    print(t)