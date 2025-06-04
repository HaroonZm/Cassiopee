import math

EPS = 1e-10

def float_equal(x, y):
    return abs(x - y) < EPS

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)

    def __eq__(self, other):
        return float_equal(self.x, other.x) and float_equal(self.y, other.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, k):
        return Point(self.x * k, self.y * k)

    def __rmul__(self, k):
        return self.__mul__(k)

    def __truediv__(self, k):
        return Point(self.x / k, self.y / k)

    def norm(self):
        return self.x * self.x + self.y * self.y

    def abs(self):
        return math.sqrt(self.norm())

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def is_orthogonal(self, other):
        return float_equal(self.dot(other), 0.0)

    def is_parallel(self, other):
        return float_equal(self.cross(other), 0.0)

Vector = Point

class Segment:
    def __init__(self, p1=None, p2=None):
        if p1 is None:
            self.p1 = Point()
        else:
            self.p1 = p1
        if p2 is None:
            self.p2 = Point()
        else:
            self.p2 = p2

    def __repr__(self):
        return "Segment({}, {})".format(self.p1, self.p2)

    def __eq__(self, other):
        return self.p1 == other.p1 and self.p2 == other.p2

    def vector(self):
        return self.p2 - self.p1

    def is_orthogonal(self, other):
        return self.vector().is_orthogonal(other.vector())

    def is_parallel(self, other):
        return self.vector().is_parallel(other.vector())

    def projection(self, p):
        v = self.vector()
        vp = p - self.p1
        t = v.dot(vp) / v.norm()
        proj = v * t + self.p1
        return proj

    def reflection(self, p):
        proj = self.projection(p)
        v = proj - p
        return p + v * 2

Line = Segment

class Circle:
    def __init__(self, c=None, r=0.0):
        if c is None:
            self.c = Point()
        else:
            self.c = c
        self.r = r

    def __eq__(self, other):
        return self.c == other.c and self.r == other.r

    def __repr__(self):
        return "Circle({}, {})".format(self.c, self.r)

def main():
    data = input().split()
    x1 = int(data[0])
    y1 = int(data[1])
    x2 = int(data[2])
    y2 = int(data[3])
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    l = Line(p1, p2)
    q = int(input())
    for _ in range(q):
        xy = input().split()
        x = int(xy[0])
        y = int(xy[1])
        p = Point(x, y)
        a = l.reflection(p)
        print(a.x, a.y)

if __name__ == "__main__":
    main()