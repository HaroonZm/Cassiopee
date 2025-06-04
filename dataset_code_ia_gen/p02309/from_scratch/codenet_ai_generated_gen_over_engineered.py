import math
from abc import ABC, abstractmethod
from typing import Tuple, List


class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __lt__(self, other: 'Point') -> bool:
        if not isinstance(other, Point):
            return NotImplemented
        if self.x != other.x:
            return self.x < other.x
        return self.y < other.y

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return False
        return math.isclose(self.x, other.x, abs_tol=1e-9) and math.isclose(self.y, other.y, abs_tol=1e-9)

    def __repr__(self) -> str:
        return f"Point(x={self.x:.8f}, y={self.y:.8f})"


class Circle:
    __slots__ = ('center', 'radius')

    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius


class IntersectionSolver(ABC):
    @abstractmethod
    def solve(self) -> List[Point]:
        pass


class CircleCircleIntersectionSolver(IntersectionSolver):
    def __init__(self, c1: Circle, c2: Circle):
        self.c1 = c1
        self.c2 = c2

    def solve(self) -> List[Point]:
        # Let circle1 center = (x0, y0), radius = r0
        # Let circle2 center = (x1, y1), radius = r1
        x0, y0, r0 = self.c1.center.x, self.c1.center.y, self.c1.radius
        x1, y1, r1 = self.c2.center.x, self.c2.center.y, self.c2.radius

        # Compute distance between centers
        dx = x1 - x0
        dy = y1 - y0
        d = math.hypot(dx, dy)

        # According to problem constraints, centers are distinct and have at least one cross point
        # We proceed directly to intersection calculation

        # a = (r0^2 - r1^2 + d^2) / (2d)
        a = (r0**2 - r1**2 + d**2) / (2 * d)

        # h = sqrt(r0^2 - a^2)
        h_sq = r0**2 - a**2
        h_sq = max(h_sq, 0.0)  # Numerical stability
        h = math.sqrt(h_sq)

        # P2 = point along the line between centers at distance a from c1
        x2 = x0 + a * (dx / d)
        y2 = y0 + a * (dy / d)

        # Intersection points
        # x3 = x2 +- h * (dy / d)
        # y3 = y2 +- h * (-dx / d)
        rx = -dy * (h / d)
        ry = dx * (h / d)

        p1 = Point(x2 + rx, y2 + ry)
        p2 = Point(x2 - rx, y2 - ry)

        # If the two points are effectively the same (one intersection), return two identical points
        if p1 == p2:
            return [p1, p1]

        points_sorted = sorted([p1, p2])
        return points_sorted


class InputReader:
    @staticmethod
    def read_circle() -> Circle:
        tokens = input().strip().split()
        if len(tokens) != 3:
            raise ValueError("Input must consist of exactly three integers per circle line")
        x, y, r = map(int, tokens)
        return Circle(Point(float(x), float(y)), float(r))


class OutputFormatter:
    @staticmethod
    def format_points(points: List[Point]) -> str:
        # Format with 8 decimal places, separated by spaces
        return ' '.join(f"{p.x:.8f} {p.y:.8f}" for p in points)


def main():
    c1 = InputReader.read_circle()
    c2 = InputReader.read_circle()
    solver = CircleCircleIntersectionSolver(c1, c2)
    points = solver.solve()
    output = OutputFormatter.format_points(points)
    print(output)


if __name__ == "__main__":
    main()