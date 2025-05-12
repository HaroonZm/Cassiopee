from math import sqrt
x1, y1 = map(int, raw_input().split())
x0, y0, r0 = map(int, raw_input().split())

def solve(x1, y1, r1, x2, y2, r2):
    rr0 = (x2 - x1)**2 + (y2 - y1)**2
    xd = x2 - x1
    yd = y2 - y1
    rr1 = r1**2; rr2 = r2**2
    cv = (rr0 + rr1 - rr2)
    sv = sqrt(4*rr0*rr1 - cv**2)
    return (
        (x1 + (cv*xd - sv*yd)/(2.*rr0), y1 + (cv*yd + sv*xd)/(2.*rr0)),
        (x1 + (cv*xd + sv*yd)/(2.*rr0), y1 + (cv*yd - sv*xd)/(2.*rr0)),
    )

r1 = sqrt((x1 - x0)**2 + (y1 - y0)**2 - r0**2)

p0, p1 = sorted(solve(x1, y1, r1, x0, y0, r0))
print "%.08f %.08f" % p0
print "%.08f %.08f" % p1