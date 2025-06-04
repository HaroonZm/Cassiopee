import math

EPS = 1e-10

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, a):
        return Point(self.x * a, self.y * a)

    def __truediv__(self, a):
        return Point(self.x / a, self.y / a)

    def __str__(self):
        return str(self.x) + ',' + str(self.y)

    def __repr__(self):
        return 'Point(' + str(self.x) + ',' + str(self.y) + ')'

    def __lt__(self, other):
        if self.y == other.y:
            return self.x < other.x
        else:
            return self.y < other.y

    def __eq__(self, other):
        return abs(self.x - other.x) < EPS and abs(self.y - other.y) < EPS

class Segment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return 'segment:(' + str(self.p1) + ';' + str(self.p2) + ')'

    def __repr__(self):
        return 'segment:(' + str(self.p1) + ';' + str(self.p2) + ')'

def norm(p):
    return p.x * p.x + p.y * p.y

def length(p):
    return math.sqrt(p.x * p.x + p.y * p.y)

def dot(a, b):
    return a.x * b.x + a.y * b.y

def cross(a, b):
    return a.x * b.y - a.y * b.x

def project(seg, p):
    base = seg.p2 - seg.p1
    r = dot(p - seg.p1, base) / norm(base)
    return seg.p1 + base * r

def reflect(seg, p):
    tmp = project(seg, p) - p
    return p + tmp * 2.0

s = [int(x) for x in input().split()]
p1 = Point(s[0], s[1])
p2 = Point(s[2], s[3])
seg = Segment(p1, p2)
q = int(input())
for i in range(q):
    s = [int(x) for x in input().split()]
    p = Point(s[0], s[1])
    refl = reflect(seg, p)
    print(refl.x, refl.y)