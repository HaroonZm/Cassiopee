import math

EPS = 1e-10

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __mul__(self, a):  # a: scalar
        return Point(self.x * a, self.y * a)

    def __truediv__(self, a):  # a: scalar
        return Point(self.x / a, self.y / a)

    def __str__(self):
        return str(self.x) + ',' + str(self.y)

    def __repr__(self):
        return 'Point(' + str(self.x) + ',' + str(self.y) + ')'

    def __lt__(self, other):
        if self.y - other.y == 0:
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

class Circle:
    def __init__(self, c, r):
        self.c = c
        self.r = r

    def __str__(self):
        return 'Circle:(center point: ' + str(self.c) + '; radius: ' + str(self.r) + ')'

    def __repr__(self):
        return 'Circle:(center point: ' + str(self.c) + '; radius: ' + str(self.r) + ')'

class Polygon:
    def __init__(self, ps = []):
        self.ps = ps
        self.size = len(ps)

    def __getitem__(self, i):
        return self.ps[i]

    def __setitem__(self, i, p):
        self.ps[i] = p

    def __iter__(self):
        return iter(self.ps)

    def addpoint(self, i, p):
        self.ps.insert(i, p)
        self.size += 1

    def delpoint(self, i):
        self.size -= 1
        return self.ps.pop(i)

    def sortYX(self):
        self.ps.sort()

    def __str__(self):
        return 'Polygon:' + str(tuple(self.ps))

    def __repr__(self):
        return 'Polygon:' + str(tuple(self.ps))

    def __len__(self):
        return len(self.ps)

    def __eq__(self, other):
        return self.ps == other.ps

    def draw(self):
        import turtle
        turtle.screensize(800, 800, "black")
        turtle.title("Polygon convex hull")
        turtle.setworldcoordinates(-400, -400, 400, 400)
        t = turtle.Turtle()
        t.pencolor("red")
        for pt in self.ps:
            t.goto(pt.x, pt.y)
            t.dot(10, 'white')

def norm(p):
    return p.x * p.x + p.y * p.y

def length(p):
    return math.sqrt(p.x * p.x + p.y * p.y)

def dot(a, b):
    return a.x * b.x + a.y * b.y

def cross(a, b):
    return a.x * b.y - a.y * b.x

def project(s, p):
    base = s.p2 - s.p1
    r = dot(p - s.p1, base) / norm(base)
    return s.p1 + base * r

def getDistance(a, b):
    return length(a - b)

def getDistanceLP(l, p):
    return abs(cross(l.p2 - l.p1, p - l.p1) / length(l.p2 - l.p1))

def getDistanceSP(s, p):
    if dot(s.p2 - s.p1, p - s.p1) < 0.0:
        return length(p - s.p1)
    if dot(s.p1 - s.p2, p - s.p2) < 0.0:
        return length(p - s.p2)
    return getDistanceLP(s, p)

def isOrthogonalSG(s1, s2):
    return abs(dot(s1.p2 - s1.p1, s2.p2 - s2.p1)) < EPS

def isParallelLN(s1, s2):
    return abs(cross(s1.p2 - s1.p1, s2.p2 - s2.p1)) < 0

COUNTER_CLOCKWISE = 1
CLOCKWISE = -1
ONLINE_BACK = -2
ONLINE_FRONT = 2
ON_SEGMENT = 0

def ccw(p0, p1, p2):
    a = p1 - p0
    b = p2 - p0
    if cross(a, b) > EPS:
        return COUNTER_CLOCKWISE
    if cross(a, b) < -EPS:
        return CLOCKWISE
    if dot(a, b) < -EPS:
        return ONLINE_BACK
    if norm(a) < norm(b):
        return ONLINE_FRONT
    return ON_SEGMENT

def toleft(p0, p1, p2):
    a = p1 - p0
    b = p2 - p0
    tmp = cross(a, b)
    if tmp > EPS:
        return 1
    elif abs(tmp) < EPS and norm(a) <= norm(b):
        return 2
    elif abs(tmp) < EPS and norm(a) > norm(b):
        return -2
    else:
        return -1

def reflect(s, p):
    return p + (project(s, p) - p) * 2.0

def intersectSG(s1, s2):
    return intersectP4(s1.p1, s1.p2, s2.p1, s2.p2)

def getDistanceSG(s1, s2):
    if intersectSG(s1, s2):
        return 0.0
    return min(
        getDistanceSP(s1, s2.p1),
        getDistanceSP(s1, s2.p2),
        getDistanceSP(s2, s1.p1),
        getDistanceSP(s2, s1.p2)
    )

def intersectP4(p1, p2, p3, p4):
    return ccw(p1, p2, p3) * ccw(p1, p2, p4) <= 0 and \
           ccw(p3, p4, p1) * ccw(p3, p4, p2) <= 0

q = int(input())
for i in range(q):
    s = [int(x) for x in input().split()]
    p0 = Point(s[0], s[1])
    p1 = Point(s[2], s[3])
    p2 = Point(s[4], s[5])
    p3 = Point(s[6], s[7])

    if p0 == p2 or p0 == p3 or p1 == p2 or p1 == p3:
        print(1)
    elif cross(p1 - p0, p2 - p0) * cross(p1 - p0, p3 - p0) < 0 and \
         cross(p3 - p2, p0 - p2) * cross(p3 - p2, p1 - p2) < 0:
        print(1)
    elif cross(p1 - p0, p2 - p0) == 0 and dot(p1 - p0, p2 - p0) > 0 and \
         length(p2 - p0) < length(p1 - p0):
        print(1)
    elif cross(p1 - p0, p3 - p0) == 0 and dot(p1 - p0, p3 - p0) > 0 and \
         length(p3 - p0) < length(p1 - p0):
        print(1)
    elif cross(p3 - p2, p0 - p2) == 0 and dot(p3 - p2, p0 - p2) > 0 and \
         length(p0 - p2) < length(p3 - p2):
        print(1)
    elif cross(p3 - p2, p1 - p2) == 0 and dot(p3 - p2, p1 - p2) > 0 and \
         length(p1 - p2) < length(p3 - p2):
        print(1)
    else:
        print(0)