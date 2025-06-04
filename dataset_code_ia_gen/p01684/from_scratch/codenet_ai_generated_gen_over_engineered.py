import math
import sys
from abc import ABC, abstractmethod
from typing import Optional, Tuple, Iterator

# Mathematical constants often used throughout, defined in a single place.
class Constants:
    PI = math.pi
    EPS = 1e-10
    MARGIN = 1e-4

# Abstract geometry entity base class for future extensibility
class GeometryEntity(ABC):
    @abstractmethod
    def contains_point(self, x: float, y: float) -> bool:
        pass

# Circle class representing a circle with center (x, y) and radius r
class Circle(GeometryEntity):
    def __init__(self, x: float, y: float, r: float):
        self.x = x
        self.y = y
        self.r = r  # radius
    
    @property
    def area(self) -> float:
        return Constants.PI * self.r * self.r
    
    # Check if a point (px, py) belongs inside or on this circle
    def contains_point(self, px: float, py: float) -> bool:
        dx = px - self.x
        dy = py - self.y
        return dx*dx + dy*dy <= self.r * self.r + Constants.EPS
    
    # Checks if the circle fits inside the given rectangle with margin
    def fits_in_rectangle(self, width: float, height: float) -> bool:
        margin = Constants.MARGIN
        return (self.x - self.r >= -margin and
                self.y - self.r >= -margin and
                self.x + self.r <= width + margin and
                self.y + self.r <= height + margin)
    
    def __repr__(self):
        return f"Circle(x={self.x}, y={self.y}, r={self.r})"


# Abstract Solver class: to allow possibly different solving strategies in the future
class AbstractVennSolver(ABC):
    @abstractmethod
    def solve(self, U_W: float, U_H: float, A: float, B: float, AB: float) -> Optional[Tuple[Circle, Circle]]:
        pass


