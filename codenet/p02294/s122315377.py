#! /usr/bin/env python3

from typing import List, Tuple
from math import sqrt
from enum import IntEnum

EPS = 1e-10

def float_equal(x: float, y: float) -> bool:
    return abs(x - y) < EPS

class PointLocation(IntEnum):
    COUNTER_CLOCKWISE = 1
    CCW = 1
    CLOCKWISE = -1
    CW = -1
    ONLINE_BACK = 2
    O_B = 2
    ONLINE_FRONT = -2
    O_F = -2
    ON_SEGMENT = 0
    O_S = 0

PL = PointLocation

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

    def distance(self, other: 'Point') -> float:
        return (self - other).abs()

    def in_side_of(self, seg: 'Segment') -> bool:
        return seg.vector().dot(
            Segment(seg.p1, self).vector()) >= 0

    def in_width_of(self, seg: 'Segment') -> bool:
        return \
            self.in_side_of(seg) and \
            self.in_side_of(seg.reverse())

    def distance_to_line(self, seg: 'Segment') -> float:
        return \
            abs((self - seg.p1).cross(seg.vector())) / \
            seg.length()

    def distance_to_segment(self, seg: 'Segment') -> float:
        if not self.in_side_of(seg):
            return self.distance(seg.p1)
        if not self.in_side_of(seg.reverse()):
            return self.distance(seg.p2)
        else:
            return self.distance_to_line(seg)

    def location(self, seg: 'Segment') -> PointLocation:
        p = self - seg.p1
        d = seg.vector().cross(p)
        if d > EPS:
            return PointLocation.COUNTER_CLOCKWISE
        if d < -EPS:
            return PointLocation.CLOCKWISE
        if seg.vector().dot(p) < 0.0:
            return PointLocation.ONLINE_BACK
        if seg.vector().norm() < p.norm():
            return PointLocation.ONLINE_FRONT
        return PointLocation.ON_SEGMENT

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

    def reverse(self) -> 'Segment':
        return Segment(self.p2, self.p1)

    def length(self) -> float:
        return self.p1.distance(self.p2)

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

    def intersect_ratio(self, other: 'Segment') -> Tuple[float, float]:
        a = self.vector()
        b = other.vector()
        c = self.p1 - other.p1
        s = b.cross(c) / a.cross(b)
        t = a.cross(c) / a.cross(b)
        return s, t

    def intersects(self, other: 'Segment') -> bool:
        d0 = self.p1.location(other)
        d1 = self.p2.location(other)
        d2 = other.p1.location(self)
        d3 = other.p2.location(self)
        return d0 * d1 * d2 * d3 == 0 or \
            (d0 * d1 == -1 and d2 * d3 == -1)

    def intersection(self, other: 'Segment') -> Point:
        s, _ = self.intersect_ratio(other)
        return self.p1 + s * self.vector()

    def distance_with_segment(self, other: 'Segment') -> float:
        if not self.is_parallel(other) and \
                self.intersects(other):
            return 0
        else:
            return min(
                self.p1.distance_to_segment(other),
                self.p2.distance_to_segment(other),
                other.p1.distance_to_segment(self),
                other.p2.distance_to_segment(self))

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
    q = int(input())

    for _ in range(q):
        x0, y0, x1, y1, x2, y2, x3, y3 = \
            [int(x) for x in input().split()]
        s1 = Segment(Point(x0, y0), Point(x1, y1))
        s2 = Segment(Point(x2, y2), Point(x3, y3))
        print(1 if s1.intersects(s2) else 0)

if __name__ == "__main__":
    main()