from math import sin, cos, atan2

def sgn(x, eps=1e-10):
    if x < -eps:
        return -1
    if -eps <= x <= eps:
        return 0
    if x > eps:
        return 1

class Vector:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def arg(self):
        return atan2(self.y, self.x)

    def norm(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def rotate(self, t):
        nx = self.x * cos(t) - self.y * sin(t)
        ny = self.x * sin(t) + self.y * cos(t)
        return Vector(nx, ny)

    def counter(self):
        return Vector(-self.x, -self.y)

    def times(self, k):
        return Vector(self.x * k, self.y * k)

    def unit(self):
        length = self.norm()
        return Vector(self.x / length, self.y / length)

    def normal(self):
        length = self.norm()
        return Vector(-self.y / length, self.x / length)

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def sub(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def __str__(self):
        return "{:.9f} {:.9f}".format(self.x, self.y)

class Line:
    def __init__(self, bgn=None, end=None):
        if bgn is None:
            bgn = Vector()
        if end is None:
            end = Vector()
        self.bgn = bgn
        self.end = end

    def build(self, a, b, c):
        if sgn(a) != 0 or sgn(b) != 0:
            if sgn(b) == 0:
                self.bgn = Vector(-c / a, 0.0)
                self.end = Vector(-c / a, 1.0)
            else:
                self.v = Vector(0.0, -c / b)
                self.u = Vector(1.0, -(a + b) / b)

    def vec(self):
        return self.end.sub(self.bgn)

    def projection(self, point):
        v = self.vec()
        u = point.sub(self.bgn)
        k = v.dot(u) / v.norm()
        h = v.unit().times(k)
        return self.bgn.add(h)

    def refrection(self, point):
        proj = self.projection(point)
        diff = proj.sub(point)
        twice = diff.times(2)
        return twice.add(point)

xp1, yp1, xp2, yp2 = map(int, input().split())
q = int(input())
p1 = Vector(xp1, yp1)
p2 = Vector(xp2, yp2)
l = Line(p1, p2)

for i in range(q):
    x, y = map(int, input().split())
    p = Vector(x, y)
    ref = l.refrection(p)
    print(ref)