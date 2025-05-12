#! /usr/bin/env python3

from typing import List
from math import sqrt

EPS = 1e-10

def float_equal(x: float, y: float) -> bool:
    return abs(x - y) < EPS

class Point:

    def __init__(self, x: float=0.0, y: float=0.0) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return "Point({}, {})".format(self.x, self.y)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            # print("NotImplemented in Point")
            return NotImplemented
        return float_equal(self.x, other.x) and \
            float_equal(self.y, other.y)

    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Point') -> 'Point':
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, k: float) -> 'Point':
        return Point(self.x * k, self.y * k)

    def __rmul__(self, k: float) -> 'Point':
        return self * k

    def __truediv__(self, k: float) -> 'Point':
        return Point(self.x / k, self.y / k)

    def __lt__(self, other: 'Point') -> bool:
        return self.y < other.y \
            if abs(self.x - other.x) < EPS \
            else self.x < other.x

    def norm(self):
        return self.x * self.x + self.y * self.y

    def abs(self):
        return sqrt(self.norm())

    def dot(self, other: 'Point') -> float:
        return self.x * other.x + self.y * other.y

    def cross(self, other: 'Point') -> float:
        return self.x * other.y - self.y * other.x

    def is_orthogonal(self, other: 'Point') -> bool:
        return float_equal(self.dot(other), 0.0)

    def is_parallel(self, other: 'Point') -> bool:
        return float_equal(self.cross(other), 0.0)

Vector = Point

class Segment:

    def __init__(self, p1: Point = None, p2: Point = None) -> None:
        self.p1: Point = Point() if p1 is None else p1
        self.p2: Point = Point() if p2 is None else p2

    def __repr__(self) -> str:
        return "Segment({}, {})".format(self.p1, self.p2)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Segment):
            # print("NotImplemented in Segment")
            return NotImplemented
        return self.p1 == other.p1 and self.p2 == other.p2

    def vector(self) -> Vector:
        return self.p2 - self.p1

    def is_orthogonal(self, other: 'Segment') -> bool:
        return self.vector().is_orthogonal(other.vector())

    def is_parallel(self, other: 'Segment') -> bool:
        return self.vector().is_parallel(other.vector())

    def projection(self, p: Point) -> Point:
        v = self.vector()
        vp = p - self.p1
        return v.dot(vp) / v.norm() * v + self.p1

    def reflection(self, p: Point) -> Point:
        x = self.projection(p)
        return p + 2 * (x - p)

Line = Segment

class Circle:

    def __init__(self, c: Point=None, r: float=0.0) -> None:
        self.c: Point = Point() if c is None else c
        self.r: float = r

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Circle):
            return NotImplemented
        return self.c == other.c and self.r == other.r

    def __repr__(self) -> str:
        return "Circle({}, {})".format(self.c, self.r)

def main() -> None:
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    l = Line(p1, p2)

    q = int(input())

    for _ in range(q):
        x, y = [int(x) for x in input().split()]
        p = Point(x, y)
        a = l.reflection(p)
        print(a.x, a.y)

if __name__ == "__main__":
    main()