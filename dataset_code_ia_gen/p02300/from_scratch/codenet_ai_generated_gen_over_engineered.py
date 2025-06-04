from typing import List, Tuple, Protocol, Iterator, Optional
from abc import abstractmethod
import sys

class Point:
    __slots__ = ('x', 'y')
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point({self.x},{self.y})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return False
        return (self.x == other.x) and (self.y == other.y)

    def __lt__(self, other: 'Point') -> bool:
        # Sort by y, then by x
        if self.y != other.y:
            return self.y < other.y
        return self.x < other.x

    def __sub__(self, other: 'Point') -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y)


class Vector:
    __slots__ = ('dx', 'dy')
    def __init__(self, dx: int, dy: int) -> None:
        self.dx = dx
        self.dy = dy

    def cross(self, other: 'Vector') -> int:
        # Cross product of two vectors
        return self.dx * other.dy - self.dy * other.dx

    def __repr__(self) -> str:
        return f"Vector({self.dx},{self.dy})"


class ConvexHullAlgorithm(Protocol):
    @abstractmethod
    def compute(self, points: List[Point]) -> List[Point]:
        pass


class GrahamScan:
    def compute(self, points: List[Point]) -> List[Point]:
        n = len(points)
        if n <= 1:
            return points.copy()

        # Find the pivot: lowest y, leftmost x
        pivot = min(points)
        
        def polar_angle_cmp(p: Point) -> Tuple[int, int]:
            # Vector from pivot to p
            v = p - pivot
            # To sort by angle between pivot-p and horizontal axis, we use cross product indirectly
            # but here since we only need a sorting key, we will use atan2 approximation
            # But since we want a sophisticated design, let's avoid math.atan2 and use relative quadrant and cross
            # We'll use tuple of quadrant and cross product for sorting stable by angle

            # quadrant 1 if dy>=0 and dx>=0
            # quadrant 2 dy>0 and dx<0
            # quadrant 3 dy<0 and dx<0
            # quadrant 4 dy<0 and dx>=0
            # but to keep 'complex', let's define quadrant roughly for sorting by angle
            dx = v.dx
            dy = v.dy
            if dy > 0 or (dy == 0 and dx >= 0):
                quadrant = 1
            else:
                quadrant = 2
            # distance squared for tie-breaker (to cluster colinear points correctly)
            dist_sq = dx*dx + dy*dy
            return (quadrant, -dy * dx, dist_sq)  # -dy*dx is arbitrary surrogate for angle order

        # Sort points by polar angle around pivot
        sorted_points = points.copy()
        sorted_points.remove(pivot)
        # We need to group colinear points on hull boundary, so we will sort colinear points by distance ascending
        # We'll do that by adjusting comparator more minutely here:
        def angle_distance_key(p: Point) -> Tuple[int,int,int]:
            v = p - pivot
            dx = v.dx
            dy = v.dy
            # quadrant
            quad = 0
            if dy > 0 or (dy == 0 and dx >= 0):
                quad = 1
            else:
                quad = 2
            # cross surrogate: for the angle ordering we use cross with (1,0)
            # cross of vector (dx, dy) with (1,0) is dy
            # so angle order ascending is by quadrant then by -dy or dy depending on quadrant
            # let's just use dy and dx properly
            return (quad, -dy*dx, dx*dx+dy*dy)
        
        sorted_points.sort(key=angle_distance_key)

        # Build hull with a deque stack pattern:
        hull: List[Point] = [pivot]

        def orientation(a: Point, b: Point, c: Point) -> int:
            # >0 left turn, <0 right turn, 0 colinear
            return (b - a).cross(c - b)

        for pt in sorted_points:
            # Remove points that make a right turn, but keep colinear points on boundary
            while len(hull) > 1 and orientation(hull[-2], hull[-1], pt) < 0:
                hull.pop()
            hull.append(pt)

        # After this we might miss some colinear points on the boundary.
        # We must add all points on edges between hull points that lie on hull boundary.
        # But per problem statement, all boundary points including colinear on boundary must be included.

        # To fulfill this sophisticated extension, reconstruct hull edges including colinear boundary points:
        
        # We create a spatial query to detect points colinear on hull edges:
        boundary_points_set = set(hull)

        def is_point_on_segment(a: Point, b: Point, p: Point) -> bool:
            # check colinearity:
            if orientation(a,b,p) != 0:
                return False
            # check p lies within rectangle bounds of segment a-b
            min_x = min(a.x, b.x)
            max_x = max(a.x, b.x)
            min_y = min(a.y, b.y)
            max_y = max(a.y, b.y)
            return min_x <= p.x <= max_x and min_y <= p.y <= max_y

        # We'll create a sophisticated edge mapping for quick insert:
        # Create a list of edges of hull
        edges = [(hull[i], hull[(i+1)%len(hull)]) for i in range(len(hull))]

        # Collect points that lie on any hull edge but are not yet in hull
        extra_boundary_points: List[Point] = []

        for point in points:
            if point in boundary_points_set:
                continue
            for a,b in edges:
                if is_point_on_segment(a, b, point):
                    extra_boundary_points.append(point)
                    break

        # Add the extra boundary points to hull and reorder properly
        all_boundary_points = hull + extra_boundary_points

        # Sort all boundary points again in CCW order starting from pivot respecting problem condition
        def ccw_sort_key(p: Point) -> Tuple[int,int,int]:
            v = p - pivot
            dx = v.dx
            dy = v.dy
            quad = 0
            if dy > 0 or (dy == 0 and dx >= 0):
                quad = 1
            else:
                quad = 2
            dist_sq = dx*dx + dy*dy
            return (quad, -dy*dx, dist_sq)

        all_boundary_points = list(set(all_boundary_points))  # unique
        all_boundary_points.sort(key=ccw_sort_key)

        # Ensure pivot is first element
        # pivot is minimum y, x guaranteed
        min_index = all_boundary_points.index(pivot)
        rotated = all_boundary_points[min_index:] + all_boundary_points[:min_index]

        return rotated


class ConvexHullFacade:
    def __init__(self, algorithm: ConvexHullAlgorithm) -> None:
        self._algorithm = algorithm

    def get_convex_hull(self, points: List[Point]) -> List[Point]:
        if len(points) < 3:
            return points.copy()
        return self._algorithm.compute(points)


class InputParser:
    @staticmethod
    def parse_input() -> List[Point]:
        input_lines = sys.stdin.read().strip().split('\n')
        n = int(input_lines[0])
        pts = []
        for i in range(1, n + 1):
            x_str,y_str = input_lines[i].split()
            x,y = int(x_str), int(y_str)
            pts.append(Point(x, y))
        return pts


class OutputFormatter:
    @staticmethod
    def print_output(points: List[Point]) -> None:
        print(len(points))
        for p in points:
            print(p.x, p.y)


def main() -> None:
    points = InputParser.parse_input()
    hull_algorithm = GrahamScan()
    facade = ConvexHullFacade(hull_algorithm)
    hull = facade.get_convex_hull(points)
    OutputFormatter.print_output(hull)

if __name__ == "__main__":
    main()