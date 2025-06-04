import math
from abc import ABC, abstractmethod
from typing import List, Tuple

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __sub__(self, other: 'Point') -> 'Point':
        return Point(self.x - other.x, self.y - other.y)

    def cross(self, other: 'Point') -> float:
        return self.x * other.y - self.y * other.x

    def distance_to(self, other: 'Point') -> float:
        return math.hypot(self.x - other.x, self.y - other.y)

class ConvexHullSolver(ABC):
    @abstractmethod
    def compute_hull(self, points: List[Point]) -> List[Point]:
        pass

    @abstractmethod
    def compute_area(self, hull: List[Point]) -> float:
        pass

class GrahamScanHullSolver(ConvexHullSolver):
    def compute_hull(self, points: List[Point]) -> List[Point]:
        # Sort points lex order
        points = sorted(points, key=lambda p: (p.x, p.y))

        # Build lower hull
        lower = []
        for p in points:
            while len(lower) >= 2 and (lower[-1] - lower[-2]).cross(p - lower[-2]) <= 0:
                lower.pop()
            lower.append(p)

        # Build upper hull
        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and (upper[-1] - upper[-2]).cross(p - upper[-2]) <= 0:
                upper.pop()
            upper.append(p)

        # Concatenate lower and upper hull to full hull; skip last point of each because it is duplicated
        hull = lower[:-1] + upper[:-1]
        return hull

    def compute_area(self, hull: List[Point]) -> float:
        area = 0.0
        n = len(hull)
        for i in range(n):
            j = (i + 1) % n
            area += hull[i].x * hull[j].y - hull[j].x * hull[i].y
        return abs(area) / 2.0

class Rabbit:
    def __init__(self, speed: float):
        self.speed = speed

    def position(self, angle_rad: float) -> Point:
        return Point(self.speed * math.cos(angle_rad), self.speed * math.sin(angle_rad))

class TeamStrategy:
    def __init__(self, rabbits: List[Rabbit]):
        self.rabbits = rabbits
        self.n = len(rabbits)

    def maximize_area(self) -> float:
        # Strategy: assign each rabbit a direction (angle), find the maximum convex polygon area possible
        # Because convex polygon with points at distance r_i from origin in directions can have large area,
        # We need to search angles. But direct search in continuous range is complex.
        # The optimal is to place points in order with angles increasing, forming a convex polygon.
        # We will search on the space of angles, ensuring angles are strictly ordered to maintain convexity.
        # Due to constraints (N <= 8), we can do backtracking with pruning.

        angles = [0.0] * self.n
        best_area = 0.0

        # We'll fix the first angle at 0 for rotation normalization
        angles[0] = 0.0

        def backtrack(i: int, prev_angle: float):
            nonlocal best_area
            if i == self.n:
                points = [self.rabbits[j].position(angles[j]) for j in range(self.n)]
                hull_solver = GrahamScanHullSolver()
                hull = hull_solver.compute_hull(points)
                if len(hull) >= 3:
                    area = hull_solver.compute_area(hull)
                    if area > best_area:
                        best_area = area
                return

            # To maintain non-decreasing angles, choose angle from prev_angle + epsilon up to 2*pi
            # We'll sample the angle space with decent granularity to keep time reasonable.
            # Since N <= 8, and sampling 60 points per angle max, roughly 60^(N-1) is large,
            # so we limit samples or do heuristics.
            # Instead we sample limited candidate angles for each rabbit.

            samples_count = 60
            start = prev_angle + 1e-9
            end = 2 * math.pi - (self.n - i - 1) * (2*math.pi / self.n)
            # The end is to keep enough space for remaining points, to avoid angle overlaps

            # If start > end, no valid angle for this position, backtrack
            if start > end + 1e-12:
                return

            for s in range(samples_count):
                candidate = start + s * (end - start) / (samples_count - 1)
                angles[i] = candidate
                backtrack(i + 1, candidate)

        backtrack(1, 0.0)
        return best_area

def main():
    N = int(input())
    rabbits = [Rabbit(float(input())) for _ in range(N)]

    strategy = TeamStrategy(rabbits)
    max_area = strategy.maximize_area()

    print(f"{max_area:.9f}")

if __name__ == "__main__":
    main()