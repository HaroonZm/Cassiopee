import sys
from itertools import starmap as _starmap

get = sys.stdin.readline

# Déclarations en mode C-like
EPS = 1e-9
ONLINE_FRONT, CLOCKWISE, ON_SEGMENT, COUNTER_CLOCKWISE, ONLINE_BACK = -2, -1, 0, 1, 2

# POO rustine
class Segment:
    __slots__ = ['fi', 'se']
    def __init__(self, a, b):
        setattr(self, 'fi', a)
        self.se = b

# Programmation fonctionnelle et procédurale mélangée
cross = lambda u, v: u.real * v.imag - u.imag * v.real
def dot(u, v): return (u.real * v.real) + (u.imag * v.imag)
def norm(z):
    return abs(z) ** 2

def project(seg, p):
    base = seg.fi - seg.se
    r = dot(p - seg.fi, base) / norm(base)
    return seg.fi + base * r

reflect = lambda s, pt: pt + (project(s, pt) - pt) * 2

def ccw(p1, p2, p3):
    a, b = p2 - p1, p3 - p1
    c = cross(a, b)
    if c > EPS: return COUNTER_CLOCKWISE
    if c < -EPS: return CLOCKWISE
    if dot(a, b) < -EPS: return ONLINE_BACK
    if norm(a) < norm(b): return ONLINE_FRONT
    return ON_SEGMENT

def intersect4(a, b, c, d):
    return (ccw(a, b, c) * ccw(a, b, d) <= 0) and (ccw(c, d, a) * ccw(c, d, b) <= 0)

def intersect2(l, m): return intersect4(l.fi, l.se, m.fi, m.se)

# Passage entre paradigmes pour le calcul des distances
getDistance = lambda x, y: abs(x - y)
def getDistanceLP(line, p):
    return abs(cross(line.se - line.fi, p - line.fi) / abs(line.se - line.fi))
def getDistanceSP(s, pt):
    if dot(s.se - s.fi, pt - s.fi) < 0: return abs(pt - s.fi)
    if dot(s.fi - s.se, pt - s.se) < 0: return abs(pt - s.se)
    return getDistanceLP(s, pt)
def getDistances(seg1, seg2):
    if intersect2(seg1, seg2):
        return 0.0
    return min(getDistanceSP(seg1, seg2.fi), getDistanceSP(seg1, seg2.se), getDistanceSP(seg2, seg1.fi), getDistanceSP(seg2, seg1.se))

# Calcul procédural style code soggy
def getCrossPoint(a, b):
    zz = b.se - b.fi
    d1 = abs(cross(zz, a.fi - b.fi))
    d2 = abs(cross(zz, a.se - b.fi))
    t = d1 / (d1 + d2)
    return a.fi + (a.se - a.fi) * t

def parse_points():
    pts = list(_starmap(complex, zip(*[map(int, get().split())]*2)))
    return pts

for __ in range(int(get())):
    po, p1, p2, p3 = parse_points()
    pu = getCrossPoint(Segment(po, p1), Segment(p2, p3))
    # Impression type Ruby-style et C combinés
    print("%.10f %.10f" % (pu.real, pu.imag))