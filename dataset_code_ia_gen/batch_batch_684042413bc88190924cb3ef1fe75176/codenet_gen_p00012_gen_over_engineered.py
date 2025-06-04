from abc import ABC, abstractmethod
import sys
from typing import List, Tuple


class Point:
    __slots__ = ['_x', '_y']

    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    def __sub__(self, other: 'Point') -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Vector:
    __slots__ = ['_dx', '_dy']

    def __init__(self, dx: float, dy: float):
        self._dx = dx
        self._dy = dy

    @property
    def dx(self) -> float:
        return self._dx

    @property
    def dy(self) -> float:
        return self._dy

    def cross(self, other: 'Vector') -> float:
        return self.dx * other.dy - self.dy * other.dx

    def __repr__(self):
        return f"Vector({self.dx}, {self.dy})"


class Shape(ABC):
    @abstractmethod
    def contains(self, point: Point) -> bool:
        pass


class Triangle(Shape):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self._p1 = p1
        self._p2 = p2
        self._p3 = p3
        self._validate_triangle()

    def _validate_triangle(self):
        # Check side lengths >= 1.0 according to constraints
        def dist(a: Point, b: Point) -> float:
            return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5
        sides = [dist(self._p1, self._p2), dist(self._p2, self._p3), dist(self._p3, self._p1)]
        if any(side < 1.0 for side in sides):
            raise ValueError("Triangle side length less than 1.0")
        # Additional check for collinearity (area zero)
        if abs(self.area()) < 0.000001:
            raise ValueError("Points are collinear, no valid triangle")

    def area(self) -> float:
        # Using cross product for the parallelogram area and dividing by 2
        v1 = self._p2 - self._p1
        v2 = self._p3 - self._p1
        return abs(v1.cross(v2)) / 2.0

    def contains(self, point: Point) -> bool:
        # Barycentric coordinate method with floating tolerance
        v0 = self._p3 - self._p1
        v1 = self._p2 - self._p1
        v2 = point - self._p1

        dot00 = v0.dx * v0.dx + v0.dy * v0.dy
        dot01 = v0.dx * v1.dx + v0.dy * v1.dy
        dot02 = v0.dx * v2.dx + v0.dy * v2.dy
        dot11 = v1.dx * v1.dx + v1.dy * v1.dy
        dot12 = v1.dx * v2.dx + v1.dy * v2.dy

        denom = dot00 * dot11 - dot01 * dot01
        if abs(denom) < 1e-15:
            # Degenerate triangle
            return False

        invDenom = 1 / denom
        u = (dot11 * dot02 - dot01 * dot12) * invDenom
        v = (dot00 * dot12 - dot01 * dot02) * invDenom

        # point is in triangle if u,v >=0 and u+v <=1 with tolerance
        tolerance = 1e-9
        in_triangle = (u >= -tolerance) and (v >= -tolerance) and (u + v <= 1 + tolerance)
        if not in_triangle:
            return False

        # Additional distance from sides check: ensure distance >= 0.001 if inside
        dists = self._distances_to_sides(point)
        if any(d < 0.001 for d in dists):
            # According to problem constraints distance >=0.001 to each side if point inside
            # So points too close to side considered outside
            return False
        return True

    def _distances_to_sides(self, pt: Point) -> List[float]:
        # Distance from point to line segment using vector projection
        def distance_point_to_segment(p: Point, a: Point, b: Point) -> float:
            ap = p - a
            ab = b - a
            ab2 = ab.dx * ab.dx + ab.dy * ab.dy
            if ab2 == 0:
                return ((p.x - a.x) ** 2 + (p.y - a.y) ** 2) ** 0.5
            t = max(0.0, min(1.0, (ap.dx * ab.dx + ap.dy * ab.dy) / ab2))
            projx = a.x + t * ab.dx
            projy = a.y + t * ab.dy
            return ((p.x - projx) ** 2 + (p.y - projy) ** 2) ** 0.5

        return [distance_point_to_segment(pt, self._p1, self._p2),
                distance_point_to_segment(pt, self._p2, self._p3),
                distance_point_to_segment(pt, self._p3, self._p1)]


class DataSetParser:
    def __init__(self, lines: List[str]):
        self._lines = lines

    def parse(self) -> List[Tuple[Triangle, Point]]:
        data = []
        for line in self._lines:
            if line.strip() == '':
                continue
            parts = line.strip().split()
            if len(parts) != 8:
                continue  # or raise error
            nums = list(map(float, parts))
            p1 = Point(nums[0], nums[1])
            p2 = Point(nums[2], nums[3])
            p3 = Point(nums[4], nums[5])
            pt = Point(nums[6], nums[7])
            try:
                triangle = Triangle(p1, p2, p3)
            except ValueError:
                # Invalid triangle, skip or handle gracefully
                continue
            data.append((triangle, pt))
        return data


class PointInTriangleProcessor:
    def __init__(self, datasets: List[Tuple[Triangle, Point]]):
        self._datasets = datasets

    def process(self) -> List[str]:
        results = []
        for triangle, point in self._datasets:
            result = "YES" if triangle.contains(point) else "NO"
            results.append(result)
        return results


def main():
    input_lines = sys.stdin.read().strip().split('\n')
    parser = DataSetParser(input_lines)
    datasets = parser.parse()
    processor = PointInTriangleProcessor(datasets)
    results = processor.process()
    for res in results:
        print(res)


if __name__ == '__main__':
    main()