class VennDiagramSolver(AbstractVennSolver):
    """
    This solver tries to find two circles representing sets A and B in rectangle U_W x U_H such that:
    - Area(Circle A) = A
    - Area(Circle B) = B
    - Area(Intersection of A and B) = AB
    - Circles fit inside rectangle with margin
    Most sophisticated approach:
    - Abstracted intersection area computations
    - Numerical solver for distance d between circle centers
    """
    def __init__(self):
        self.pi = Constants.PI
        self.eps = Constants.EPS
        self.margin = Constants.MARGIN

    def _radius_from_area(self, area: float) -> float:
        return math.sqrt(area / self.pi)
    
    def _intersection_area(self, r1: float, r2: float, d: float) -> float:
        """
        Compute the area of intersection between two circles with radii r1, r2 and center distance d.
        Source: http://mathworld.wolfram.com/Circle-CircleIntersection.html
        Returns zero if circles do not overlap.
        """
        if d >= r1 + r2:
            return 0.0
        if d <= abs(r1 - r2):
            # One circle is inside the other; intersection area is smaller circle area.
            return math.pi * min(r1, r2)**2

        r1_sq = r1 * r1
        r2_sq = r2 * r2

        alpha = math.acos((d*d + r1_sq - r2_sq) / (2 * d * r1))
        beta = math.acos((d*d + r2_sq - r1_sq) / (2 * d * r2))

        area = (r1_sq * alpha + r2_sq * beta -
                0.5 * (r1_sq * math.sin(2*alpha) + r2_sq * math.sin(2*beta)))
        return area
    
    def _find_distance_for_intersection(self, r1: float, r2: float, target: float) -> Optional[float]:
        """
        Find distance d between two circle centers given radii r1 and r2 so that
        their intersection area is target.
        Uses binary search on d.
        Returns None if no suitable d found.
        """
        # Distance d ranges from |r1-r2| to r1+r2 for intersection
        low = abs(r1 - r2)
        high = r1 + r2
        
        # The intersection area decreases monotonically as d grows for these two fixed radii.
        # Special easy cases:
        max_intersection = math.pi * min(r1, r2)**2
        if target > max_intersection + self.eps:
            return None
        if abs(target - max_intersection) <= self.eps:
            return low
        if target < 0 - self.eps:
            return None
        if target <= 0 + self.eps:
            # Target intersection zero means circles do not overlap
            if d_ok := (high >= low):
                return high
            return None
        
        # Binary search for intersection area matching target
        for _ in range(100):  # 100 iterations for sufficient precision
            mid = (low + high) / 2
            area = self._intersection_area(r1, r2, mid)
            if abs(area - target) <= 1e-7:
                return mid
            if area > target:
                low = mid  # Need circles farther to reduce intersection
            else:
                high = mid
        # After bsearch, return best estimate
        return (low + high) / 2
    
    def _compute_circle_positions(
        self, U_W: float, U_H: float, rA: float, rB: float, d: float
    ) -> Optional[Tuple[Circle, Circle]]:
        """
        Compute positions of two circles (centers) given:
        - radii and distance d between centers
        - circles should fully fit inside rectangle U_W x U_H with margins
        We attempt placing both centers on the horizontal center line Y = U_H/2
        and try minimal margin constraints.
        """
        # vertical center line to maximize margin top and bottom
        center_y = U_H / 2
        
        # The problem reduces to placing centers at (xA, center_y), (xB, center_y)
        # such that distance d between centers, circles fit inside rectangle.
        # To maximize margin from left/right edges:
        # xA - rA >= 0
        # xB + rB <= U_W
        # xB - xA = d
        #
        # One optimal solution is:
        # xA = rA + margin
        # xB = xA + d
        #
        # Check feasibility:
        xA = rA + self.margin
        xB = xA + d
        
        if xB + rB > U_W + self.margin:
            # Not enough horizontal space on the right, try to shift to left if possible
            delta = xB + rB - (U_W + self.margin)
            # Try shifting both circles left by delta
            xA -= delta
            xB -= delta
            if xA - rA < -self.margin:
                return None
        
        circleA = Circle(xA, center_y, rA)
        circleB = Circle(xB, center_y, rB)
        if circleA.fits_in_rectangle(U_W, U_H) and circleB.fits_in_rectangle(U_W, U_H):
            return circleA, circleB
        return None
    
    def solve(self, U_W: float, U_H: float, A: float, B: float, AB: float) -> Optional[Tuple[Circle, Circle]]:
        """
        Solve the problem for one dataset.
        Returns tuple of Circle A and Circle B or None if impossible.
        """
        # Validate intersection limit
        if AB > min(A, B) + self.eps:
            # intersection can't be larger than smaller set
            return None
        if A <= 0 or B <= 0:
            return None
        
        rA = self._radius_from_area(A)
        rB = self._radius_from_area(B)
        
        # Handle corner cases:
        # If AB == 0, the circles must not intersect at all.
        # If AB == min(A, B), one circle is inside the other fully overlapping
        
        d = None
        if abs(AB) < self.eps:
            # No intersection allowed: distance >= rA + rB
            d = rA + rB
        else:
            # Find distance d for which intersection area is AB
            d = self._find_distance_for_intersection(rA, rB, AB)
            if d is None:
                # No suitable distance found
                return None

        # Use distance d to locate circle centers inside rectangle
        positions = self._compute_circle_positions(U_W, U_H, rA, rB, d)
        if positions is None:
            # Try a different arrangement: swap A and B and try again,
            # as placing circles in reverse order might help margin.
            positions = self._compute_circle_positions(U_W, U_H, rB, rA, d)
            if positions is not None:
                # Swap back the circles to match A and B order
                circleB, circleA = positions
                return circleA, circleB
            return None

        circleA, circleB = positions
        # Validate areas approximately
        areaA = circleA.area
        areaB = circleB.area
        inter_area = self._intersection_area(rA, rB, d)
        # Absolute errors must not exceed 0.0001
        if abs(areaA - A) > 0.0001 or abs(areaB - B) > 0.0001 or abs(inter_area - AB) > 0.0001:
            return None
        return circleA, circleB


class InputOutputHandler:
    def __init__(self):
        self.solver = VennDiagramSolver()
    
    def parse_line(self, line: str) -> Optional[Tuple[float, float, float, float, float]]:
        parts = line.strip().split()
        if len(parts) != 5:
            return None
        vals = list(map(float, parts))
        if all(abs(v) < 1e-9 for v in vals):
            # termination line
            return None
        return tuple(vals)
    
    def read_datasets(self) -> Iterator[Tuple[float, float, float, float, float]]:
        for line in sys.stdin:
            parsed = self.parse_line(line)
            if parsed is None:
                break
            yield parsed
    
    def format_output(self, circleA: Circle, circleB: Circle) -> str:
        # Floating point format with required precision - 9 decimals for safety
        return f"{circleA.x:.9f} {circleA.y:.9f} {circleA.r:.9f} {circleB.x:.9f} {circleB.y:.9f} {circleB.r:.9f}"
    
    def run(self):
        for U_W, U_H, A, B, AB in self.read_datasets():
            result = self.solver.solve(U_W, U_H, A, B, AB)
            if result is None:
                print("impossible")
            else:
                circleA, circleB = result
                print(self.format_output(circleA, circleB))


if __name__ == "__main__":
    io_handler = InputOutputHandler()
    io_handler.run()