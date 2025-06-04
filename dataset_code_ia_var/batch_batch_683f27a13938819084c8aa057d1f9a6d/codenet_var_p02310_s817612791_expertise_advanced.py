from math import pi, cos, sin, atan2, hypot, isclose
from functools import cached_property, singledispatch
from operator import attrgetter

EPS = 1e-9

def eq(a, b):
    return isclose(a, b, abs_tol=EPS)

class Point:
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @cached_property
    def arg(self):
        return atan2(self.y, self.x)
    def __str__(self):
        return f"{self.x:.8f} {self.y:.8f}"
    def __repr__(self):
        return f"Point({self.x},{self.y})"
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)
    def __truediv__(self, scalar):
        return Point(self.x / scalar, self.y / scalar)
    def __eq__(self, other):
        return eq(self.x, other.x) and eq(self.y, other.y)
    def __abs__(self):
        return hypot(self.x, self.y)
    def __iter__(self):
        yield self.x
        yield self.y

def Rotation(vec: Point, rad):
    c, s = cos(rad), sin(rad)
    return Point(vec.x * c - vec.y * s, vec.x * s + vec.y * c)

class Circle:
    __slots__ = ("p", "r")
    def __init__(self, p: Point, r: float):
        self.p = p
        self.r = r

class Line:
    __slots__ = ("a", "b", "_dir", "arg")
    def __init__(self, a: Point, b: Point):
        self.a, self.b = a, b
        self._dir = a - b
        self.arg = self._dir.arg % pi
    def __str__(self):
        return f"[({self.a.x}, {self.a.y}) - ({self.b.x}, {self.b.y})]"
    def par(self, point):
        return Line(point, point + self._dir)
    def tan(self, point):
        return Line(point, point + Rotation(self._dir, pi/2))

class Segment(Line):
    __slots__ = ()
    def __init__(self, a, b):
        super().__init__(a, b)

def cross(u: Point, v: Point):
    return u.x * v.y - u.y * v.x

def dot(u: Point, v: Point):
    return u.x * v.x + u.y * v.y

def ccw(a, b, c):
    ab, ac = b-a, c-a
    cr = cross(ab, ac)
    if cr > EPS: return 1
    if cr < -EPS: return -1
    if dot(ac, ab) < -EPS: return 2
    if abs(ab) < abs(ac): return -2
    return 0

def projection(l: Line, p: Point):
    t = dot(l.b - l.a, p - l.a) / dot(l.b - l.a, l.b - l.a)
    return l.a + (l.b - l.a) * t

def reflection(l: Line, p: Point):
    return p + (projection(l, p) - p) * 2

def isPararell(l1: Line, l2: Line):
    return eq(cross(l1.a - l1.b, l2.a - l2.b), 0)

def isVertical(l1: Line, l2: Line):
    return eq(dot(l1.a - l1.b, l2.a - l2.b), 0)

def isIntersect_lp(l: Line, p: Point):
    return abs(ccw(l.a, l.b, p)) != 1

def isIntersect_ll(l1: Line, l2: Line):
    return not isPararell(l1, l2) or isIntersect_lp(l1, l2.a)

def isIntersect_sp(s: Segment, p: Point):
    return ccw(s.a, s.b, p) == 0

def isIntersect_ss(s1: Segment, s2: Segment):
    return ccw(s1.a, s1.b, s2.a) * ccw(s1.a, s1.b, s2.b) <= 0 and ccw(s2.a, s2.b, s1.a) * ccw(s2.a, s2.b, s1.b) <= 0

def isIntersect_ls(l: Line, s: Segment):
    return cross(l.b - l.a, s.a - l.a) * cross(l.b - l.a, s.b - l.a) < EPS

def isIntersect_cp(c: Circle, p: Point):
    return abs(abs(c.p - p) - c.r) < EPS

def isIntersect_cl(c: Circle, l: Line):
    return distance_lp(l, c.p) <= c.r + EPS

