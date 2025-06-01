from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import Optional, Tuple, List, Iterator
import sys


class Fortune(Enum):
    DAI_KICHI = "dai-kichi"
    CHU_KICHI = "chu-kichi"
    KICHI = "kichi"
    SYO_KICHI = "syo-kichi"
    KYO = "kyo"

    @staticmethod
    def from_area(area: Optional[float]) -> Fortune:
        if area is None:
            return Fortune.KYO
        if area >= 1_900_000:
            return Fortune.DAI_KICHI
        if area >= 1_000_000:
            return Fortune.CHU_KICHI
        if area >= 100_000:
            return Fortune.KICHI
        if area > 0:
            return Fortune.SYO_KICHI
        return Fortune.KYO


@dataclass(frozen=True)
class Point:
    x: float
    y: float

    def __sub__(self, other: Point) -> Point:
        return Point(self.x - other.x, self.y - other.y)

    def cross(self, other: Point) -> float:
        return self.x * other.y - self.y * other.x


@dataclass(frozen=True)
class LineSegment:
    start: Point
    end: Point

    def direction(self) -> Point:
        return self.end - self.start


class GeometryError(Exception):
    pass


class IntersectionCalculator:
    """Calculates intersection points between line segments with high abstraction."""

    @staticmethod
    def _is_point_on_segment(p: Point, seg: LineSegment) -> bool:
        min_x = min(seg.start.x, seg.end.x)
        max_x = max(seg.start.x, seg.end.x)
        min_y = min(seg.start.y, seg.end.y)
        max_y = max(seg.start.y, seg.end.y)
        # Check bounding box first
        if not (min_x - 1e-9 <= p.x <= max_x + 1e-9 and min_y - 1e-9 <= p.y <= max_y + 1e-9):
            return False
        # Check colinearity by cross product
        d1 = seg.end - seg.start
        d2 = p - seg.start
        cross = d1.cross(d2)
        return abs(cross) < 1e-9

    @staticmethod
    def line_line_intersection(seg1: LineSegment, seg2: LineSegment) -> Optional[Point]:
        """Return the intersection point of two line segments if it exists and lies on both segments."""
        p = seg1.start
        r = seg1.direction()
        q = seg2.start
        s = seg2.direction()

        r_cross_s = r.cross(s)
        if abs(r_cross_s) < 1e-14:
            # Lines are parallel or colinear
            # Check if colinear
            pq = q - p
            if abs(pq.cross(r)) < 1e-14:
                # They are colinear: no single intersection point, but infinite or none
                return None
            else:
                return None  # parallel, no intersection

        t = (q - p).cross(s) / r_cross_s
        u = (q - p).cross(r) / r_cross_s

        if 0 - 1e-14 <= t <= 1 + 1e-14 and 0 - 1e-14 <= u <= 1 + 1e-14:
            inter_point = Point(p.x + t * r.x, p.y + t * r.y)
            # Safety: double check points on segment
            if IntersectionCalculator._is_point_on_segment(inter_point, seg1) and IntersectionCalculator._is_point_on_segment(inter_point, seg2):
                return inter_point
        return None


@dataclass(frozen=True)
class Triangle:
    p1: Point
    p2: Point
    p3: Point

    def area(self) -> float:
        # Using cross product formula for 2D polygon area (triangle here)
        return abs((self.p2 - self.p1).cross(self.p3 - self.p1)) / 2


class OmikujiSolver:
    """Solver class encapsulating the problem."""

    def __init__(self, segments: List[LineSegment]) -> None:
        if len(segments) != 3:
            raise GeometryError("Exactly three line segments are required")
        self.segments = segments
        self.intersections: List[Optional[Point]] = []

    def compute_intersections(self) -> Optional[List[Point]]:
        # Find intersections of the 3 lines taken pairwise
        points = []
        pairs = [(0, 1), (1, 2), (2, 0)]
        for i, j in pairs:
            inter = IntersectionCalculator.line_line_intersection(self.segments[i], self.segments[j])
            if inter is None:
                # No intersection found - no triangle
                return None
            points.append(inter)

        # Check if any two intersections are effectively the same point
        # Also check if all three points coincide (one-point intersection)
        # or if any two points coincide => no triangle
        tol = 1e-9
        def points_equal(a: Point, b: Point) -> bool:
            return abs(a.x - b.x) < tol and abs(a.y - b.y) < tol

        # Check pairwise distinctness
        if points_equal(points[0], points[1]) or points_equal(points[1], points[2]) or points_equal(points[2], points[0]):
            return None  # Not a proper triangle

        return points

    def solve(self) -> Fortune:
        points = self.compute_intersections()
        if points is None:
            return Fortune.KYO
        triangle = Triangle(points[0], points[1], points[2])
        area = triangle.area()
        if area < 1e-9:
            # Area zero means no triangle
            return Fortune.KYO
        return Fortune.from_area(area)


class OmikujiInputParser:
    def __init__(self, input_stream: Iterator[str]) -> None:
        self.input_stream = input_stream

    def __iter__(self) -> Iterator[List[LineSegment]]:
        while True:
            lines = []
            try:
                for _ in range(3):
                    line = next(self.input_stream)
                    if line.strip() == "":
                        raise StopIteration
                    lines.append(line)
            except StopIteration:
                return
            if all(line.strip() == "0 0 0 0" for line in lines):
                return
            segments = []
            for line in lines:
                x1, y1, x2, y2 = map(int, line.strip().split())
                segments.append(LineSegment(Point(x1, y1), Point(x2, y2)))
            yield segments


def main() -> None:
    parser = OmikujiInputParser(iter(sys.stdin.readline, ""))
    for segments in parser:
        solver = OmikujiSolver(segments)
        fortune = solver.solve()
        print(fortune.value)


if __name__ == "__main__":
    main()