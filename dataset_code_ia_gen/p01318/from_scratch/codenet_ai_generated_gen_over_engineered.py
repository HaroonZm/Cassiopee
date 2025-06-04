from abc import ABC, abstractmethod
from typing import List, Tuple, Optional
import sys
import math
import itertools

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __sub__(self, other:'Point') -> 'Point':
        return Point(self.x - other.x, self.y - other.y)

    def distance(self, other:'Point') -> float:
        return math.hypot(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"Point({self.x},{self.y})"

class Line:
    """
    Represents an infinite line given by equation Ax + By + C = 0
    """
    def __init__(self, A: float, B: float, C: float):
        norm = math.hypot(A, B)
        self.A = A / norm
        self.B = B / norm
        self.C = C / norm

    @staticmethod
    def from_points(p1: Point, p2: Point) -> 'Line':
        A = p2.y - p1.y
        B = p1.x - p2.x
        C = -(A * p1.x + B * p1.y)
        return Line(A, B, C)

    @staticmethod
    def perpendicular_through_point(line:'Line', p:Point) -> 'Line':
        # perpendicular line: A' = B, B' = -A
        A_ = line.B
        B_ = -line.A
        C_ = -(A_ * p.x + B_ * p.y)
        return Line(A_, B_, C_)

    def distance_to_point(self, p: Point) -> float:
        return abs(self.A * p.x + self.B * p.y + self.C)

    def side(self, p: Point) -> float:
        # positive if point is on one side, negative on the other, zero on line
        return self.A * p.x + self.B * p.y + self.C

    def __repr__(self):
        return f"Line({self.A}x + {self.B}y + {self.C} = 0)"

class Jewel:
    def __init__(self, x: int, y: int, r: int, m: int):
        self.center = Point(x,y)
        self.r = r
        self.m = m

    def distance_to_line_surface(self, line: Line) -> Optional[float]:
        """
        Calculate the distance d between the line and the jewel's surface.
        This is distance from center to line minus radius r.
        Returns None if line intersects (penetrates) jewel circle.
        """
        dist_center_line = line.distance_to_point(self.center)

        if dist_center_line < self.r - 1e-10:
            # line penetrates jewel, invalid
            return None
        else:
            # distance to surface d >= 0
            return dist_center_line - self.r

    def is_absorbed_by_line(self, line: Line) -> bool:
        """
        Check if jewel is safely attracted by metal rod placed along line.
        Condition:
          - line does not penetrate jewel (distance_center_line >= r)
          - distance surface to line d <= magnet power m
        """
        d = self.distance_to_line_surface(line)
        if d is None:
            return False
        return 0 <= d <= self.m + 1e-10


class LineCandidateGenerator:
    """
    Abstract factory to generate candidate lines that might maximize attracted jewels.
    For extensibility and testability.
    """

    def __init__(self, jewels: List[Jewel]):
        self.jewels = jewels

    def generate(self) -> List[Line]:
        candidates = []
        # Candidates from pairwise jewel center connections => the line passing close to both jewel surfaces
        candidates.extend(self.lines_from_jewel_pairs())
        # Candidates from tangents between jewel circles (important to consider)
        candidates.extend(self.lines_from_external_tangents())
        # Candidates from single jewel shifted by magnet radius generating vertical lines
        candidates.extend(self.lines_from_single_jewel())

        # deduplicate lines by normalized coefficients
        unique = {}
        for line in candidates:
            key = (round(line.A, 12), round(line.B, 12), round(line.C, 12))
            unique[key] = line
        return list(unique.values())

    def lines_from_jewel_pairs(self) -> List[Line]:
        """
        Generate lines that pass through midpoints or between pairs of jewel centers,
        as potential candidates.
        We'll consider the line through centers and lines perpendicular at points offset by magnet radii.
        """
        lines = []
        for i, j in itertools.combinations(range(len(self.jewels)), 2):
            j1 = self.jewels[i]
            j2 = self.jewels[j]
            if j1.center.x == j2.center.x and j1.center.y == j2.center.y:
                continue  # ignore identical centers
            # line through centers
            line_centers = Line.from_points(j1.center, j2.center)
            lines.append(line_centers)

            # Try offset lines parallel to line_centers, shifted by magnet radii + radius
            # Actually, better to consider tangents explicitly in other method.
        return lines

    def lines_from_external_tangents(self) -> List[Line]:
        """
        Generate candidate lines that are external common tangents to pairs of jewels
        We consider all 4 types of tangents between two circles.
        """
        lines = []
        for i, j in itertools.combinations(range(len(self.jewels)), 2):
            c1 = self.jewels[i]
            c2 = self.jewels[j]
            ts = self.common_tangents(c1, c2)
            lines.extend(ts)
        return lines

    def common_tangents(self, c1: Jewel, c2: Jewel) -> List[Line]:
        """
        Compute lines tangent to both jewels from outside (or inner)
        Each tangent line can be described by angle and intercept.
        Approach adapted from geometry routines.
        Return list of Line objects.
        """
        res = []
        x1, y1, r1 = c1.center.x, c1.center.y, c1.r
        x2, y2, r2 = c2.center.x, c2.center.y, c2.r
        dx = x2 - x1
        dy = y2 - y1
        dist = math.hypot(dx, dy)
        if dist < 1e-14:
            # same center, no tangent lines
            return res

        # Loop for external and internal tangent: +1 and -1
        for sign1 in [+1, -1]:
            r = r2 * sign1 - r1
            if dist == 0 and r == 0:
                continue
            # Check discriminant
            sq = dist * dist - r * r
            if sq < -1e-14:
                # no tangent lines for this sign combo
                continue
            sq = 0 if abs(sq) < 1e-14 else sq
            h = math.sqrt(sq)
            # Tangent points calculation
            # Formula from https://cp-algorithms.com/geometry/circle_tangents.html
            vx = (dx * r + -dy * h) / (dist * dist)
            vy = (dy * r + dx * h) / (dist * dist)
            A = vy
            B = -vx
            # The line satisfies A x + B y + C = 0
            # We know line is tangent to circle1, so plug (x1, y1)
            C = -A * x1 - B * y1 + r1
            l1 = Line(A, B, C)
            res.append(l1)

            C = -A * x1 - B * y1 - r1
            l2 = Line(A, B, C)
            res.append(l2)

        return res

    def lines_from_single_jewel(self) -> List[Line]:
        """
        For each jewel, consider vertical and horizontal placement just outside the circle + magnet distance.
        These lines might maximize absorption of that jewel and neighbors.
        """
        lines = []
        for j in self.jewels:
            # vertical line x = x0 (A=1,B=0,C=-x0)
            x0 = j.center.x + j.r + j.m
            lines.append(Line(1, 0, -x0))
            x0 = j.center.x - (j.r + j.m)
            lines.append(Line(1, 0, -x0))
            # horizontal line y = y0
            y0 = j.center.y + j.r + j.m
            lines.append(Line(0, 1, -y0))
            y0 = j.center.y - (j.r + j.m)
            lines.append(Line(0, 1, -y0))
        return lines


class JewelAbsorber:
    """
    Calculates maximum number of jewels absorbed by placing one infinite metal rod.
    """

    def __init__(self, jewels: List[Jewel]):
        self.jewels = jewels

    def max_absorbable(self) -> int:
        if len(self.jewels) == 0:
            return 0
        if len(self.jewels) == 1:
            # Just check single jewel if can place line near its surface
            j = self.jewels[0]
            # line tangential just at distance <= m and no penetration
            # e.g., vertical line x = x0 at distance r + d <= r + m
            # We can always place such a line since infinite length, so always 1
            return 1

        candidate_generator = LineCandidateGenerator(self.jewels)
        candidates = candidate_generator.generate()

        max_count = 1  # At least one jewel can be absorbed by some line (can pass tangent)
        for line in candidates:
            count = 0
            for jewel in self.jewels:
                if jewel.is_absorbed_by_line(line):
                    count += 1
            if count > max_count:
                max_count = count

        # Also consider all possible angles from pairs of jewel centers (rotate line)
        # This is implicitly done in candidate lines generation.

        return max_count


class InputReader:
    """
    Iterator reading datasets from stdin
    """

    def __init__(self):
        self.lines = sys.stdin.read().strip().split('\n')
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self) -> Optional[List[Jewel]]:
        while self.idx < len(self.lines):
            line = self.lines[self.idx].strip()
            self.idx += 1
            if line == '0':
                raise StopIteration
            if not line:
                continue
            N = int(line)
            jewels = []
            for _ in range(N):
                x, y, r, m = map(int, self.lines[self.idx].strip().split())
                self.idx += 1
                jewels.append(Jewel(x,y,r,m))
            return jewels
        raise StopIteration

def main():
    reader = InputReader()
    for jewels in reader:
        absorber = JewelAbsorber(jewels)
        print(absorber.max_absorbable())

if __name__ == "__main__":
    main()