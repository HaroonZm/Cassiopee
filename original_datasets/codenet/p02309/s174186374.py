import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return Point(self.x * other, self.y * other)
    def __truediv__(self, other):
        return Point(self.x / other, self.y / other)
    def __repr__(self):
        return str(round(self.x, 8)) + ' ' + str(round(self.y, 8))
    def __lt__(self, other):
        if self.x == other.x:
            return self.y < other.y
        else:
            return self.x < other.x

class Vector(Point):
    pass

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

class Segment(Line):
    pass

class Circle:
    def __init__(self, c, r):
        self.c = c
        self.r = r

def points_to_vector(p1, p2):
    x = p1.x - p2.x
    y = p1.y - p2.y
    return Vector(x, y)

def vector(p):
    return Vector(p.x, p.y)

def dot(v1, v2):
    return v1.x * v2.x + v1.y * v2.y

def cross(v1, v2):
    return v1.x * v2.y - v1.y * v2.x

def norm(v):
    return v.x**2 + v.y**2

def distance(v):
    return math.sqrt(norm(v))

def project(s, p):
    base = points_to_vector(s.p1, s.p2)
    hypo = points_to_vector(p, s.p1)
    r = dot(hypo, base) / norm(base)
    return s.p1 + base * r

def reflect(s, p):
    return p + (project(s, p) -p) * 2

def get_distance(s1, s2):
    if intersect_s(s1, s2):
        return 0
    d1 = get_distance_sp(s1, s2.p1)
    d2 = get_distance_sp(s1, s2.p2)
    d3 = get_distance_sp(s2, s1.p1)
    d4 = get_distance_sp(s2, s1.p2)
    return min(d1, min(d2, min(d3, d4)))

def get_distance_pp(p1, p2):
    return distance(p1 - p2)

def get_distance_lp(l, p):
    return abs(cross(l.p2 - l.p1, p - l.p1) / distance(l.p2 - l.p1))

def get_distance_sp(s, p):
    if dot(s.p2 - s.p1, p - s.p1) < 0:
        return distance(p - s.p1)
    elif dot(s.p1 - s.p2, p - s.p2) < 0:
        return distance(p - s.p2)
    else:
        return get_distance_lp(s, p)

def ccw(p0, p1, p2):
    EPS = 1e-10
    COUNTER_CLOCKWISE = 1
    CLOCKWISE = -1
    ONLINE_BACK = 2
    ONLINE_FRONT = -2
    ON_SEGMENT = 0
    v1 = p1 - p0
    v2 = p2 - p0
    if cross(v1, v2) > EPS:
        return COUNTER_CLOCKWISE
    elif cross(v1, v2) < -EPS:
        return CLOCKWISE
    elif dot(v1, v2) < -EPS:
        return ONLINE_BACK
    elif norm(v1) < norm(v2):
        return ONLINE_FRONT
    else:
        return ON_SEGMENT

def intersect_p(p1, p2, p3, p4):
    return ccw(p1, p2, p3) * ccw(p1, p2, p4) <= 0 and ccw(p3, p4, p1) * ccw(p3, p4, p2) <= 0

def intersect_s(s1, s2):
    return intersect_p(s1.p1, s1.p2, s2.p1, s2.p2)

def get_cross_point(s1, s2):
    base = s2.p2 - s2.p1
    d1 = abs(cross(base, s1.p1 - s2.p1))
    d2 = abs(cross(base, s1.p2 - s2.p1))
    t = d1 / (d1 + d2)
    return s1.p1 + (s1.p2 - s1.p1) * t

def get_cross_points(c, l):
    pr = project(l, c.c)
    e = (l.p2 - l.p1) / distance(l.p2 - l.p1)
    base = math.sqrt(c.r**2 - norm(pr - c.c))
    return pr + e * base, pr - e * base

def arg(p):
    return math.atan2(p.y, p.x)

def polar(a, r):
    return Point(math.cos(r) * a, math.sin(r) * a)

def get_cross_points_cirlces(c1, c2):
    d = distance(c1.c - c2.c)
    a = math.acos((c1.r**2 + d * d - c2.r**2) / (2 * c1.r * d))
    t = arg(c2.c - c1.c)
    return c1.c + polar(c1.r, t + a), c1.c + polar(c1.r, t - a)

import sys
# sys.stdin = open('input.txt')

temp = list(map(int, input().split()))
c1 = Circle(Point(temp[0], temp[1]), temp[2])
temp = list(map(int, input().split()))
c2 = Circle(Point(temp[0], temp[1]), temp[2])
ans = get_cross_points_cirlces(c1, c2)
print(min(ans), max(ans))