def isIntersect_cs(c: Circle, s: Segment):
    return min(distance_sp(s, c.p), distance_sp(s, c.p)) <= c.r + EPS

def intersect_cc(c1: Circle, c2: Circle):
    if c1.r < c2.r: c1, c2 = c2, c1
    d = abs(c1.p - c2.p)
    if eq(c1.r + c2.r, d): return 3  # 内接
    if eq(c1.r - c2.r, d): return 1  # 外接
    if c1.r + c2.r < d: return 4      # 離れてる
    if c1.r - c2.r < d: return 2      # 2交点
    return 0

def distance_pp(p1: Point, p2: Point):
    return abs(p1 - p2)

def distance_lp(l: Line, p: Point):
    return abs(projection(l, p) - p)

def distance_ll(l1: Line, l2: Line):
    return 0.0 if isIntersect_ll(l1, l2) else distance_lp(l1, l2.a)

def distance_sp(s: Segment, p: Point):
    r = projection(s, p)
    if isIntersect_sp(s, r): return abs(r - p)
    return min(abs(s.a - p), abs(s.b - p))

def distance_ss(s1: Segment, s2: Segment):
    if isIntersect_ss(s1, s2): return 0.0
    return min(distance_sp(s1, s2.a), distance_sp(s1, s2.b), distance_sp(s2, s1.a), distance_sp(s2, s1.b))

def distance_ls(l: Line, s: Segment):
    if isIntersect_ls(l, s): return 0.0
    return min(distance_lp(l, s.a), distance_lp(l, s.b))

def crosspoint_ll(l1: Line, l2: Line):
    A = cross(l1.b - l1.a, l2.b - l2.a)
    B = cross(l1.b - l1.a, l1.b - l2.a)
    if eq(abs(A), 0) and eq(abs(B), 0): return l2.a
    return l2.a + (l2.b - l2.a) * (B / A)

def crosspoint_ss(s1: Segment, s2: Segment):
    return crosspoint_ll(s1, s2)

def crosspoint_lc(l: Line, c: Circle):
    p = projection(l, c.p)
    d = distance_lp(l, c.p)
    if eq(d, c.r): return [p]
    unit = (l.b - l.a) / abs(l.b - l.a)
    h = (c.r**2 - d**2)**0.5
    return [p + unit * h, p - unit * h]

def crosspoint_sc(s: Segment, c: Circle):
    return [pt for pt in crosspoint_lc(s, c) if isIntersect_sp(s, pt)]

def crosspoint_cc(c1: Circle, c2: Circle):
    d = abs(c1.p - c2.p)
    if not abs(c1.r - c2.r) <= d <= c1.r + c2.r: return []
    x = (d**2 + c1.r**2 - c2.r**2) / (2 * d)
    y = (c1.r**2 - x**2)**0.5 if c1.r**2 - x**2 >= 0 else 0.0
    base = c1.p + (c2.p - c1.p) * (x / d)
    dir_ = Rotation(c2.p - c1.p, pi/2) / abs(c2.p - c1.p)
    return [base + dir_ * y, base - dir_ * y] if y > EPS else [base]

def tangent_cp(c: Circle, p: Point):
    vec = p - c.p
    q = (abs(vec)**2 - c.r**2)
    if q < -EPS: return []
    c2 = Circle(p, q**0.5 if q >= 0 else 0)
    return crosspoint_cc(c, c2)

import sys
input = sys.stdin.readline

def verify_1A():
    p1x, p1y, p2x, p2y = map(int, input().split())
    l = Line(Point(p1x, p1y), Point(p2x, p2y))
    Q = int(input())
    for _ in range(Q):
        px, py = map(int, input().split())
        print(projection(l, Point(px, py)))

