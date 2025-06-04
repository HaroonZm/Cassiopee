import sys
from typing import List, Tuple

class Point:
    __slots__ = ('x', 'y')
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __sub__(self, other: 'Point') -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

class Vector:
    __slots__ = ('x', 'y')
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def cross(self, other: 'Vector') -> int:
        return self.x * other.y - self.y * other.x

    def dot(self, other: 'Vector') -> int:
        return self.x * other.x + self.y * other.y

class Polygon:
    def __init__(self, vertices: List[Point]):
        self.vertices = vertices
        self.n = len(vertices)
        # Precompute bounding box (can be useful for future extensions)
        xs = [p.x for p in vertices]
        ys = [p.y for p in vertices]
        self.min_x = min(xs)
        self.max_x = max(xs)
        self.min_y = min(ys)
        self.max_y = max(ys)

    def contains_point(self, pt: Point) -> int:
        # Returns:
        # 2 if inside polygon
        # 1 if on edge
        # 0 otherwise

        # First, check if point is exactly on some polygon edge
        for i in range(self.n):
            a = self.vertices[i]
            b = self.vertices[(i + 1) % self.n]
            if self._point_on_segment(pt, a, b):
                return 1

        # Ray casting algorithm for point-in-polygon test
        # Count number of intersections of ray to the right of pt with polygon edges
        intersections = 0
        for i in range(self.n):
            a = self.vertices[i]
            b = self.vertices[(i + 1) % self.n]
            if self._ray_intersects_segment(pt, a, b):
                intersections += 1

        return 2 if intersections % 2 == 1 else 0

    def _point_on_segment(self, p: Point, a: Point, b: Point) -> bool:
        # Checks if point p lies on line segment ab
        ap = p - a
        ab = b - a
        cross = ap.cross(ab)
        if cross != 0:
            return False
        dot = ap.dot(ab)
        if dot < 0:
            return False
        squared_length_ab = ab.dot(ab)
        if dot > squared_length_ab:
            return False
        return True

    def _ray_intersects_segment(self, p: Point, a: Point, b: Point) -> bool:
        # Assumes ray cast to the right (+x)
        # Checks if horizontal ray from p to +∞ intersects segment ab

        # Make sure a.y <= b.y for consistency
        if a.y > b.y:
            a, b = b, a
        if p.y == a.y or p.y == b.y:
            # Perturb p.y slightly upward to avoid ambiguities per Jordan curve theorem
            py = p.y + 0.1
        else:
            py = p.y

        if py < a.y or py > b.y:
            return False
        if a.y == b.y:
            # Horizontal segment, no intersection
            return False

        # Compute intersection x coordinate of segment with horizontal line y = py
        intersect_x = a.x + (b.x - a.x) * (py - a.y) / (b.y - a.y)
        return intersect_x > p.x

class PolygonContainmentSolver:
    def __init__(self):
        self.polygon = None
        self.queries: List[Point] = []

    def read_input(self):
        input_lines = sys.stdin.read().strip().split('\n')
        n = int(input_lines[0])
        vertices = []
        idx = 1
        for _ in range(n):
            x, y = map(int, input_lines[idx].split())
            vertices.append(Point(x, y))
            idx += 1
        self.polygon = Polygon(vertices)
        q = int(input_lines[idx])
        idx += 1
        for _ in range(q):
            x, y = map(int, input_lines[idx].split())
            self.queries.append(Point(x, y))
            idx += 1

    def solve(self):
        for query_pt in self.queries:
            res = self.polygon.contains_point(query_pt)
            print(res)

def main():
    solver = PolygonContainmentSolver()
    solver.read_input()
    solver.solve()

if __name__ == "__main__":
    main()