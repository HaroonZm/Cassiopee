from collections import defaultdict
INF = 10**9
while 1:
    N = int(input())
    if N == 0:
        break
    P = [list(map(int, input().split())) for i in range(N)]
    S = defaultdict(list)
    X = set()
    x0 = y0 = INF; x1 = y1 = -INF
    for i in range(4):
        x, y = map(int, input().split())
        x0 = min(x0, x); x1 = max(x1, x)
        y0 = min(y0, y); y1 = max(y1, y)
    S[y0] = [INF]; S[y1] = [INF]
    X.add(x0); X.add(x1)
    for x, y in P:
        S[y].append(x)
        X.add(x)
    xs = sorted(X)
    MP = {x: i for i, x in enumerate(xs)}
    L = len(xs)

    su = 0
    for i in range(N):
        xa, ya = P[i-1]
        xb, yb = P[i]
        su += xa*yb - ya*xb
    su = abs(su) // 2
    res = 0
    *ps, = S.items()
    ps.sort()
    mode = 0
    prv = -1
    U = [0]*L
    for y, vs in ps:
        if mode:
            px = 0; c = 0
            d = y - prv
            for i in range(L):
                if U[i]:
                    x = min(max(xs[i], x0), x1)
                    if c == 1:
                        res += d * (x - px)
                    c ^= 1
                    px = x
        for x in vs:
            if x == INF:
                mode ^= 1
            else:
                U[MP[x]] ^= 1
        prv = y
    print(su - res)