import sys
from abc import ABC, abstractmethod
from typing import List, Tuple, Iterator, Optional


class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __sub__(self, other: 'Point') -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y)

    def distance_to(self, other: 'Point') -> float:
        return (self - other).length()

    def __repr__(self):
        return f"Point({self.x},{self.y})"


class Vector:
    __slots__ = ('x', 'y')

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def dot(self, other: 'Vector') -> float:
        return self.x * other.x + self.y * other.y

    def length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def scale(self, scalar: float) -> 'Vector':
        return Vector(self.x * scalar, self.y * scalar)

    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)

    def to_point(self) -> Point:
        return Point(self.x, self.y)

    def __repr__(self):
        return f"Vector({self.x},{self.y})"


class Shape(ABC):
    @abstractmethod
    def intersects_segment(self, p1: Point, p2: Point) -> bool:
        pass


class CylinderWall(Shape):
    __slots__ = ('center', 'radius')

    def __init__(self, center: Point, radius: int):
        self.center = center
        self.radius = radius

    def intersects_segment(self, p1: Point, p2: Point) -> bool:
        # Check if segment p1-p2 intersects the circle defined by center and radius

        # Vector from p1 to p2
        d = p2 - p1
        f = p1 - self.center

        a = d.dot(d)
        b = 2 * f.dot(d)
        c = f.dot(f) - self.radius * self.radius

        discriminant = b * b - 4 * a * c

        if discriminant < 0:
            # no intersection
            return False

        discriminant_sqrt = discriminant ** 0.5
        t1 = (-b - discriminant_sqrt) / (2 * a)
        t2 = (-b + discriminant_sqrt) / (2 * a)

        # Check if either of the intersection points lies between 0 and 1 on the segment
        if (0 <= t1 <= 1) or (0 <= t2 <= 1):
            return True
        return False

    def __repr__(self):
        return f"CylinderWall(center={self.center}, radius={self.radius})"


class VisibilityChecker:
    __slots__ = ('walls',)

    def __init__(self, walls: List[CylinderWall]):
        self.walls = walls

    def is_visible(self, taro: Point, oni: Point) -> bool:
        for wall in self.walls:
            if wall.intersects_segment(oni, taro):
                return False
        return True


class InputParser:
    @staticmethod
    def int_stream() -> Iterator[int]:
        for line in sys.stdin:
            for n_str in line.strip().split():
                yield int(n_str)

    def __init__(self):
        self._stream = self.int_stream()

    def next_int(self) -> int:
        return next(self._stream)

    def read_dataset(self) -> Optional[Tuple[List[CylinderWall], List[Tuple[Point, Point]]]]:
        try:
            n = self.next_int()
        except StopIteration:
            return None
        if n == 0:
            return None

        walls: List[CylinderWall] = []
        for _ in range(n):
            wx = self.next_int()
            wy = self.next_int()
            r = self.next_int()
            walls.append(CylinderWall(Point(wx, wy), r))

        m = self.next_int()
        pos_pairs: List[Tuple[Point, Point]] = []
        for _ in range(m):
            tx = self.next_int()
            ty = self.next_int()
            sx = self.next_int()
            sy = self.next_int()
            pos_pairs.append((Point(tx, ty), Point(sx, sy)))

        return walls, pos_pairs


class OutputHandler:
    @staticmethod
    def print_results(results: List[str]) -> None:
        for r in results:
            print(r)


class HarukuroboVisibilitySystem:
    __slots__ = ('parser',)

    def __init__(self):
        self.parser = InputParser()

    def run(self) -> None:
        while True:
            dataset = self.parser.read_dataset()
            if dataset is None:
                break
            walls, queries = dataset
            checker = VisibilityChecker(walls)
            results = []
            for taro_pos, oni_pos in queries:
                visible = checker.is_visible(taro_pos, oni_pos)
                results.append("Danger" if visible else "Safe")
            OutputHandler.print_results(results)


def main():
    system = HarukuroboVisibilitySystem()
    system.run()


if __name__ == "__main__":
    main()