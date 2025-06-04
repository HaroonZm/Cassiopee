import sys
import math
from typing import List, Tuple, Optional, Iterable, Iterator

class Point:
    __slots__ = ('x', 'y')
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def distance_to(self, other: 'Point') -> float:
        return math.hypot(self.x - other.x, self.y - other.y)

    def distance_to_squared(self, other: 'Point') -> float:
        dx = self.x - other.x
        dy = self.y - other.y
        return dx*dx + dy*dy

    def __repr__(self) -> str:
        return f"Point({self.x:.5f},{self.y:.5f})"

class Circle:
    __slots__ = ('center', 'radius')
    def __init__(self, center: Point, radius: float) -> None:
        self.center = center
        self.radius = radius

    def contains_point(self, p: Point) -> bool:
        # inclusive: on the circle is inside
        return self.center.distance_to_squared(p) <= self.radius * self.radius + 1e-12

    def count_points_inside(self, points: Iterable[Point]) -> int:
        return sum(1 for p in points if self.contains_point(p))

    def __repr__(self) -> str:
        return f"Circle(center={self.center}, radius={self.radius})"

class CircleFinder:
    RADIUS = 1.0
    RADIUS_SQ = RADIUS*RADIUS
    EPSILON = 1e-10

    def __init__(self, points: List[Point]) -> None:
        self.points = points

    @staticmethod
    def circle_from_two_points(p1: Point, p2: Point, radius: float) -> List[Circle]:
        d_sq = p1.distance_to_squared(p2)
        d = math.sqrt(d_sq)
        if d > 2*radius + 1e-9:
            return []
        # midpoint between p1,p2
        mx = (p1.x + p2.x)/2
        my = (p1.y + p2.y)/2
        # distance from midpoint to center(s)
        h = math.sqrt(radius*radius - (d/2)**2)
        # direction vector perpendicular to p1->p2 normalized
        dx = (p2.x - p1.x)/d
        dy = (p2.y - p1.y)/d
        # two possible centers
        c1 = Point(mx - dy*h, my + dx*h)
        c2 = Point(mx + dy*h, my - dx*h)
        return [Circle(c1, radius), Circle(c2, radius)]

    def max_enclosed_points(self) -> int:
        n = len(self.points)
        if n == 1:
            return 1
        # The best count found so far
        best = 1

        # Compute max points for all circles with center at some point
        # i.e. circle centered on the point itself (covers that point at least)
        for p_base in self.points:
            count = sum(1 for p in self.points if p_base.distance_to(p) <= self.RADIUS + 1e-12)
            if count > best:
                best = count

        # Compute max points for all circles defined by pairs of points (the two points on circumference)
        # Because radius is fixed at 1, there can be 0,1 or 2 circles passing by two points.
        for i in range(n):
            for j in range(i+1,n):
                circles = self.circle_from_two_points(self.points[i], self.points[j], self.RADIUS)
                for circle in circles:
                    count = circle.count_points_inside(self.points)
                    if count > best:
                        best = count
        return best

class DataSetParser:
    def __init__(self, input_lines: Iterator[str]) -> None:
        self.lines = input_lines

    def __iter__(self) -> Iterator[List[Point]]:
        while True:
            try:
                line = next(self.lines).strip()
            except StopIteration:
                break
            if line == '0':
                break
            if not line:
                continue
            n = int(line)
            pts = []
            for _ in range(n):
                line = next(self.lines).strip()
                x_str, y_str = line.split()
                pts.append(Point(float(x_str), float(y_str)))
            yield pts

def main() -> None:
    parser = DataSetParser(iter(sys.stdin))
    for points in parser:
        finder = CircleFinder(points)
        print(finder.max_enclosed_points())

if __name__ == '__main__':
    main()