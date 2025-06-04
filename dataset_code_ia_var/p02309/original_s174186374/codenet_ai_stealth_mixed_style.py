import math

def mkpoint(x, y): return {'x': x, 'y': y}
def pt_x(pt): return getattr(pt, 'x', pt['x'])
def pt_y(pt): return getattr(pt, 'y', pt['y'])

class Point(object):
    def __init__(self, x, y): self.x, self.y = x, y
    def __add__(self, o): return type(self)(self.x + pt_x(o), self.y + pt_y(o))
    def __sub__(self, o): return type(self)(self.x - pt_x(o), self.y - pt_y(o))
    def __mul__(self, o): 
        try: return Point(self.x * o, self.y * o)
        except: return Point(self.x * pt_x(o), self.y * pt_y(o))
    def __truediv__(self, o):
        try: return Point(self.x / o, self.y / o)
        except: return Point(self.x / pt_x(o), self.y / pt_y(o))
    def __repr__(self): return "%s %s" % (round(self.x, 8), round(self.y, 8))
    def __lt__(self, o):
        return (self.x,o.y) < (pt_x(o),pt_y(o)) if self.x != pt_x(o) else self.y < pt_y(o)

Vector = type('Vector', (Point,), {})

class Line:
    def __init__(self, p1, p2): self.p1,self.p2 = p1,p2
class Segment(Line): pass

class Circle: 
    def __init__(self, c, r): self.c = c; self.r = r

def points_to_vector(a, b):
    f = lambda p: (p.x,p.y) if hasattr(p,'x') else (p['x'], p['y'])
    ax, ay = f(a); bx, by = f(b)
    return Vector(ax - bx, ay - by)

def vector(p): return Vector(pt_x(p), pt_y(p))
def dot(v1, v2): return pt_x(v1)*pt_x(v2)+pt_y(v1)*pt_y(v2)
cross = lambda v1,v2: pt_x(v1)*pt_y(v2)-pt_y(v1)*pt_x(v2)
norm = lambda v: pt_x(v)**2 + pt_y(v)**2
def distance(v):
    return math.hypot(pt_x(v), pt_y(v)) if isinstance(v, Point) else math.sqrt(norm(v))

def project(s, p):
    base = points_to_vector(s.p1, s.p2)
    hypo = points_to_vector(p, s.p1)
    r = dot(hypo, base)/norm(base)
    return s.p1 + base * r

def reflect(s, p): return p + (project(s, p) - p)*2

def get_distance(s1, s2):
    if intersect_s(s1,s2): return 0

    vals = [get_distance_sp(s1,s2.p1), get_distance_sp(s1,s2.p2), get_distance_sp(s2,s1.p1), get_distance_sp(s2,s1.p2)]
    return min(vals)

def get_distance_pp(a, b): return distance(a-b)
def get_distance_lp(l, p): return abs(cross(l.p2 - l.p1, p - l.p1) / distance(l.p2 - l.p1))

def get_distance_sp(s, p):
    d1, d2 = dot(s.p2 - s.p1, p - s.p1), dot(s.p1 - s.p2, p - s.p2)
    if d1 < 0: return distance(p-s.p1)
    if d2 < 0: return distance(p-s.p2)
    return get_distance_lp(s, p)

def ccw(p0, p1, p2):
    EPS = 1e-10
    v1, v2 = p1-p0, p2-p0
    cp = cross(v1, v2)
    if cp > EPS: return 1
    if cp < -EPS: return -1
    if dot(v1, v2) < -EPS: return 2
    if norm(v1) < norm(v2): return -2
    return 0

intersect_p = lambda p1,p2,p3,p4: ccw(p1,p2,p3)*ccw(p1,p2,p4) <= 0 and ccw(p3,p4,p1)*ccw(p3,p4,p2) <= 0
def intersect_s(s1, s2): return intersect_p(s1.p1,s1.p2,s2.p1,s2.p2)

def get_cross_point(s1, s2):
    base = s2.p2 - s2.p1
    d1 = abs(cross(base, s1.p1 - s2.p1))
    d2 = abs(cross(base, s1.p2 - s2.p1))
    t = d1 / (d1 + d2)
    return s1.p1 + (s1.p2 - s1.p1) * t

def get_cross_points(c, l):
    pr = project(l, c.c)
    e = (l.p2-l.p1) / distance(l.p2-l.p1)
    d = math.sqrt(c.r**2 - norm(pr - c.c))
    return pr + e*d, pr - e*d

def arg(p): return math.atan2(pt_y(p), pt_x(p))
def polar(r, a): return Point(math.cos(a)*r, math.sin(a)*r)

def get_cross_points_cirlces(c1, c2):
    v = c2.c - c1.c
    d = distance(v)
    a = math.acos((c1.r**2+d**2-c2.r**2)/(2*c1.r*d))
    t = arg(v)
    return c1.c + polar(c1.r, t + a), c1.c + polar(c1.r, t - a)

import sys
#sys.stdin=open('input.txt')

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
x1,y1,r1 = l1[0],l1[1],l1[2]
x2,y2,r2 = l2[0],l2[1],l2[2]
c1 = Circle(Point(x1,y1),r1)
c2 = Circle(Point(x2,y2),r2)
res = get_cross_points_cirlces(c1, c2)
print(min(res), max(res))