import sys
from typing import List, Tuple, Protocol
from abc import abstractmethod
import math

class Point:
    __slots__ = ('x', 'y')
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    def __sub__(self, other: 'Point') -> 'Point':
        return Point(self.x - other.x, self.y - other.y)
    def cross(self, other: 'Point') -> float:
        return self.x * other.y - self.y * other.x
    def __repr__(self):
        return f"Point({self.x},{self.y})"

class Line:
    __slots__ = ('p1', 'p2', 'dir')
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
        self.dir = p2 - p1
    def on_left(self, p: Point) -> bool:
        return (self.dir.cross(p - self.p1)) > -1e-15  # include points on the line as inside
    def intersection(self, a: Point, b: Point) -> Point:
        # Compute intersection of segment ab with line p1p2
        A = b - a
        B = self.p2 - self.p1
        denom = B.cross(A)
        if abs(denom) < 1e-20:
            # Parallel or coincident; intersection undefined for this context
            raise ValueError("Lines are parallel or coincident")
        t = (self.p1 - a).cross(B) / denom
        return Point(a.x + A.x * t, a.y + A.y * t)

class Polygon(Protocol):
    @abstractmethod
    def clip_polygon(self, clip_line: Line) -> 'Polygon': ...
    @abstractmethod
    def area(self) -> float: ...

class ConvexPolygon:
    __slots__ = ('points',)
    def __init__(self, points: List[Point]):
        self.points = points
    def clip_polygon(self, clip_line: Line) -> 'ConvexPolygon':
        # Sutherland-Hodgman polygon clipping
        new_points: List[Point] = []
        n = len(self.points)
        for i in range(n):
            curr = self.points[i]
            nxt = self.points[(i+1)%n]
            curr_in = clip_line.on_left(curr)
            nxt_in = clip_line.on_left(nxt)
            if curr_in:
                new_points.append(curr)
            if curr_in != nxt_in:
                inter_pt = clip_line.intersection(curr, nxt)
                new_points.append(inter_pt)
        # To remove any collinear duplicates caused by intersection points
        filtered = []
        for p in new_points:
            if len(filtered) == 0 or math.fabs(p.x - filtered[-1].x) > 1e-15 or math.fabs(p.y - filtered[-1].y) > 1e-15:
                filtered.append(p)
        if filtered and (math.fabs(filtered[0].x - filtered[-1].x) < 1e-15 and math.fabs(filtered[0].y - filtered[-1].y) < 1e-15):
            filtered.pop()
        return ConvexPolygon(filtered)
    def area(self) -> float:
        # Shoelace formula
        area = 0.0
        n = len(self.points)
        for i in range(n):
            j = (i + 1) % n
            area += self.points[i].x * self.points[j].y - self.points[j].x * self.points[i].y
        return abs(area) * 0.5

class Parser:
    @staticmethod
    def parse_polygon(input_stream) -> ConvexPolygon:
        n = int(next(input_stream))
        points = []
        for _ in range(n):
            x, y = map(int, next(input_stream).split())
            points.append(Point(x,y))
        return ConvexPolygon(points)
    @staticmethod
    def parse_queries(input_stream) -> List[Tuple[Point, Point]]:
        q = int(next(input_stream))
        queries = []
        for _ in range(q):
            p1x,p1y,p2x,p2y = map(int, next(input_stream).split())
            queries.append((Point(p1x,p1y), Point(p2x,p2y)))
        return queries

class ConvexCutSolver:
    def __init__(self, polygon: ConvexPolygon):
        self.polygon = polygon
    def solve(self, queries: List[Tuple[Point, Point]]) -> List[float]:
        areas = []
        for p1,p2 in queries:
            line = Line(p1, p2)
            clipped_polygon = self.polygon.clip_polygon(line)
            areas.append(clipped_polygon.area())
        return areas

def main():
    input_stream = iter(sys.stdin.read().strip().split('\n'))
    polygon = Parser.parse_polygon(input_stream)
    queries = Parser.parse_queries(input_stream)
    solver = ConvexCutSolver(polygon)
    results = solver.solve(queries)
    for area in results:
        print(f"{area:.8f}")

if __name__ == "__main__":
    main()