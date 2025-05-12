from math import sqrt
def calc(x1, y1, rr1, x2, y2, rr2):
    rr0 = (x2 - x1)**2 + (y2 - y1)**2
    xd = x2 - x1
    yd = y2 - y1
    cv = (rr0 + rr1 - rr2)
    if 4*rr0*rr1 < cv**2:
        return tuple()
    if 4*rr0*rr1 == cv**2:
        return ((x1 + cv*xd/(2.*rr0), y1 + cv*yd/(2.*rr0)),)
    sv = sqrt(4*rr0*rr1 - cv**2)
    return (
        (x1 + (cv*xd - sv*yd)/(2.*rr0), y1 + (cv*yd + sv*xd)/(2.*rr0)),
        (x1 + (cv*xd + sv*yd)/(2.*rr0), y1 + (cv*yd - sv*xd)/(2.*rr0)),
    )

def solve(mid):
    ps = []
    for i in xrange(n):
        x1, y1, l1 = P[i]
        if l1 < mid:
            return 0
        rr1 = l1**2 - mid**2
        for j in xrange(i):
            x2, y2, l2 = P[j]
            rr2 = l2**2 - mid**2
            if (x1 - x2)**2 + (y1 - y2)**2 > (sqrt(rr1)+sqrt(rr2))**2:
                return 0
            ps.extend(calc(x1, y1, rr1, x2, y2, rr2))
        ps.append((x1, y1))
    if n == 1:
        return 1
    for px, py in ps:
        if all((px-x)**2 + (py-y)**2 < l**2 - mid**2 + 1e-8 for x, y, l in P):
            return 1
    return 0

while 1:
    n = input()
    if n == 0:
        break
    P = [map(int, raw_input().split()) for i in xrange(n)]

    left = 1.; right = min(l for x, y, l in P)+1e-8
    while left+1e-8 < right:
        mid = (left + right) / 2.
        if solve(mid):
            left = mid
        else:
            right = mid
    print "%.08f" % left