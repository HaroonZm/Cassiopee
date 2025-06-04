import sys
readline = sys.stdin.readline
write = sys.stdout.write

while True:
    vals = readline()
    if not vals:
        break
    x1y1x2y2x3y3 = list(map(int, vals.split()))
    if len(x1y1x2y2x3y3) < 6:
        continue
    x1, y1, x2, y2, x3, y3 = x1y1x2y2x3y3
    if x1 == y1 == x2 == y2 == x3 == y3 == 0:
        break

    d12 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    d23 = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
    d31 = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5

    e1 = ((x1, y1), ((x2 - x1) / d12, (y2 - y1) / d12), ((x3 - x1) / d31, (y3 - y1) / d31))
    e2 = ((x2, y2), ((x3 - x2) / d23, (y3 - y2) / d23), ((x1 - x2) / d12, (y1 - y2) / d12))
    e3 = ((x3, y3), ((x1 - x3) / d31, (y1 - y3) / d31), ((x2 - x3) / d23, (y2 - y3) / d23))

    EPS = 1e-8

    # flatten calc
    def calc(e, x):
        p0, p1, p2 = e
        x0, y0 = p0
        x1, y1 = p1
        x2, y2 = p2
        xc = (x1 + x2) / 2
        yc = (y1 + y2) / 2
        dc = (xc ** 2 + yc ** 2) ** 0.5
        cv = (x1 * xc + y1 * yc) / dc
        sv = (x1 * yc - y1 * xc) / dc
        d = x / cv
        return (x0 + xc * d / dc, y0 + yc * d / dc), x * sv / cv

    # flatten check
    def check(p0, r0):
        x0, y0 = p0
        left = 0
        right = min(d12, d23)
        while right - left > EPS:
            mid = (left + right) / 2
            (x1, y1), r1 = calc(e2, mid)
            if (x0 - x1) ** 2 + (y0 - y1) ** 2 < (r0 + r1) ** 2:
                right = mid
            else:
                left = mid
        (x1, y1), r1 = calc(e2, left)
        left2 = 0
        right2 = min(d23, d31)
        while right2 - left2 > EPS:
            mid2 = (left2 + right2) / 2
            (x2, y2), r2 = calc(e3, mid2)
            if (x0 - x2) ** 2 + (y0 - y2) ** 2 < (r0 + r2) ** 2:
                right2 = mid2
            else:
                left2 = mid2
        (x2, y2), r2 = calc(e3, left2)
        return (x1 - x2) ** 2 + (y1 - y2) ** 2 < (r1 + r2) ** 2, r1, r2

    left = 0
    right = min(d12, d31)
    while right - left > EPS:
        mid = (left + right) / 2
        p0, r0 = calc(e1, mid)
        ok, r1, r2 = check(p0, r0)
        if ok:
            left = mid
        else:
            right = mid
    p0, r0 = calc(e1, right)
    ok, r1, r2 = check(p0, r0)

    write("%.16f %.16f %.16f\n" % (r0, r1, r2))