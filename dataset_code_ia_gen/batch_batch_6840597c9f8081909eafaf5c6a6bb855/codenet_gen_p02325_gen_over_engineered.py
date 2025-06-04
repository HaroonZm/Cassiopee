import math
from typing import List, Tuple, Protocol

# Geometry abstractions

class Point2D:
    __slots__ = ('x', 'y')
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_to(self, other: 'Point2D') -> float:
        dx = self.x - other.x
        dy = self.y - other.y
        return math.hypot(dx, dy)

    def __repr__(self):
        return f"Point2D({self.x},{self.y})"


# Interface for distance metrics, allows future extension for other metrics
class DistanceMetric(Protocol):
    def distance(self, a: Point2D, b: Point2D) -> float:
        ...


class EuclideanDistance(DistanceMetric):
    def distance(self, a: Point2D, b: Point2D) -> float:
        return a.distance_to(b)


# Abstract input parser to allow future changes in input format or validation
class InputParser:
    def __init__(self):
        self.N = 0
        self.points: List[Point2D] = []

    def parse(self, raw_input: List[str]) -> Tuple[int, List[Point2D]]:
        # First line is N
        self.N = int(raw_input[0].strip())
        self.points = []
        for line in raw_input[1:self.N+1]:
            x_str, y_str = line.strip().split()
            point = Point2D(float(x_str), float(y_str))
            self.points.append(point)
        return self.N, self.points


# Abstract TSP Solver for extensibility if we want different TSP variants
class TSPSolver(Protocol):
    def solve(self, points: List[Point2D]) -> float:
        ...


# Concrete Bitonic TSP solver with heavy abstraction and state encapsulation
class BitonicTSPSolver(TSPSolver):
    def __init__(self, metric: DistanceMetric):
        self.metric = metric
        self.N = 0
        self.points: List[Point2D] = []
        self.dp: List[List[float]] = []
        self.INF = float('inf')

    def _initialize(self, points: List[Point2D]) -> None:
        self.points = points
        self.N = len(points)
        # DP table dp[i][j]: min distance path covering points 0..i where 
        # path is bitonic and endpoints of "right chain" are points i and j (j < i)
        self.dp = [[self.INF] * self.N for _ in range(self.N)]
        self.dp[1][0] = self.metric.distance(points[0], points[1])

    def _solve_dp(self) -> float:
        for i in range(2, self.N):
            for j in range(i-1):
                if j < i-1:
                    # Extend path by point i from dp[i-1][j]
                    self.dp[i][j] = self.dp[i-1][j] + self.metric.distance(self.points[i-1], self.points[i])
                else:
                    # j == i-1 case: find k < i-1 to connect
                    self.dp[i][i-1] = self.INF
                    for k in range(i-1):
                        candidate = self.dp[i-1][k] + self.metric.distance(self.points[k], self.points[i])
                        if candidate < self.dp[i][i-1]:
                            self.dp[i][i-1] = candidate
        # Answer is dp[N-1][j] + dist(points[j], points[N-1]) minimum over j < N-1
        res = self.INF
        for j in range(self.N - 1):
            candidate = self.dp[self.N - 1][j] + self.metric.distance(self.points[j], self.points[self.N - 1])
            if candidate < res:
                res = candidate
        return res

    def solve(self, points: List[Point2D]) -> float:
        self._initialize(points)
        return self._solve_dp()


def main():
    import sys

    raw_input = sys.stdin.read().strip().split('\n')

    parser = InputParser()
    N, points = parser.parse(raw_input)

    # Points given are guaranteed sorted by x-coordinate as per problem statement
    metric = EuclideanDistance()

    solver = BitonicTSPSolver(metric)
    result = solver.solve(points)

    print(f"{result:.8f}")


if __name__ == "__main__":
    main()