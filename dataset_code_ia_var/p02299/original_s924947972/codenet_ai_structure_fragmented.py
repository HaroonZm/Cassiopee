import sys
from math import sqrt, atan2, acos, sin, cos
from sys import stdin

def get_input():
    return stdin.readline

def small_epsilon():
    return 1e-10

def equal_with_epsilon(a, b, eps=1e-10):
    return abs(a - b) < eps

def points_are_equal(p1, p2):
    return equal_with_epsilon(p1.x, p2.x) and equal_with_epsilon(p1.y, p2.y)

def point_norm(x, y):
    return x * x + y * y

def point_abs(x, y):
    return sqrt(point_norm(x, y))

def make_point(x=0.0, y=0.0):
    if isinstance(x, tuple):
        return Point(x[0], x[1])
    else:
        return Point(x, y)

def point_add(p1, p2):
    return Point(p1.x + p2.x, p1.y + p2.y)

def point_sub(p1, p2):
    return Point(p1.x - p2.x, p1.y - p2.y)

def point_mul(p, scalar):
    return Point(p.x * scalar, p.y * scalar)

def point_div(p, scalar):
    return Point(p.x / scalar, p.y / scalar)

def point_lt(p1, p2):
    return (p1.x, p1.y) < (p2.x, p2.y)

def point_is_zero(x):
    return abs(x) < small_epsilon()

def vector_from_points(p1, p2):
    return Vector(p2.x - p1.x, p2.y - p1.y)

def vector_dot(a, b):
    return a.x * b.x + a.y * b.y

def vector_cross(a, b):
    return a.x * b.y - a.y * b.x

def vector_is_orthogonal(a, b):
    return point_is_zero(vector_dot(a, b))

def vector_is_parallel(a, b):
    return point_is_zero(vector_cross(a, b))

def segment_vector(seg):
    return Vector(seg.p2.x - seg.p1.x, seg.p2.y - seg.p1.y)

def ccw_main(p0, p1, p):
    a = Vector(point_sub(p1, p0))
    b = Vector(point_sub(p, p0))
    if vector_cross(a, b) > small_epsilon():
        return 1
    elif vector_cross(a, b) < -small_epsilon():
        return -1
    elif vector_dot(a, b) < -small_epsilon():
        return 2
    elif point_norm(a.x, a.y) < point_norm(b.x, b.y):
        return -2
    else:
        return 0

def segment_project_point(seg, p):
    base = Vector(point_sub(seg.p2, seg.p1))
    a = Vector(point_sub(p, seg.p1))
    r = vector_dot(a, base) / point_norm(base.x, base.y)
    return point_add(seg.p1, point_mul(base, r))

def point_reflect_segment(p, s):
    proj = segment_project_point(s, p)
    delta = point_sub(proj, p)
    double_delta = point_mul(delta, 2)
    return point_add(p, double_delta)

def point_distance_to_segment(p, s):
    segvec1 = point_sub(s.p2, s.p1)
    segvec2 = point_sub(s.p1, s.p2)
    v1 = point_sub(p, s.p1)
    v2 = point_sub(p, s.p2)
    if vector_dot(Vector(segvec1), Vector(v1)) < 0.0:
        return abs(p - s.p1)
    if vector_dot(Vector(segvec2), Vector(v2)) < 0.0:
        return abs(p - s.p2)
    seg_line = point_sub(s.p2, s.p1)
    ps = point_sub(p, s.p1)
    cross = vector_cross(Vector(seg_line), Vector(ps))
    norm = point_abs(seg_line.x, seg_line.y)
    return abs(cross / norm)

def segment_intersect(s1, s2):
    ans1 = ccw_main(s1.p1, s1.p2, s2.p1) * ccw_main(s1.p1, s1.p2, s2.p2)
    ans2 = ccw_main(s2.p1, s2.p2, s1.p1) * ccw_main(s2.p1, s2.p2, s1.p2)
    return ans1 <= 0 and ans2 <= 0

def segment_cross_point(s1, s2):
    base = point_sub(s2.p2, s2.p1)
    d1 = abs(vector_cross(Vector(base), Vector(point_sub(s1.p1, s2.p1))))
    d2 = abs(vector_cross(Vector(base), Vector(point_sub(s1.p2, s2.p1))))
    t = d1 / (d1 + d2)
    diff = point_sub(s1.p2, s1.p1)
    diff_scaled = point_mul(diff, t)
    return point_add(s1.p1, diff_scaled)

def segment_distance(s1, s2):
    if segment_intersect(s1, s2):
        return 0.0
    d1 = point_distance_to_segment(s2.p1, s1)
    d2 = point_distance_to_segment(s2.p2, s1)
    d3 = point_distance_to_segment(s1.p1, s2)
    d4 = point_distance_to_segment(s1.p2, s2)
    return min(d1, d2, d3, d4)

def segment_is_orthogonal(s1, s2):
    v1 = Vector(point_sub(s1.p2, s1.p1))
    v2 = Vector(point_sub(s2.p2, s2.p1))
    return vector_is_orthogonal(v1, v2)

def segment_is_parallel(s1, s2):
    v1 = Vector(point_sub(s1.p2, s1.p1))
    v2 = Vector(point_sub(s2.p2, s2.p1))
    return vector_is_parallel(v1, v2)

