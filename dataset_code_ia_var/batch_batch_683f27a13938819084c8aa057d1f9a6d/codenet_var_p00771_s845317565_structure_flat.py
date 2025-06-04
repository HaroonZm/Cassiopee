import sys
MI = 1e-6
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    b = []
    for _ in range(n):
        bx, by, l = map(int, sys.stdin.readline().split())
        b.append([bx, by, l])
    px0 = -100
    px1 = -33
    px2 = 33
    px3 = 100
    for _ in range(100):
        if abs(px0 - px3) < MI:
            x1 = px0
            x2 = px3
            break
        else:
            x1 = px0
            x2 = px3
        y10 = -100
        y11 = -33
        y12 = 33
        y13 = 100
        for __ in range(100):
            if abs(y10 - y13) < MI:
                v1 = 0
                for bx, by, l in b:
                    d = l**2 - (px1-bx)**2 - (y10-by)**2
                    if __ == 0:
                        v1 = d
                    else:
                        v1 = min(v1, d)
                v2 = 0
                for bx, by, l in b:
                    d = l**2 - (px1-bx)**2 - (y13-by)**2
                    if __ == 0:
                        v2 = d
                    else:
                        v2 = min(v2, d)
                sy1 = (v1 + v2) / 2
                break
            else:
                v1 = 0
                for bx, by, l in b:
                    d = l**2 - (px1-bx)**2 - (y11-by)**2
                    if __ == 0:
                        v1 = d
                    else:
                        v1 = min(v1, d)
                v2 = 0
                for bx, by, l in b:
                    d = l**2 - (px1-bx)**2 - (y12-by)**2
                    if __ == 0:
                        v2 = d
                    else:
                        v2 = min(v2, d)
                if v1 < v2:
                    y10 = y11
                else:
                    y13 = y12
                y11 = (2*y10 + y13) / 3
                y12 = (y10 + 2*y13) / 3
        y20 = -100
        y21 = -33
        y22 = 33
        y23 = 100
        for ___ in range(100):
            if abs(y20 - y23) < MI:
                v1 = 0
                for bx, by, l in b:
                    d = l**2 - (px2-bx)**2 - (y20-by)**2
                    if ___ == 0:
                        v1 = d
                    else:
                        v1 = min(v1, d)
                v2 = 0
                for bx, by, l in b:
                    d = l**2 - (px2-bx)**2 - (y23-by)**2
                    if ___ == 0:
                        v2 = d
                    else:
                        v2 = min(v2, d)
                sy2 = (v1 + v2) / 2
                break
            else:
                v1 = 0
                for bx, by, l in b:
                    d = l**2 - (px2-bx)**2 - (y21-by)**2
                    if ___ == 0:
                        v1 = d
                    else:
                        v1 = min(v1, d)
                v2 = 0
                for bx, by, l in b:
                    d = l**2 - (px2-bx)**2 - (y22-by)**2
                    if ___ == 0:
                        v2 = d
                    else:
                        v2 = min(v2, d)
                if v1 < v2:
                    y20 = y21
                else:
                    y23 = y22
                y21 = (2*y20 + y23) / 3
                y22 = (y20 + 2*y23) / 3
        if sy1 < sy2:
            px0 = px1
        else:
            px3 = px2
        px1 = (2*px0 + px3) / 3
        px2 = (px0 + 2*px3) / 3
    x10 = -100
    x11 = -33
    x12 = 33
    x13 = 100
    for _ in range(100):
        if abs(x10 - x13) < MI:
            vx1 = 0
            for bx, by, l in b:
                d = l**2 - (x10-bx)**2 - (y10-by)**2
                vx1 = d if _ == 0 else min(vx1, d)
            vx2 = 0
            for bx, by, l in b:
                d = l**2 - (x13-bx)**2 - (y13-by)**2
                vx2 = d if _ == 0 else min(vx2, d)
            ans = (vx1 + vx2) / 2
            break
        else:
            vx1 = 0
            for bx, by, l in b:
                d = l**2 - (x11-bx)**2 - (y11-by)**2
                vx1 = d if _ == 0 else min(vx1, d)
            vx2 = 0
            for bx, by, l in b:
                d = l**2 - (x12-bx)**2 - (y12-by)**2
                vx2 = d if _ == 0 else min(vx2, d)
            if vx1 < vx2:
                x10 = x11
            else:
                x13 = x12
            x11 = (2*x10 + x13) / 3
            x12 = (x10 + 2*x13) / 3
    print(ans**0.5)