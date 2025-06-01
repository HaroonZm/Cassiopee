from abc import ABC, abstractmethod
from typing import List, Tuple
import sys


class Point:
    def __init__(self, x: float, y: float) -> None:
        self._x = x
        self._y = y

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    def as_tuple(self) -> Tuple[float, float]:
        return (self._x, self._y)


class Polygon(ABC):
    def __init__(self, vertices: List[Point]) -> None:
        if len(vertices) < 3:
            raise ValueError("A polygon must have at least 3 vertices.")
        if len(vertices) > 20:
            raise ValueError("A polygon must have at most 20 vertices.")
        self._vertices = vertices.copy()

    @property
    def vertices(self) -> List[Point]:
        return self._vertices.copy()

    @abstractmethod
    def area(self) -> float:
        pass


class ConvexPolygon(Polygon):
    def __init__(self, vertices: List[Point]) -> None:
        super().__init__(vertices)
        if not self._is_convex():
            raise ValueError("The polygon is not convex.")

    def _cross_product_z(self, a: Point, b: Point, c: Point) -> float:
        # Vector AB
        abx = b.x - a.x
        aby = b.y - a.y
        # Vector BC
        bcx = c.x - b.x
        bcy = c.y - b.y
        return abx * bcy - aby * bcx

    def _is_convex(self) -> bool:
        # A polygon is convex if all cross products of adjacent edges have the same sign
        n = len(self._vertices)
        if n < 4:
            # Triangles are always convex
            return True
        sign = None
        for i in range(n):
            a = self._vertices[i]
            b = self._vertices[(i + 1) % n]
            c = self._vertices[(i + 2) % n]
            cross = self._cross_product_z(a, b, c)
            if cross == 0:
                # Collinear points are borderline but allowed here as convex
                continue
            current_sign = cross > 0
            if sign is None:
                sign = current_sign
            elif sign != current_sign:
                return False
        return True

    def area(self) -> float:
        # Implement polygon area using the shoelace formula
        n = len(self._vertices)
        sum1 = 0.0
        sum2 = 0.0
        for i in range(n):
            x_i, y_i = self._vertices[i].as_tuple()
            x_next, y_next = self._vertices[(i + 1) % n].as_tuple()
            sum1 += x_i * y_next
            sum2 += y_i * x_next
        return abs(sum1 - sum2) / 2.0


class InputParser(ABC):
    @abstractmethod
    def parse(self, lines: List[str]) -> List[Point]:
        pass


class ConvexPolygonInputParser(InputParser):
    def parse(self, lines: List[str]) -> List[Point]:
        points = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if ',' not in line:
                raise ValueError(f"Invalid coordinate format: {line}")
            x_str, y_str = line.split(',', 1)
            x = float(x_str.strip())
            y = float(y_str.strip())
            points.append(Point(x, y))
        if not (3 <= len(points) <= 20):
            raise ValueError("Number of vertices must be between 3 and 20 inclusive.")
        return points


class PolygonAreaCalculator(ABC):
    @abstractmethod
    def calculate_area(self, polygon: Polygon) -> float:
        pass


class ConvexPolygonAreaCalculator(PolygonAreaCalculator):
    def calculate_area(self, polygon: ConvexPolygon) -> float:
        return polygon.area()


class PolygonApp:
    def __init__(self,
                 parser: InputParser,
                 area_calculator: PolygonAreaCalculator) -> None:
        self._parser = parser
        self._area_calculator = area_calculator

    def run(self, input_lines: List[str]) -> None:
        points = self._parser.parse(input_lines)
        polygon = ConvexPolygon(points)
        area = self._area_calculator.calculate_area(polygon)
        print(f"{area:.6f}")


def main():
    input_lines = [line.rstrip('\n') for line in sys.stdin if line.strip() != '']
    app = PolygonApp(
        parser=ConvexPolygonInputParser(),
        area_calculator=ConvexPolygonAreaCalculator()
    )
    app.run(input_lines)


if __name__ == "__main__":
    main()