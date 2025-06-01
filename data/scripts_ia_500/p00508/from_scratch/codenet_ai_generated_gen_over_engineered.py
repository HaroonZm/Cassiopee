from typing import List, Tuple, Protocol, runtime_checkable
from abc import abstractmethod
import sys
import math

@runtime_checkable
class PointProtocol(Protocol):
    x: int
    y: int

class Point:
    __slots__ = ('x', 'y')
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def distance_sq(self, other: 'PointProtocol') -> int:
        dx = self.x - other.x
        dy = self.y - other.y
        return dx * dx + dy * dy

class InputReader:
    def __init__(self, sys_stdin=sys.stdin):
        self._stdin = sys_stdin

    def read_int(self) -> int:
        return int(self._stdin.readline().strip())

    def read_points(self, n: int) -> List[Point]:
        points = []
        for _ in range(n):
            x_str, y_str = self._stdin.readline().split()
            points.append(Point(int(x_str), int(y_str)))
        return points

class ClosestPairAlgorithm(Protocol):
    @abstractmethod
    def find_closest_pair_distance_sq(self, points: List[PointProtocol]) -> int:
        pass

class DivideAndConquerClosestPair:
    def find_closest_pair_distance_sq(self, points: List[PointProtocol]) -> int:
        Px = sorted(points, key=lambda p: p.x)
        Py = sorted(points, key=lambda p: p.y)
        return self._closest_pair_recursive(Px, Py)

    def _closest_pair_recursive(self, Px: List[PointProtocol], Py: List[PointProtocol]) -> int:
        n = len(Px)
        if n <= 3:
            return self._brute_force(Px)
        mid = n // 2
        Qx = Px[:mid]
        Rx = Px[mid:]
        midpoint_x = Px[mid].x
        Qy = []
        Ry = []
        for p in Py:
            if p.x <= midpoint_x:
                Qy.append(p)
            else:
                Ry.append(p)
        d_left = self._closest_pair_recursive(Qx, Qy)
        d_right = self._closest_pair_recursive(Rx, Ry)
        d = min(d_left, d_right)
        strip = [p for p in Py if abs(p.x - midpoint_x) ** 2 < d]
        d_strip = self._strip_closest(strip, d)
        return min(d, d_strip)

    def _brute_force(self, points: List[PointProtocol]) -> int:
        min_dist = math.inf
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                dist = points[i].distance_sq(points[j])
                if dist < min_dist:
                    min_dist = dist
        return min_dist

    def _strip_closest(self, strip: List[PointProtocol], d: int) -> int:
        min_dist = d
        length = len(strip)
        for i in range(length):
            j = i + 1
            while j < length and (strip[j].y - strip[i].y)**2 < min_dist:
                dist = strip[i].distance_sq(strip[j])
                if dist < min_dist:
                    min_dist = dist
                j += 1
        return min_dist

class ClosestPairSolver:
    def __init__(self, reader: InputReader, algorithm: ClosestPairAlgorithm):
        self.reader = reader
        self.algorithm = algorithm

    def solve(self) -> int:
        n = self.reader.read_int()
        points = self.reader.read_points(n)
        return self.algorithm.find_closest_pair_distance_sq(points)

def main():
    reader = InputReader()
    algorithm = DivideAndConquerClosestPair()
    solver = ClosestPairSolver(reader, algorithm)
    result = solver.solve()
    print(result)

if __name__ == "__main__":
    main()