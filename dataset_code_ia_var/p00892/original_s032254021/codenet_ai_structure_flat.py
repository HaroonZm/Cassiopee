import sys
readline = sys.stdin.readline
write = sys.stdout.write

while True:
    line = readline()
    if not line:
        break
    M_N = line.strip()
    if not M_N:
        continue
    M, N = map(int, M_N.split())
    if M == 0 and N == 0:
        break
    P = []
    for _ in range(M):
        while True:
            l = readline()
            if l.strip():
                break
        P.append(list(map(int, l.strip().split())))
    Q = []
    for _ in range(N):
        while True:
            l = readline()
            if l.strip():
                break
        Q.append(list(map(int, l.strip().split())))
    xs = set()
    for i in range(M):
        xs.add(P[i][0])
    for i in range(N):
        xs.add(Q[i][0])
    X = list(xs)
    X.sort()
    ans = 0
    L = len(X)
    for j in range(L-1):
        def local_calc(x):
            y_ma = -100
            y_mi = 100
            for i in range(M):
                x0, y0 = P[i-1]
                x1, y1 = P[i]
                if (x0 <= x <= x1) or (x1 <= x <= x0):
                    if x0 == x1:
                        y_ma = max(y_ma, max(y1, y0))
                        y_mi = min(y_mi, min(y1, y0))
                    else:
                        y = (x - x0)*(y1-y0)/(x1-x0) + y0
                        y_ma = max(y_ma, y)
                        y_mi = min(y_mi, y)
            if not y_mi <= y_ma:
                return 0
            z_ma = -100
            z_mi = 100
            for i in range(N):
                x0, z0 = Q[i-1]
                x1, z1 = Q[i]
                if (x0 <= x <= x1) or (x1 <= x <= x0):
                    if x0 == x1:
                        z_ma = max(z_ma, max(z1, z0))
                        z_mi = min(z_mi, min(z1, z0))
                    else:
                        z = (x - x0)*(z1-z0)/(x1-x0) + z0
                        z_ma = max(z_ma, z)
                        z_mi = min(z_mi, z)
            if not z_mi <= z_ma:
                return 0
            return (z_ma - z_mi) * (y_ma - y_mi)
        x0 = X[j]
        x1 = X[j+1]
        s0 = local_calc(x0)
        s1 = local_calc((x0 + x1)/2)
        s2 = local_calc(x1)
        if s1 > 0:
            ans += (x1 - x0) * (s0 + s2 + 4*s1) / 6
    write("%.16f\n" % ans)