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
            return NotImplemented
        return float_equal(self.x, other.x) and float_equal(self.y, other.y)
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
        return self.y < other.y if abs(self.x - other.x) < EPS else self.x < other.x
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
            return NotImplemented
        return self.p1 == other.p1 and self.p2 == other.p2
    def vector(self):
        return self.p2 - self.p1
    def is_orthogonal(self, other: 'Segment') -> bool:
        return self.vector().is_orthogonal(other.vector())
    def is_parallel(self, other: 'Segment') -> bool:
        return self.vector().is_parallel(other.vector())

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

def classify(s1: Segment, s2: Segment) -> int:
    if s1.is_parallel(s2):
        return 2
    elif s1.is_orthogonal(s2):
        return 1
    else:
        return 0

def main() -> None:
    q = int(input())
    for _ in range(q):
        s1, s2 = Segment(), Segment()
        s1.p1.x, s1.p1.y, s1.p2.x, s1.p2.y, s2.p1.x, s2.p1.y, s2.p2.x, s2.p2.y = [int(x) for x in input().split()]
        print(classify(s1, s2))

if __name__ == "__main__":
    main()