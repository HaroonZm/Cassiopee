from collections import defaultdict, deque
from bisect import bisect
W, H, M = map(int, input().split())
L = [list(map(int, input().split())) for i in range(M)]

XS = set([0, W])
YS = set([0, H])

for px, py, qx, qy in L:
    XS.add(px); XS.add(qx)
    YS.add(py); YS.add(qy)

X0 = sorted(XS)
Y0 = sorted(YS)

def convert(X0):
    mp = {}
    prv = -1
    cur = 0
    for x in X0:
        mp[x] = cur
        cur += 2
        prv = x
    cur -= 1
    return mp, cur

XM, X = convert(X0)
YM, Y = convert(Y0)

C = [[0]*X for i in range(Y)]
D = [[-1]*X for i in range(Y)]
for i in range(Y):
    C[i][0] = C[i][X-1] = 1
for i in range(X):
    C[0][i] = C[Y-1][i] = 1
for px, py, qx, qy in L:
    if px == qx:
        if not py < qy:
            py, qy = qy, py
        x0 = XM[px]
        y0 = YM[py]; y1 = YM[qy]
        for i in range(y0, y1+1):
            C[i][x0] = 1
    else:
        if not px < qx:
            px, qx = qx, px
        x0 = XM[px]; x1 = XM[qx]
        y0 = YM[py]
        for i in range(x0, x1+1):
            C[y0][i] = 1

dd = ((-1, 0), (0, -1), (1, 0), (0, 1))
que = deque()
cur = 0
for i in range(Y):
    for j in range(X):
        if C[i][j] or D[i][j] != -1:
            continue
        D[i][j] = cur
        que.append((j, i))
        while que:
            x, y = que.popleft()
            for dx, dy in dd:
                nx = x + dx; ny = y + dy
                if C[ny][nx] or D[ny][nx] != -1:
                    continue
                D[ny][nx] = cur
                que.append((nx, ny))
        cur += 1

N = cur
INF = 10**9
G = [[] for i in range(N)]
for i in range(1, Y-1):
    for j in range(1, X-1):
        a = D[i-1][j]; b = D[i+1][j]
        if a != -1 != b != a:
            G[a].append(b)
            G[b].append(a)
        a = D[i][j-1]; b = D[i][j+1]
        if a != -1 != b != a:
            G[a].append(b)
            G[b].append(a)

Q = int(input())
for i in range(Q):
    sx, sy, gx, gy = map(int, input().split())
    x0 = (bisect(X0, sx)-1)*2+1; y0 = (bisect(Y0, sy-1)-1)*2+1
    x1 = (bisect(X0, gx)-1)*2+1; y1 = (bisect(Y0, gy)-1)*2+1
    assert D[y0][x0] != -1 and D[y1][x1] != -1
    s = D[y0][x0]; t = D[y1][x1]
    que = deque([s])
    U = [-1]*N
    U[s] = 0
    while que:
        v = que.popleft()
        d = U[v]
        for w in G[v]:
            if U[w] != -1:
                continue
            U[w] = d+1
            que.append(w)
    print(U[t])