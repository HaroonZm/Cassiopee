import sys
input = sys.stdin.readline

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    X1 = [0] * m
    Y1 = [0] * m
    X2 = [0] * n
    Z2 = [0] * n
    for i in range(m):
        x, y = map(int, input().split())
        X1[i] = x
        Y1[i] = y
    for i in range(n):
        x, z = map(int, input().split())
        X2[i] = x
        Z2[i] = z
    min1 = min(X1)
    max1 = max(X1)
    min2 = min(X2)
    max2 = max(X2)
    X = X1 + X2
    X.sort()
    ans = 0

    # Inlining width() function as repeated code
    lX1 = len(X1)
    lX2 = len(X2)
    for i in range(len(X)-1):
        a = X[i]
        b = X[i+1]
        c = (a + b) / 2
        if not (min1 <= c <= max1 and min2 <= c <= max2):
            continue

        # width(X1, Y1, a)
        lb1a, ub1a = float('inf'), -float('inf')
        for j in range(lX1):
            x1 = X1[j]
            y1 = Y1[j]
            x2 = X1[(j+1) % lX1]
            y2 = Y1[(j+1) % lX1]
            if (x1-a)*(x2-a) <= 0 and x1 != x2:
                y = y1 + (y2 - y1) * (a - x1) / (x2 - x1)
                lb1a = min(lb1a, y)
                ub1a = max(ub1a, y)
        wa = max(0, ub1a - lb1a)

        # width(X2, Z2, a)
        lb2a, ub2a = float('inf'), -float('inf')
        for j in range(lX2):
            x1 = X2[j]
            y1 = Z2[j]
            x2p = X2[(j+1) % lX2]
            y2p = Z2[(j+1) % lX2]
            if (x1-a)*(x2p-a) <= 0 and x1 != x2p:
                y = y1 + (y2p - y1) * (a - x1) / (x2p - x1)
                lb2a = min(lb2a, y)
                ub2a = max(ub2a, y)
        za = max(0, ub2a - lb2a)

        # width(X1, Y1, b)
        lb1b, ub1b = float('inf'), -float('inf')
        for j in range(lX1):
            x1 = X1[j]
            y1 = Y1[j]
            x2 = X1[(j+1) % lX1]
            y2 = Y1[(j+1) % lX1]
            if (x1-b)*(x2-b) <= 0 and x1 != x2:
                y = y1 + (y2 - y1) * (b - x1) / (x2 - x1)
                lb1b = min(lb1b, y)
                ub1b = max(ub1b, y)
        wb = max(0, ub1b - lb1b)

        # width(X2, Z2, b)
        lb2b, ub2b = float('inf'), -float('inf')
        for j in range(lX2):
            x1 = X2[j]
            y1 = Z2[j]
            x2p = X2[(j+1) % lX2]
            y2p = Z2[(j+1) % lX2]
            if (x1-b)*(x2p-b) <= 0 and x1 != x2p:
                y = y1 + (y2p - y1) * (b - x1) / (x2p - x1)
                lb2b = min(lb2b, y)
                ub2b = max(ub2b, y)
        zb = max(0, ub2b - lb2b)

        # width(X1, Y1, c)
        lb1c, ub1c = float('inf'), -float('inf')
        for j in range(lX1):
            x1 = X1[j]
            y1 = Y1[j]
            x2 = X1[(j+1) % lX1]
            y2 = Y1[(j+1) % lX1]
            if (x1-c)*(x2-c) <= 0 and x1 != x2:
                y = y1 + (y2 - y1) * (c - x1) / (x2 - x1)
                lb1c = min(lb1c, y)
                ub1c = max(ub1c, y)
        wc = max(0, ub1c - lb1c)

        # width(X2, Z2, c)
        lb2c, ub2c = float('inf'), -float('inf')
        for j in range(lX2):
            x1 = X2[j]
            y1 = Z2[j]
            x2p = X2[(j+1) % lX2]
            y2p = Z2[(j+1) % lX2]
            if (x1-c)*(x2p-c) <= 0 and x1 != x2p:
                y = y1 + (y2p - y1) * (c - x1) / (x2p - x1)
                lb2c = min(lb2c, y)
                ub2c = max(ub2c, y)
        zc = max(0, ub2c - lb2c)

        fa = wa * za
        fb = wb * zb
        fc = wc * zc

        ans += (b - a) / 6 * (fa + 4 * fc + fb)
    print(ans)