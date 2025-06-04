import sys
input = sys.stdin.readline
mod = 998244353

N = int(input())
E = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    x, y = map(int, input().split())
    E[x].append(y)
    E[y].append(x)

Q = [1]
D = [-1] * (N + 1)
D[1] = 0
while Q:
    x = Q.pop()
    for to in E[x]:
        if D[to] == -1:
            D[to] = D[x] + 1
            Q.append(to)

f = D.index(max(D))
Q = [f]
D = [-1] * (N + 1)
D[f] = 0
while Q:
    x = Q.pop()
    for to in E[x]:
        if D[to] == -1:
            D[to] = D[x] + 1
            Q.append(to)

MAX = max(D)
l = D.index(MAX)
Q = [l]
D2 = [-1] * (N + 1)
D2[l] = 0
while Q:
    x = Q.pop()
    for to in E[x]:
        if D2[to] == -1:
            D2[to] = D2[x] + 1
            Q.append(to)

if MAX % 2 == 0:
    for i in range(N + 1):
        if D[i] == MAX // 2 and D2[i] == MAX // 2:
            c = i
            break

    TOP_SORT = []

    Q = [c]
    D = [-1] * (N + 1)
    P = [-1] * (N + 1)
    D[c] = 0
    while Q:
        x = Q.pop()
        TOP_SORT.append(x)
        for to in E[x]:
            if D[to] == -1:
                D[to] = D[x] + 1
                Q.append(to)
                P[to] = x

    DP = [[[0, 0, 0] for _ in range(3)] for _ in range(N + 1)]

    for x in TOP_SORT[::-1]:
        if D[x] == MAX // 2:
            DP[x][1][1] = 1
        elif len(E[x]) == 1:
            DP[x][0][0] = 1
        else:
            for to in E[x]:
                if to == P[x]:
                    continue
                X = [[0, 0, 0] for _ in range(3)]
                for i in range(3):
                    for j in range(3):
                        X[0][0] += DP[to][i][j]
                        X[i][0] += DP[to][i][j]
                        X[0][j] += DP[to][i][j]
                if DP[x] == [[0, 0, 0] for _ in range(3)]:
                    DP[x] = X
                else:
                    Y = [[0, 0, 0] for _ in range(3)]
                    for i in range(3):
                        for j in range(3):
                            for k in range(3):
                                for l in range(3):
                                    Y[min(2, i + k)][min(2, j + l)] = (Y[min(2, i + k)][min(2, j + l)] + X[i][j] * DP[x][k][l]) % mod
                    DP[x] = Y

    print(DP[c][1][1] * pow(2, mod - 2, mod) % mod)

else:
    for i in range(N + 1):
        if D[i] == MAX // 2 and D2[i] == MAX // 2 + 1:
            c1 = i
        elif D[i] == MAX // 2 + 1 and D2[i] == MAX // 2:
            c2 = i

    TOP_SORT = []

    Q = [c1, c2]
    D = [-1] * (N + 1)
    P = [-1] * (N + 1)
    D[c1] = 0
    D[c2] = 0
    P[c1] = c2
    P[c2] = c1

    while Q:
        x = Q.pop()
        TOP_SORT.append(x)
        for to in E[x]:
            if D[to] == -1:
                D[to] = D[x] + 1
                Q.append(to)
                P[to] = x

    DP = [[[0, 0, 0] for _ in range(3)] for _ in range(N + 1)]

    for x in TOP_SORT[::-1]:
        if D[x] == MAX // 2:
            DP[x][1][1] = 1
        elif len(E[x]) == 1:
            DP[x][0][0] = 1
        else:
            for to in E[x]:
                if to == P[x]:
                    continue
                X = [[0, 0, 0] for _ in range(3)]
                for i in range(3):
                    for j in range(3):
                        X[0][0] += DP[to][i][j]
                        X[i][0] += DP[to][i][j]
                        X[0][j] += DP[to][i][j]
                if DP[x] == [[0, 0, 0] for _ in range(3)]:
                    DP[x] = X
                else:
                    Y = [[0, 0, 0] for _ in range(3)]
                    for i in range(3):
                        for j in range(3):
                            for k in range(3):
                                for l in range(3):
                                    Y[min(2, i + k)][min(2, j + l)] = (Y[min(2, i + k)][min(2, j + l)] + X[i][j] * DP[x][k][l]) % mod
                    DP[x] = Y

    print(sum(DP[c1][1]) * sum(DP[c2][1]) % mod)