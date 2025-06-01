import sys
import math
from typing import List, Tuple, Iterator, Optional

class Point:
    __slots__ = ('x', 'y')
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_to(self, other: 'Point') -> float:
        dx = self.x - other.x
        dy = self.y - other.y
        return math.hypot(dx, dy)
    
    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: 'Point') -> 'Point':
        return Point(self.x - other.x, self.y - other.y)
        
    def scale(self, factor: float) -> 'Point':
        return Point(self.x * factor, self.y * factor)

class Circle:
    __slots__ = ('center', 'radius')
    def __init__(self, center: Point, radius: float = 1.0):
        self.center = center
        self.radius = radius

    def contains_point(self, point: Point) -> bool:
        return self.center.distance_to(point) <= self.radius + 1e-14

    def intersect_circle(self, other: 'Circle') -> List[Point]:
        # Returns the intersection points of two circles (0, 1, or 2 points)
        d = self.center.distance_to(other.center)
        r0, r1 = self.radius, other.radius
        if d > r0 + r1 + 1e-14 or d < abs(r0 - r1) - 1e-14:
            return []
        if d == 0 and r0 == r1: 
            # Circles coincide, infinite intersections, but we return empty for current problem
            return []
        a = (r0*r0 - r1*r1 + d*d) / (2*d)
        h_sq = r0*r0 - a*a
        if h_sq < -1e-14:
            return []
        h = math.sqrt(max(0.0, h_sq))
        p2 = other.center - self.center
        p2 = p2.scale(a/d)
        mid = self.center + p2
        if h == 0:
            return [mid]  # tangent
        # compute intersection points
        offset = Point(-(other.center.y - self.center.y) * (h/d), (other.center.x - self.center.x) * (h/d))
        i1 = mid + offset
        i2 = mid - offset
        return [i1, i2]

class StickerOverlapCalculator:
    __slots__ = ('stickers', 'radius', 'square_side')

    def __init__(self, stickers: List[Point], radius: float = 1.0, square_side: float = 10.0):
        self.stickers = [Circle(center=s, radius=radius) for s in stickers]
        self.radius = radius
        self.square_side = square_side

    def _generate_candidate_points(self) -> Iterator[Point]:
        # The candidate points are the centers of the circles and the intersection points of all circle pairs
        for circle in self.stickers:
            yield circle.center
        n = len(self.stickers)
        for i in range(n):
            for j in range(i+1, n):
                intersections = self.stickers[i].intersect_circle(self.stickers[j])
                for pt in intersections:
                    if 0.0 <= pt.x <= self.square_side and 0.0 <= pt.y <= self.square_side:
                        yield pt

    def _count_overlaps_at(self, point: Point) -> int:
        count = 0
        for circle in self.stickers:
            if circle.contains_point(point):
                count += 1
        return count

    def max_overlap(self) -> int:
        if not self.stickers:
            return 0
        max_count = 1
        for candidate in self._generate_candidate_points():
            current_count = self._count_overlaps_at(candidate)
            if current_count > max_count:
                max_count = current_count
        return max_count

class InputParser:
    @staticmethod
    def parse_line(line: str) -> Optional[Tuple[int, List[Point]]]:
        line = line.strip()
        if not line or line == '0':
            return None
        n = int(line)
        points = []
        for _ in range(n):
            coord_line = sys.stdin.readline()
            if not coord_line:
                break
            x_str, y_str = coord_line.split(',')
            points.append(Point(float(x_str), float(y_str)))
        return n, points

def main():
    results = []
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        line = line.strip()
        if line == '0':
            break
        n = int(line)
        stickers = []
        for _ in range(n):
            coord_line = sys.stdin.readline()
            x_str, y_str = coord_line.strip().split(',')
            stickers.append(Point(float(x_str), float(y_str)))
        calc = StickerOverlapCalculator(stickers)
        results.append(calc.max_overlap())
    for r in results:
        print(r)

if __name__ == '__main__':
    main()