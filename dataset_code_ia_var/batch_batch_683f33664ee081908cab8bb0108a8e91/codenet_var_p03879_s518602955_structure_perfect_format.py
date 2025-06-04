from math import acos, tan, hypot

def getRad1(s12, s13, s23):
    return acos((s12 * s12 + s13 * s13 - s23 * s23) / (2 * s12 * s13))

def getMaxR(s12, rad1, rad2):
    tan1 = tan(rad1 / 2)
    tan2 = tan(rad2 / 2)
    h = s12 * (tan1 * tan2) / (tan1 + tan2)

    def isOK(mid):
        return s12 - mid / tan1 - mid / tan2 <= 2 * mid

    ng, ok = 0, h
    while abs(ok - ng) > 1e-12:
        mid = (ng + ok) / 2
        if isOK(mid):
            ok = mid
        else:
            ng = mid
    return ok

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

s12 = hypot(x1 - x2, y1 - y2)
s23 = hypot(x2 - x3, y2 - y3)
s31 = hypot(x3 - x1, y3 - y1)

rad1 = getRad1(s12, s31, s23)
rad2 = getRad1(s23, s12, s31)
rad3 = getRad1(s31, s23, s12)

maxRs = [
    getMaxR(s12, rad1, rad2),
    getMaxR(s23, rad2, rad3),
    getMaxR(s31, rad3, rad1)
]

print(max(maxRs))