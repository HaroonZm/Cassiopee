from typing import List, Tuple
from abc import ABC, abstractmethod

class Point:
    __slots__ = ('x', 'y')
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __iter__(self):
        yield self.x
        yield self.y
    
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

class PolygonalEntity(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Polygon(PolygonalEntity):
    def __init__(self, points: List[Point]):
        if len(points) < 3:
            raise ValueError("A polygon must have at least 3 vertices.")
        self._points = points
    
    @property
    def points(self) -> Tuple[Point, ...]:
        return tuple(self._points)
    
    def area(self) -> float:
        return self._shoelace_formula()
    
    def _shoelace_formula(self) -> float:
        n = len(self._points)
        sum1 = 0
        sum2 = 0
        for i in range(n):
            x_i, y_i = self._points[i].x, self._points[i].y
            x_next, y_next = self._points[(i + 1) % n].x, self._points[(i + 1) % n].y
            sum1 += x_i * y_next
            sum2 += y_i * x_next
        return abs(sum1 - sum2) / 2.0

class PolygonFactory:
    @staticmethod
    def from_input(n: int, coords: List[Tuple[int, int]]) -> Polygon:
        points = [Point(x, y) for x, y in coords]
        return Polygon(points)

class AreaPrinter:
    @staticmethod
    def print_area(polygon: Polygon):
        print(f"{polygon.area():.1f}")

class PolygonAreaApplication:
    def __init__(self):
        self._polygon_factory = PolygonFactory()
        self._area_printer = AreaPrinter()
    
    def run(self):
        n = int(input())
        coords = [tuple(map(int, input().split())) for _ in range(n)]
        polygon = self._polygon_factory.from_input(n, coords)
        self._area_printer.print_area(polygon)

if __name__ == "__main__":
    app = PolygonAreaApplication()
    app.run()