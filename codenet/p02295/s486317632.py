import sys
from itertools import starmap
readline = sys.stdin.readline
EPS = 1e-9
ONLINE_FRONT = -2
CLOCKWISE = -1
ON_SEGMENT = 0
COUNTER_CLOCKWISE = 1
ONLINE_BACK = 2
class Segment(object):
    __slots__ = ('fi', 'se')
    def __init__(self, fi, se):
        self.fi = fi
        self.se = se
def cross(a, b):
    return a.real * b.imag - a.imag * b.real
def dot(a, b):
    return a.real * b.real + a.imag * b.imag
def norm(base):
    return abs(base) ** 2
def project(s, p2):
    base = s.fi - s.se
    r = dot(p2 - s.fi, base) / norm(base)
    return s.fi + base * r
def reflect(s, p):
    return p + (project(s, p) - p) * 2.0
def ccw(p1, p2, p3):
    a = p2 - p1
    b = p3 - p1
    if cross(a, b) > EPS: return 1
    if cross(a, b) < -EPS: return -1
    if dot(a, b) < -EPS: return 2
    if norm(a) < norm(b): return -2
    return 0
def intersect4(p1, p2, p3, p4):
    return (ccw(p1, p2, p3) * ccw(p1, p2, p4) <= 0 and
			ccw(p3, p4, p1) * ccw(p3, p4, p2) <= 0)
def intersect2(s1, s2):
    return intersect4(s1.fi, s1.se, s2.fi, s2.se)
def getDistance(a, b):  return abs(a - b)
def getDistanceLP(l, p):
    return abs(cross(l.se - l.fi, p - l.fi) / abs(l.se - l.fi))
def getDistanceSP(s, p):
    if dot(s.se - s.fi, p - s.fi) < 0.0: return abs(p - s.fi)
    if dot(s.fi - s.se, p - s.se) < 0.0: return abs(p - s.se)
    return getDistanceLP(s, p)
def getDistances(s1, s2):
    if intersect2(s1, s2): return 0.0
    return min(getDistanceSP(s1, s2.fi), getDistanceSP(s1, s2.se),
               getDistanceSP(s2, s1.fi), getDistanceSP(s2, s1.se))
def getCrossPoint(s1, s2):
	base = s2.se - s2.fi
	d1 = abs(cross(base, s1.fi - s2.fi))
	d2 = abs(cross(base, s1.se - s2.fi))
	t = d1 / (d1 + d2)
	return s1.fi + (s1.se - s1.fi) * t
n = int(readline())
for _ in [0] * n:
    p0, p1, p2, p3 = starmap(complex, zip(*[map(int, readline().split())] * 2))
    p = getCrossPoint(Segment(p0, p1), Segment(p2, p3))
    print("{0:.10f} {1:.10f}".format(p.real, p.imag))