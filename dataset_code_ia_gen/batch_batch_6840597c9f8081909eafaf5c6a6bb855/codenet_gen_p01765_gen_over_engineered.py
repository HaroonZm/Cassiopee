import math
from abc import ABC, abstractmethod
from typing import List, Tuple


class Point:
    __slots__ = ('x', 'y')
    
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_to(self, other: 'Point') -> float:
        return math.hypot(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Segment:
    __slots__ = ('start', 'end')

    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def distance_to_point(self, p: Point) -> float:
        """Distance from point p to this segment."""
        px, py = p.x, p.y
        x1, y1 = self.start.x, self.start.y
        x2, y2 = self.end.x, self.end.y

        dx, dy = x2 - x1, y2 - y1
        if dx == 0 and dy == 0:
            return p.distance_to(self.start)

        t = ((px - x1) * dx + (py - y1) * dy) / (dx * dx + dy * dy)
        t = max(0.0, min(1.0, t))
        proj_x = x1 + t * dx
        proj_y = y1 + t * dy
        return math.hypot(px - proj_x, py - proj_y)

    def __repr__(self):
        return f"Segment({self.start}, {self.end})"


class Polyline:
    """
    Represents a polyline with certain fixed endpoints as specified in the problem.
    Abstracts the representation for potential extensions.
    """
    def __init__(self, points: List[Point], fixed_start: Point, fixed_end: Point):
        self.fixed_start = fixed_start
        self.fixed_end = fixed_end
        self.points = points  # excludes the fixed endpoints
        self.segments: List[Segment] = []
        self._build_segments()

    def _build_segments(self):
        pts = [self.fixed_start] + self.points + [self.fixed_end]
        self.segments = [Segment(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]

    def distance_to_point(self, p: Point) -> float:
        """Minimum distance from point p to this polyline."""
        return min(seg.distance_to_point(p) for seg in self.segments)

    def __repr__(self):
        return f"Polyline({self.segments})"


class Channel:
    """
    Represents the channel formed by two polylines (walls).
    Provides method to calculate the minimal clearance for a circle center between them.
    """
    def __init__(self, lower_wall: Polyline, upper_wall: Polyline):
        self.lower_wall = lower_wall
        self.upper_wall = upper_wall

    def clearance_radius(self, p: Point) -> float:
        """
        Calculate the clearance radius at point p for circle passing between the walls.
        The radius is the minimal distance to either wall.
        """
        dist_lower = self.lower_wall.distance_to_point(p)
        dist_upper = self.upper_wall.distance_to_point(p)
        return min(dist_lower, dist_upper)

    def is_position_valid(self, p: Point, radius: float) -> bool:
        """
        Check if a circle with given radius can be centered at p without intersecting the walls.
        Intersection or tangency is allowed, so radius <= clearance_radius(p).
        """
        return radius <= self.clearance_radius(p)


class PathFinder(ABC):
    """
    Abstract base class for path finding in the channel.
    Future extensions could implement different algorithms.
    """
    @abstractmethod
    def can_pass(self, diameter: float) -> bool:
        """Determine if it is possible to pass the channel with given diameter circle."""
        pass


class GeometricPathFinder(PathFinder):
    """
    Implements geometry-based feasibility via continuous-space search and binary search on diameter.
    Uses a flood fill over free space putatively discretized.
    """

    def __init__(self, channel: Channel, discretization: int = 200):
        self.channel = channel
        self.discretization = discretization  # Number of discrete points along x axis to consider
        # We discretize x between 0 and 1000 into equal steps, and for each x find feasible y interval.

    def _feasible_y_range(self, x: float, radius: float) -> Tuple[float, float]:
        """
        For given x and radius, compute all y where a circle centered at (x,y) with radius is valid.
        Since problem is about passage between two polylines, 
        we compute max possible y range inside channel clearance >= radius.
        We'll do a scan of y values and find intersection intervals.
        """
        # We take y in [0, 1000], discretize finely
        VALID_THRESHOLD = 1e-12
        y_min, y_max = None, None
        step = 0.5  # coarse enough yet detailed

        possible_intervals = []
        inside = False
        start_y = None
        y = 0.0
        while y <= 1000.0 + VALID_THRESHOLD:
            p = Point(x, y)
            if self.channel.is_position_valid(p, radius):
                if not inside:
                    start_y = y
                    inside = True
            else:
                if inside:
                    possible_intervals.append((start_y, y - step))
                    inside = False
            y += step
        if inside:
            possible_intervals.append((start_y, 1000.0))

        if not possible_intervals:
            return None, None

        # Because walls do not intersect and shape is a channel, only one interval should exist ideally.
        # Take the widest interval
        widest = max(possible_intervals, key=lambda intrv: intrv[1]-intrv[0])
        return widest

    def can_pass(self, diameter: float) -> bool:
        radius = diameter / 2
        step = 1000 / self.discretization

        # For each discrete x, find feasible y interval
        feasible_intervals = []
        for i in range(self.discretization + 1):
            x = i * step
            yrange = self._feasible_y_range(x, radius)
            if yrange == (None, None):
                return False  # No feasible y here, can't pass
            feasible_intervals.append((x, yrange))

        # Now check if there exists a continuous path from x=0 (with any y<0) passing
        # the channel to x=1000 (with y>1000).
        # Actually initial position is x<0 (outside left) and must go to x>1000 (outside right).
        # So it means at x=0 and x=1000, the y-range is feasible for the circle center inside the channel.

        # We'll simulate that the circle can enter from left side
        # because at x=0 (and less), circle is outside the channel ( x<0) which is unrestricted,
        # So start feasibility at x=0 with accessible y ranges from that position.

        # Entering means some y0 at x=0 is accessible; since x=0 is on polyline start, rely on interval
        left_interval = feasible_intervals[0][1]
        right_interval = feasible_intervals[-1][1]
        if left_interval == (None,None) or right_interval == (None,None):
            return False

        # Now, verify connectivity between intervals across x discretization,
        # ensuring that the intersection between intervals at consecutive x is non empty
        prev_ymin, prev_ymax = left_interval
        for idx in range(1, len(feasible_intervals)):
            _, (cur_ymin, cur_ymax) = feasible_intervals[idx]
            # Find intersection of intervals
            low = max(prev_ymin, cur_ymin)
            high = min(prev_ymax, cur_ymax)
            if low > high:
                return False
            prev_ymin, prev_ymax = low, high

        # At the end, path from left to right exists inside the channel
        return True


class DiameterSolver:
    """
    Orchestrates the binary search over diameter based on the PathFinder feasibility predicate.
    """
    def __init__(self, pathfinder: PathFinder, precision: float = 1e-7):
        self.pathfinder = pathfinder
        self.precision = precision

    def solve(self) -> float:
        low = 0.0
        high = 1000.0  # Max possible diameter since channel width <= 1000

        while high - low > self.precision:
            mid = (low + high) / 2
            if self.pathfinder.can_pass(mid):
                low = mid
            else:
                high = mid

        return low


def parse_polyline(N: int, points_data: List[Tuple[int, int]], fixed_start: Point, fixed_end: Point) -> Polyline:
    points = [Point(x, y) for x, y in points_data]
    return Polyline(points, fixed_start, fixed_end)


def main():
    # Parsing input
    import sys
    input = sys.stdin.readline

    N1 = int(input())
    pts1 = [tuple(map(int, input().split())) for _ in range(N1)]
    N2 = int(input())
    pts2 = [tuple(map(int, input().split())) for _ in range(N2)]

    # Construct polylines with fixed endpoints
    lower_wall = parse_polyline(N1, pts1, Point(0, 0), Point(1000, 0))
    upper_wall = parse_polyline(N2, pts2, Point(0, 1000), Point(1000, 1000))
    channel = Channel(lower_wall, upper_wall)

    pathfinder = GeometricPathFinder(channel, discretization=400)
    solver = DiameterSolver(pathfinder)
    max_diameter = solver.solve()

    print(f"{max_diameter:.10f}")


if __name__ == '__main__':
    main()