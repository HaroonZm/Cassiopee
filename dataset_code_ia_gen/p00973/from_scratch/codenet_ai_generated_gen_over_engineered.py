from typing import List, Tuple
from math import hypot, isclose, inf
import sys


class Point:
    __slots__ = ['x', 'y']

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Point') -> 'Point':
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> 'Point':
        return Point(self.x * scalar, self.y * scalar)

    def dot(self, other: 'Point') -> float:
        return self.x * other.x + self.y * other.y

    def cross(self, other: 'Point') -> float:
        return self.x * other.y - self.y * other.x

    def dist_to(self, other: 'Point') -> float:
        return hypot(self.x - other.x, self.y - other.y)

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"


class Polygon:
    def __init__(self, vertices: List[Point]):
        self.vertices = vertices
        self.n = len(vertices)
        self.area = abs(self._signed_area())
        self.double_area = abs(self._signed_area() * 2)
        self._precompute_area_prefixes()

    def _signed_area(self) -> float:
        area = 0.0
        for i in range(self.n):
            j = (i + 1) % self.n
            area += self.vertices[i].cross(self.vertices[j])
        return area / 2.0

    def _precompute_area_prefixes(self):
        # For quick subpolygon area computations along the polygon chain
        self.area_prefix = [0.0] * (self.n + 1)
        for i in range(self.n):
            j = (i + 1) % self.n
            self.area_prefix[i + 1] = self.area_prefix[i] + self.vertices[i].cross(self.vertices[j])

    def subpolygon_area(self, i: int, j: int) -> float:
        # Area of polygon from vertex i to vertex j in CCW order (i<=j)
        # Use shoelace sum between i and j modulo n
        if i <= j:
            area = self.area_prefix[j] - self.area_prefix[i] + self.vertices[j].cross(self.vertices[i])
        else:
            # wrap around the polygon
            area = self.area_prefix[self.n] - self.area_prefix[i] + self.area_prefix[j] + self.vertices[j].cross(self.vertices[i])
        return abs(area / 2)

    def total_area(self):
        return self.area

    def get_vertex(self, idx: int) -> Point:
        return self.vertices[idx % self.n]


class EqualAreaCutSolver:
    def __init__(self, polygon: Polygon):
        self.poly = polygon
        self.half_area = polygon.total_area() / 2.0
        self.n = polygon.n
        # We will prepare a lazy iterator for j values per i
        # to find the 2nd point so that polygon[i..j] has area half_area

    def _point_on_edge(self, a: Point, b: Point, frac: float) -> Point:
        # Returns point at fraction frac along segment a->b
        return Point(a.x + (b.x - a.x) * frac, a.y + (b.y - a.y) * frac)

    def _interpolated_area(self, i: int, j: int, frac: float) -> float:
        # Area of polygon from vertex i to fractional point along edge j->j+1 with frac in [0,1]
        # i and j are indices of vertices, assumes i != j
        area_full = self.poly.subpolygon_area(i, j)
        # Add part of edge from j to j+1 times frac
        vj = self.poly.get_vertex(j)
        vj1 = self.poly.get_vertex(j + 1)
        cross_partial = vj.cross(self._point_on_edge(vj, vj1, frac)) - self.poly.get_vertex(j + 1).cross(vj)
        # Area = full polygon area i..j + fraction partial (triangle)
        area = abs((2 * area_full + cross_partial) / 2)
        return area

    def _find_edge_fraction_for_half_area(self, i: int, j_low: int, j_high: int) -> Tuple[int, float]:
        # Binary search on edge j_high edge fraction in [0..1] for area==half_area
        left, right = 0.0, 1.0
        for _ in range(60):
            mid = (left + right) / 2
            a = self._interpolated_area(i, j_low, mid)
            if a < self.half_area:
                left = mid
            else:
                right = mid
        return j_low, (left + right) / 2

    def find_equal_area_lines(self) -> Tuple[List[Tuple[Point, Point]], List[float]]:
        # For convex polygon, every chord pairing vertices (and edges) can produce at most one equal half-area cut
        # We find for each i the matching j and fractional edge to get half area
        results = []
        j = 1
        # j must always be ahead of i (mod n)
        for i in range(self.n):
            if j == i:
                j = (j + 1) % self.n
            # Move j forward while area polygon(i..j) < half_area
            while True:
                a = self.poly.subpolygon_area(i, j)
                if a < self.half_area:
                    j = (j + 1) % self.n
                    if j == i:  # full loop done
                        break
                else:
                    break
            # Now polygon area(i..j-1) < half_area <= polygon area(i..j)
            j_prev = (j - 1 + self.n) % self.n
            area_prev = self.poly.subpolygon_area(i, j_prev)
            if isclose(area_prev, self.half_area, abs_tol=1e-15):
                # The vertex j_prev is the cut point
                a_point = self.poly.get_vertex(i)
                b_point = self.poly.get_vertex(j_prev)
                results.append((a_point, b_point))
            else:
                # Fractional point on edge j_prev -> j to make half area
                fractional_edge_idx = j_prev
                # Binary search fraction
                left, right = 0.0, 1.0
                for _ in range(60):
                    mid = (left + right) / 2
                    a = self._interpolated_area(i, fractional_edge_idx, mid)
                    if a < self.half_area:
                        left = mid
                    else:
                        right = mid
                frac = (left + right) / 2
                a_point = self.poly.get_vertex(i)
                b_point = self._point_on_edge(self.poly.get_vertex(fractional_edge_idx), self.poly.get_vertex(fractional_edge_idx + 1), frac)
                results.append((a_point, b_point))
        return results

    def solve(self) -> Tuple[float, float]:
        # Find min and max lengths of equal-area cuts
        equal_area_segments = self.find_equal_area_lines()
        lengths = [seg[0].dist_to(seg[1]) for seg in equal_area_segments]
        min_len = min(lengths)
        max_len = max(lengths)
        return min_len, max_len


class InputParser:
    @staticmethod
    def parse_points(n: int, data: List[str]) -> List[Point]:
        pts = []
        for i in range(n):
            x_str, y_str = data[i].strip().split()
            pts.append(Point(float(x_str), float(y_str)))
        return pts


def main():
    input_lines = sys.stdin.read().strip().split('\n')
    n = int(input_lines[0])
    pts = InputParser.parse_points(n, input_lines[1:])
    polygon = Polygon(pts)
    solver = EqualAreaCutSolver(polygon)
    min_len, max_len = solver.solve()
    print(min_len)
    print(max_len)


if __name__ == '__main__':
    main()