def verify_1B():
    p1x, p1y, p2x, p2y = map(int, input().split())
    l = Line(Point(p1x, p1y), Point(p2x, p2y))
    Q = int(input())
    for _ in range(Q):
        px, py = map(int, input().split())
        print(reflection(l, Point(px, py)))

def verify_1C():
    p1x, p1y, p2x, p2y = map(int, input().split())
    p1, p2 = Point(p1x, p1y), Point(p2x, p2y)
    Q = int(input())
    for _ in range(Q):
        px, py = map(int, input().split())
        res = ccw(p1, p2, Point(px, py))
        print(["ON_SEGMENT", "COUNTER_CLOCKWISE", "CLOCKWISE", "ONLINE_BACK", "ONLINE_FRONT"][res])

def verify_2A():
    Q = int(input())
    for _ in range(Q):
        p0x, p0y, p1x, p1y, p2x, p2y, p3x, p3y = map(int, input().split())
        l1 = Line(Point(p0x, p0y), Point(p1x, p1y))
        l2 = Line(Point(p2x, p2y), Point(p3x, p3y))
        print(2 if isPararell(l1, l2) else 1 if isVertical(l1, l2) else 0)

def verify_2B():
    Q = int(input())
    for _ in range(Q):
        p0x, p0y, p1x, p1y, p2x, p2y, p3x, p3y = map(int, input().split())
        s1 = Segment(Point(p0x, p0y), Point(p1x, p1y))
        s2 = Segment(Point(p2x, p2y), Point(p3x, p3y))
        print(1 if isIntersect_ss(s1, s2) else 0)

def verify_2C():
    Q = int(input())
    for _ in range(Q):
        p0x, p0y, p1x, p1y, p2x, p2y, p3x, p3y = map(int, input().split())
        s1 = Segment(Point(p0x, p0y), Point(p1x, p1y))
        s2 = Segment(Point(p2x, p2y), Point(p3x, p3y))
        print(crosspoint_ss(s1, s2))

def verify_2D():
    Q = int(input())
    for _ in range(Q):
        p0x, p0y, p1x, p1y, p2x, p2y, p3x, p3y = map(int, input().split())
        s1 = Segment(Point(p0x, p0y), Point(p1x, p1y))
        s2 = Segment(Point(p2x, p2y), Point(p3x, p3y))
        print(f"{distance_ss(s1, s2):.8f}")

def verify_7A():
    c1x, c1y, c1r = map(int, input().split())
    c2x, c2y, c2r = map(int, input().split())
    print(intersect_cc(Circle(Point(c1x, c1y), c1r), Circle(Point(c2x, c2y), c2r)))

def verify_7D():
    cx, cy, cr = map(int, input().split())
    c = Circle(Point(cx, cy), cr)
    Q = int(input())
    for _ in range(Q):
        x1, y1, x2, y2 = map(int, input().split())
        pts = crosspoint_lc(Line(Point(x1, y1), Point(x2, y2)), c)
        if len(pts) == 1: pts.append(pts[-1])
        pts.sort(key=attrgetter('y'))
        pts.sort(key=attrgetter('x'))
        print(*pts)

def verify_7E():
    c1x, c1y, c1r = map(int, input().split())
    c1 = Circle(Point(c1x, c1y), c1r)
    c2x, c2y, c2r = map(int, input().split())
    c2 = Circle(Point(c2x, c2y), c2r)
    pts = crosspoint_cc(c1, c2)
    if len(pts) == 1: pts.append(pts[-1])
    pts.sort(key=attrgetter('y'))
    pts.sort(key=attrgetter('x'))
    print(*pts)

def verify_7F():
    px, py = map(int, input().split())
    cx, cy, cr = map(int, input().split())
    pts = tangent_cp(Circle(Point(cx, cy), cr), Point(px, py))
    if len(pts) == 1: pts.append(pts[-1])
    pts.sort(key=attrgetter('y'))
    pts.sort(key=attrgetter('x'))
    print(*pts, sep="\n")

verify_7F()