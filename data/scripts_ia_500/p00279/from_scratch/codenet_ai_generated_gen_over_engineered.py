import sys
import math
from itertools import combinations
from typing import List, Tuple, Optional

class Point:
    __slots__ = ['x','y','idx']
    def __init__(self, x: int, y: int, idx: int):
        self.x = x
        self.y = y
        self.idx = idx
    def __lt__(self, other:'Point') -> bool:
        # For lex order by x then y
        if self.x == other.x:
            return self.y < other.y
        return self.x < other.x
    def __sub__(self, other:'Point') -> 'Point':
        return Point(self.x - other.x, self.y - other.y, -1)
    def cross(self, other:'Point') -> int:
        # cross product self x other
        return self.x*other.y - self.y*other.x
    def __repr__(self):
        return f"Point(idx={self.idx},x={self.x},y={self.y})"

class Polygon:
    def __init__(self, vertices: List[Point]):
        self.vertices = vertices
    def area(self) -> float:
        # shoelace formula
        area = 0
        n = len(self.vertices)
        for i in range(n):
            p1 = self.vertices[i]
            p2 = self.vertices[(i+1)%n]
            area += p1.x*p2.y - p2.x*p1.y
        return abs(area)/2.0
    def is_convex(self) -> bool:
        n = len(self.vertices)
        if n < 3:
            return False
        sign = 0
        for i in range(n):
            a = self.vertices[i]
            b = self.vertices[(i+1)%n]
            c = self.vertices[(i+2)%n]
            cross = (b - a).cross(c - b)
            if cross == 0:
                return False
            curr_sign = 1 if cross > 0 else -1
            if sign == 0:
                sign = curr_sign
            elif sign != curr_sign:
                return False
        return True
    def ccw_order(self) -> List[Point]:
        # reorder vertices in ccw starting from vertex with min y then min x
        # find vertex with min y (then min x)
        start = min(self.vertices, key=lambda p: (p.y, p.x))
        idx = self.vertices.index(start)
        reordered = self.vertices[idx:] + self.vertices[:idx]
        # check orientation and reorder accordingly
        # If polygon is cw, reverse
        def orientation(poly: List[Point]) -> float:
            n = len(poly)
            s = 0.0
            for i in range(n):
                p1 = poly[i]
                p2 = poly[(i+1)%n]
                s += (p2.x - p1.x)*(p2.y + p1.y)
            return s
        if orientation(reordered) > 0:
            # cw, reverse to ccw
            reordered = [reordered[0]] + reordered[:0:-1]
        return reordered

class ConvexPolygonFinder:
    def __init__(self, points: List[Point]):
        self.points = points
        self.N = len(points)
        # Preprocessing for faster convexity test?
        # But since N max 40 and k max N, bruteforce combos with pruning is OK.
        # We'll implement a convexity check for each candidate polygon via Polygon.is_convex().
    def find_min_area_convex_polygon(self, k: int) -> Optional[Polygon]:
        # Among all k-combinations, find convex polygon with minimal area.
        # Note: The problem states:
        # - No 3 points collinear.
        # - Minimal convex polygon for each k unique with gap >= 0.0001 -> no ties
        # Potential optimization: 
        # Early pruning by sorting points lex order and if polygon area big, skip.
        # But simplest: try all combinations.
        if k > self.N or k < 3:
            return None
        min_area = math.inf
        best_poly = None
        pts = self.points
        # We'll generate combinations ordered by the indices (which are 1-based)
        # To accelerate convexity check, first form polygon from points in the order of combination
        # Verify if polygon is convex, and area smaller than current min_area -> keep
        # Because the polygon is formed by joining points in the order of combination, 
        # but order of indices won't necessarily form a polygon in ccw order.
        # So, the polygon's vertices are to be sorted as polygon:
        # The polygon must be convex - what order of points to consider?
        # Strategy:
        # For each combination of points, compute the polygon as the convex hull of these points
        # If polygon size != k, skip (means they are not collinear but hull is smaller)
        # Then the polygon is convex by construction
        # Among these, pick polygon with minimal area.
        for combo in combinations(pts, k):
            # Compute convex hull of these k points
            hull = self.convex_hull(list(combo))
            if len(hull) == k:
                poly = Polygon(hull)
                a = poly.area()
                if a < min_area:
                    min_area = a
                    best_poly = poly
        return best_poly

    def convex_hull(self, points: List[Point]) -> List[Point]:
        # Andrew's monotone chain algorithm 
        points = sorted(points)
        n = len(points)
        if n <= 1:
            return points
        lower = []
        for p in points:
            while len(lower) >= 2 and (lower[-1]-lower[-2]).cross(p - lower[-1]) <= 0:
                lower.pop()
            lower.append(p)
        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and (upper[-1]-upper[-2]).cross(p - upper[-1]) <= 0:
                upper.pop()
            upper.append(p)
        # Remove last element of each list because it's the start point of the other list
        hull = lower[:-1] + upper[:-1]
        return hull

def read_input() -> Tuple[List[Point], List[int]]:
    input = sys.stdin.readline
    N = int(input())
    points = []
    for i in range(N):
        x,y = map(int,input().split())
        points.append(Point(x,y,i+1))
    Q = int(input())
    ks = []
    for _ in range(Q):
        k = int(input())
        ks.append(k)
    return points, ks

def print_polygon(polygon: Polygon):
    # Output vertices indices from vertex with lowest y then x, ccw
    poly_ccw = polygon.ccw_order()
    ids = [p.idx for p in poly_ccw]
    print(' '.join(map(str, ids)))

def main():
    points, queries = read_input()
    finder = ConvexPolygonFinder(points)
    for k in queries:
        poly = finder.find_min_area_convex_polygon(k)
        if poly is None:
            print("NA")
        else:
            print_polygon(poly)

if __name__ == '__main__':
    main()