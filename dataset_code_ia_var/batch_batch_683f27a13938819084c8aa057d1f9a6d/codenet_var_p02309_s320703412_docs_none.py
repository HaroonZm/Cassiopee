from math import sqrt

def cross_point(circle1, circle2):
    x1, y1, r1 = circle1
    x2, y2, r2 = circle2
    if r1 < r2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        r1, r2 = r2, r1
    p1p2 = (x2 - x1, y2 - y1)
    np = norm(p1p2)
    if np > (r1 + r2) ** 2 or np < (r1 - r2) ** 2:
        return []
    else:
        lp = sqrt(np)
        a = (p1p2[0] / lp, p1p2[1] / lp)
        b = ((y1 - y2) / lp, (x2 - x1) / lp)
        h = sqrt((r1 + r2 + lp) * (-r1 + r2 + lp) * (r1 - r2 + lp) * (r1 + r2 - lp)) / (2 * lp)
        t = sqrt(r1 * r1 - h * h)
        if h < 1e-10:
            return [(x1 + t * a[0] + h * b[0], y1 + t * a[1] + h * b[1])]
        else:
            return [(x1 + t * a[0] + h * b[0], y1 + t * a[1] + h * b[1]),
                    (x1 + t * a[0] - h * b[0], y1 + t * a[1] - h * b[1])]

def norm(v):
    x, y = v
    return x ** 2 + y ** 2

def run():
    c1 = [int(i) for i in input().split()]
    c2 = [int(i) for i in input().split()]
    ps = cross_point(c1, c2)
    if len(ps) == 0:
        raise ValueError('two circles do not intersect')
    if len(ps) == 1:
        ps *= 2
    p1, p2 = ps
    if p1 > p2:
        p1, p2 = p2, p1
    print("{:.8f} {:.8f} {:.8f} {:.8f}".format(*p1, *p2))

if __name__ == '__main__':
    run()