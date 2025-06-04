from math import sqrt

while 1:
    n = input()
    if n == 0:
        break
    P = [map(int, raw_input().split()) for i in xrange(n)]

    left = 1.
    right = min(l for x, y, l in P) + 1e-8
    while left + 1e-8 < right:
        mid = (left + right) / 2.
        ps = []
        ok = True
        for i in xrange(n):
            x1, y1, l1 = P[i]
            if l1 < mid:
                ok = False
                break
            rr1 = l1**2 - mid**2
            for j in xrange(i):
                x2, y2, l2 = P[j]
                rr2 = l2**2 - mid**2
                if (x1 - x2)**2 + (y1 - y2)**2 > (sqrt(rr1)+sqrt(rr2))**2:
                    ok = False
                    break
                rr0 = (x2 - x1)**2 + (y2 - y1)**2
                xd = x2 - x1
                yd = y2 - y1
                cv = rr0 + rr1 - rr2
                if 4*rr0*rr1 < cv**2:
                    continue
                if 4*rr0*rr1 == cv**2:
                    px = x1 + cv*xd/(2.*rr0)
                    py = y1 + cv*yd/(2.*rr0)
                    ps.append((px, py))
                    continue
                sv = sqrt(4*rr0*rr1 - cv**2)
                px1 = x1 + (cv*xd - sv*yd)/(2.*rr0)
                py1 = y1 + (cv*yd + sv*xd)/(2.*rr0)
                px2 = x1 + (cv*xd + sv*yd)/(2.*rr0)
                py2 = y1 + (cv*yd - sv*xd)/(2.*rr0)
                ps.append((px1, py1))
                ps.append((px2, py2))
            if not ok:
                break
            ps.append((x1, y1))
        res = 0
        if ok:
            if n == 1:
                res = 1
            else:
                for px, py in ps:
                    inside = True
                    for x, y, l in P:
                        if (px-x)**2 + (py-y)**2 >= l**2 - mid**2 + 1e-8:
                            inside = False
                            break
                    if inside:
                        res = 1
                        break
        if res:
            left = mid
        else:
            right = mid
    print "%.08f" % left