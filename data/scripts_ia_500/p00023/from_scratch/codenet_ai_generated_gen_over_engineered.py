from abc import ABC, abstractmethod
from typing import List, Tuple
import math

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_to(self, other: 'Point') -> float:
        return math.hypot(self.x - other.x, self.y - other.y)

class Shape(ABC):
    @abstractmethod
    def contains(self, other: 'Shape') -> bool:
        pass

    @abstractmethod
    def intersects(self, other: 'Shape') -> bool:
        pass

    @abstractmethod
    def is_identical(self, other: 'Shape') -> bool:
        pass

class Circle(Shape):
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

    def contains(self, other: 'Shape') -> bool:
        if isinstance(other, Circle):
            dist_centers = self.center.distance_to(other.center)
            # other totally inside self if distance plus other's radius <= self's radius
            return dist_centers + other.radius < self.radius
        return False

    def intersects(self, other: 'Shape') -> bool:
        if isinstance(other, Circle):
            dist_centers = self.center.distance_to(other.center)
            sum_radii = self.radius + other.radius
            diff_radii = abs(self.radius - other.radius)
            # intersection of circumferences if distance between centers equals sum or difference of radii (tangency), 
            # or if distance between centers less than sum but greater than difference (two intersection points)
            # The problem wants to print "1" if circumferences intersect. This includes tangency or crossing.
            return diff_radii <= dist_centers <= sum_radii
        return False

    def is_identical(self, other: 'Shape') -> bool:
        if isinstance(other, Circle):
            # Two circles are identical if centers and radii are same
            return math.isclose(self.center.x, other.center.x) and \
                   math.isclose(self.center.y, other.center.y) and \
                   math.isclose(self.radius, other.radius)
        return False

class CircleRelationshipEvaluator:
    def __init__(self, circle_a: Circle, circle_b: Circle):
        self.circle_a = circle_a
        self.circle_b = circle_b

    def evaluate(self) -> int:
        # First exclude identical
        if self.circle_a.is_identical(self.circle_b):
            raise ValueError("Circles are identical according to problem statement this cannot happen.")

        # Check containment
        if self.circle_a.contains(self.circle_b):
            return 2
        if self.circle_b.contains(self.circle_a):
            return -2

        # Check circumference intersection
        if self.circle_a.intersects(self.circle_b):
            return 1

        # Else no overlap
        return 0

class InputParser:
    @staticmethod
    def parse_line(line: str) -> Tuple[float, float, float, float, float, float]:
        parts = line.strip().split()
        if len(parts) != 6:
            raise ValueError("Each dataset line must contain 6 numeric values.")
        return tuple(map(float, parts))

class CircleIntersectionProblemSolver:
    def __init__(self, input_data: List[str]):
        self.N = int(input_data[0].strip())
        if not (1 <= self.N <= 50):
            raise ValueError("N must be between 1 and 50 inclusive.")
        self.data_lines = input_data[1:self.N+1]

    def solve(self) -> List[int]:
        results = []
        for line in self.data_lines:
            xa, ya, ra, xb, yb, rb = InputParser.parse_line(line)
            circle_a = Circle(Point(xa, ya), ra)
            circle_b = Circle(Point(xb, yb), rb)
            evaluator = CircleRelationshipEvaluator(circle_a, circle_b)
            result = evaluator.evaluate()
            results.append(result)
        return results

def main():
    import sys
    input_data = sys.stdin.read().strip().split('\n')
    solver = CircleIntersectionProblemSolver(input_data)
    results = solver.solve()
    for r in results:
        print(r)

if __name__ == "__main__":
    main()