while 1:
    tmp = input().split()
    M, N = int(tmp[0]), int(tmp[1])
    if not (M and N):
        break
    X1 = []
    Y1 = []
    X2 = []
    Z2 = []
    for i in range(M):
        d = input().split()
        X1.append(int(d[0]))
        Y1.append(int(d[1]))
    for i in range(N):
        d = input().split()
        X2.append(int(d[0]))
        Z2.append(int(d[1]))
    XS = X1 + X2
    XS.sort()
    min1, max1 = min(X1), max(X1)
    min2, max2 = min(X2), max(X2)
    res = 0
    for i in range(len(XS) - 1):
        a = XS[i]
        b = XS[i + 1]
        c = (a + b) / 2
        if min1 <= c <= max1 and min2 <= c <= max2:
            n = len(X1)
            lb, ub = float('inf'), -float('inf')
            for j in range(n):
                x1, y1 = X1[j], Y1[j]
                x2, y2 = X1[(j + 1) % n], Y1[(j + 1) % n]
                if (x1 - a) * (x2 - a) <= 0 and x1 != x2:
                    y = y1 + (y2 - y1) * (a - x1) / (x2 - x1)
                    lb = min(lb, y)
                    ub = max(ub, y)
            wa = max(0, ub - lb)
            n = len(X2)
            lb, ub = float('inf'), -float('inf')
            for j in range(n):
                x1, y1 = X2[j], Z2[j]
                x2, y2 = X2[(j + 1) % n], Z2[(j + 1) % n]
                if (x1 - a) * (x2 - a) <= 0 and x1 != x2:
                    y = y1 + (y2 - y1) * (a - x1) / (x2 - x1)
                    lb = min(lb, y)
                    ub = max(ub, y)
            wa2 = max(0, ub - lb)
            fa = wa * wa2

            n = len(X1)
            lb, ub = float('inf'), -float('inf')
            for j in range(n):
                x1, y1 = X1[j], Y1[j]
                x2, y2 = X1[(j + 1) % n], Y1[(j + 1) % n]
                if (x1 - b) * (x2 - b) <= 0 and x1 != x2:
                    y = y1 + (y2 - y1) * (b - x1) / (x2 - x1)
                    lb = min(lb, y)
                    ub = max(ub, y)
            wb = max(0, ub - lb)
            n = len(X2)
            lb, ub = float('inf'), -float('inf')
            for j in range(n):
                x1, y1 = X2[j], Z2[j]
                x2, y2 = X2[(j + 1) % n], Z2[(j + 1) % n]
                if (x1 - b) * (x2 - b) <= 0 and x1 != x2:
                    y = y1 + (y2 - y1) * (b - x1) / (x2 - x1)
                    lb = min(lb, y)
                    ub = max(ub, y)
            wb2 = max(0, ub - lb)
            fb = wb * wb2

            n = len(X1)
            lb, ub = float('inf'), -float('inf')
            for j in range(n):
                x1, y1 = X1[j], Y1[j]
                x2, y2 = X1[(j + 1) % n], Y1[(j + 1) % n]
                if (x1 - c) * (x2 - c) <= 0 and x1 != x2:
                    y = y1 + (y2 - y1) * (c - x1) / (x2 - x1)
                    lb = min(lb, y)
                    ub = max(ub, y)
            wc = max(0, ub - lb)
            n = len(X2)
            lb, ub = float('inf'), -float('inf')
            for j in range(n):
                x1, y1 = X2[j], Z2[j]
                x2, y2 = X2[(j + 1) % n], Z2[(j + 1) % n]
                if (x1 - c) * (x2 - c) <= 0 and x1 != x2:
                    y = y1 + (y2 - y1) * (c - x1) / (x2 - x1)
                    lb = min(lb, y)
                    ub = max(ub, y)
            wc2 = max(0, ub - lb)
            fc = wc * wc2

            res += (b - a) / 6 * (fa + 4 * fc + fb)
    print('%.10f' % res)