def circle_line_cross_points(circle, seg):
    pr = segment_project_point(seg, circle.c)
    e = point_div(point_sub(seg.p2, seg.p1), point_abs(*(point_sub(seg.p2, seg.p1))))
    base = sqrt(circle.r * circle.r - point_norm(pr.x - circle.c.x, pr.y - circle.c.y))
    first = point_add(pr, point_mul(e, base))
    second = point_sub(pr, point_mul(e, base))
    return first, second

def circle_circle_cross_points(c1, c2):
    d = point_abs(c2.c.x - c1.c.x, c2.c.y - c1.c.y)
    a = acos((c1.r * c1.r + d * d - c2.r * c2.r) / (2 * c1.r * d))
    t = atan2(c2.c.y - c1.c.y, c2.c.x - c1.c.x)
    temp1 = Point(cos(t + a) * c1.r, sin(t + a) * c1.r)
    temp2 = Point(cos(t - a) * c1.r, sin(t - a) * c1.r)
    return point_add(c1.c, temp1), point_add(c1.c, temp2)

def contains(polygon, p):
    n = len(polygon)
    x = False
    for i in range(n):
        a = point_sub(polygon[i], p)
        b = point_sub(polygon[(i + 1) % n], p)
        if abs(vector_cross(Vector(a), Vector(b))) < small_epsilon() and vector_dot(Vector(a), Vector(b)) < small_epsilon():
            return 1
        if a.y > b.y:
            a, b = b, a
        if a.y < small_epsilon() and small_epsilon() < b.y and vector_cross(Vector(a), Vector(b)) > small_epsilon():
            x = not x
    return 2 if x else 0

class Point(object):
    epsilon = 1e-10
    def __init__(self, x=0.0, y=0.0):
        if isinstance(x, tuple):
            self.x = x[0]
            self.y = x[1]
        else:
            self.x = x
            self.y = y
    def __add__(self, other):
        return point_add(self, other)
    def __sub__(self, other):
        return point_sub(self, other)
    def __mul__(self, other):
        return point_mul(self, other)
    def __truediv__(self, other):
        return point_div(self, other)
    def __lt__(self, other):
        return point_lt(self, other)
    def __eq__(self, other):
        return points_are_equal(self, other)
    def norm(self):
        return point_norm(self.x, self.y)
    def __abs__(self):
        return point_abs(self.x, self.y)
    def ccw(self, p0, p1):
        return ccw_main(p0, p1, self)
    def project(self, s):
        return segment_project_point(s, self)
    def reflect(self, s):
        return point_reflect_segment(self, s)
    def distance(self, s):
        return point_distance_to_segment(self, s)

class Vector(Point):
    def __init__(self, x=0.0, y=0.0):
        if isinstance(x, tuple):
            self.x = x[0]
            self.y = x[1]
        elif isinstance(x, Point):
            self.x = x.x
            self.y = x.y
        else:
            self.x = x
            self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return Vector(other * self.x, other * self.y)
    def __truediv__(self, other):
        return Vector(self.x / other, self.y / other)
    @classmethod
    def dot(cls, a, b):
        return vector_dot(a, b)
    @classmethod
    def cross(cls, a, b):
        return vector_cross(a, b)
    @classmethod
    def is_orthogonal(cls, a, b):
        return vector_is_orthogonal(a, b)
    @classmethod
    def is_parallel(cls, a, b):
        return vector_is_parallel(a, b)

class Segment(object):
    def __init__(self, p1=Point(), p2=Point()):
        if isinstance(p1, Point):
            self.p1 = p1
            self.p2 = p2
        elif isinstance(p1, tuple):
            self.p1 = Point(p1[0], p1[1])
            self.p2 = Point(p2[0], p2[1])
    def intersect(self, s):
        return segment_intersect(self, s)
    def cross_point(self, s):
        return segment_cross_point(self, s)
    def distance(self, s):
        return segment_distance(self, s)
    @classmethod
    def is_orthogonal(cls, s1, s2):
        return segment_is_orthogonal(s1, s2)
    @classmethod
    def is_parallel(cls, s1, s2):
        return segment_is_parallel(s1, s2)

class Line(Segment):
    pass

class Cirle(object):
    def __init__(self, x, y=Point(), r=1.0):
        if isinstance(x, Point):
            self.c = x
            self.r = y
        elif isinstance(x, tuple):
            self.c = Point(x[0], x[1])
            self.r = r
    def cross_points(self, s):
        if isinstance(s, Segment):
            return circle_line_cross_points(self, s)
        elif isinstance(s, Cirle):
            return circle_circle_cross_points(self, s)

def read_int():
    return int(get_input()())

def read_point():
    x, y = map(int, get_input()().split())
    return Point(x, y)

def read_polygon(n):
    return [read_point() for _ in range(n)]

def handle_query(polygon):
    x, y = map(int, get_input()().split())
    p = Point(x, y)
    result = contains(polygon, p)
    print(result)

def process_queries(polygon, q):
    for _ in range(q):
        handle_query(polygon)

def main(args):
    n = read_int()
    polygon = read_polygon(n)
    q = read_int()
    process_queries(polygon, q)

if __name__ == '__main__':
    main(sys.argv[1:])