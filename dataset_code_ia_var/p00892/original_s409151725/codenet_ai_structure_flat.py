import sys
input = sys.stdin.readline

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    X1 = []
    Y1 = []
    for _ in range(m):
        x, y = map(int, input().split())
        X1.append(x)
        Y1.append(y)
    X2 = []
    Z2 = []
    for _ in range(n):
        x, z = map(int, input().split())
        X2.append(x)
        Z2.append(z)
    min1 = min(X1)
    max1 = max(X1)
    min2 = min(X2)
    max2 = max(X2)
    X_all = X1 + X2
    X_all.sort()
    ans = 0
    for idx in range(len(X_all) - 1):
        a = X_all[idx]
        b = X_all[idx + 1]
        c = (a + b) / 2

        # width for first polygon at a, b, c
        n1 = len(X1)
        lb1a = float('inf')
        ub1a = -float('inf')
        lb1b = float('inf')
        ub1b = -float('inf')
        lb1c = float('inf')
        ub1c = -float('inf')
        for i in range(n1):
            x1a = X1[i]
            y1a = Y1[i]
            x2a = X1[(i+1)%n1]
            y2a = Y1[(i+1)%n1]
            # at a
            if (x1a - a) * (x2a - a) <= 0 and x1a != x2a:
                ya = y1a + (y2a - y1a) * (a - x1a) / (x2a - x1a)
                lb1a = min(lb1a, ya)
                ub1a = max(ub1a, ya)
            # at b
            if (x1a - b) * (x2a - b) <= 0 and x1a != x2a:
                yb = y1a + (y2a - y1a) * (b - x1a) / (x2a - x1a)
                lb1b = min(lb1b, yb)
                ub1b = max(ub1b, yb)
            # at c
            if (x1a - c) * (x2a - c) <= 0 and x1a != x2a:
                yc = y1a + (y2a - y1a) * (c - x1a) / (x2a - x1a)
                lb1c = min(lb1c, yc)
                ub1c = max(ub1c, yc)
        wa = max(0, ub1a - lb1a)
        wb = max(0, ub1b - lb1b)
        wc = max(0, ub1c - lb1c)

        # width for second polygon at a, b, c
        n2 = len(X2)
        lb2a = float('inf')
        ub2a = -float('inf')
        lb2b = float('inf')
        ub2b = -float('inf')
        lb2c = float('inf')
        ub2c = -float('inf')
        for i in range(n2):
            x1b = X2[i]
            y1b = Z2[i]
            x2b = X2[(i+1)%n2]
            y2b = Z2[(i+1)%n2]
            # at a
            if (x1b - a) * (x2b - a) <= 0 and x1b != x2b:
                ya = y1b + (y2b - y1b) * (a - x1b) / (x2b - x1b)
                lb2a = min(lb2a, ya)
                ub2a = max(ub2a, ya)
            # at b
            if (x1b - b) * (x2b - b) <= 0 and x1b != x2b:
                yb = y1b + (y2b - y1b) * (b - x1b) / (x2b - x1b)
                lb2b = min(lb2b, yb)
                ub2b = max(ub2b, yb)
            # at c
            if (x1b - c) * (x2b - c) <= 0 and x1b != x2b:
                yc = y1b + (y2b - y1b) * (c - x1b) / (x2b - x1b)
                lb2c = min(lb2c, yc)
                ub2c = max(ub2c, yc)
        wa2 = max(0, ub2a - lb2a)
        wb2 = max(0, ub2b - lb2b)
        wc2 = max(0, ub2c - lb2c)

        if min1 <= c <= max1 and min2 <= c <= max2:
            fa = wa * wa2
            fb = wb * wb2
            fc = wc * wc2
            ans += (b - a) / 6 * (fa + 4 * fc + fb)
    print(ans)