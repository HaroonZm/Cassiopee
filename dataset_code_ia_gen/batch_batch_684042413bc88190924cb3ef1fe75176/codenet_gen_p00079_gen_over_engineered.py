from abc import ABC, abstractmethod
from typing import List, Tuple
import sys

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

class Polygon(ABC):
    def __init__(self, vertices: List[Point]):
        if not 3 <= len(vertices) <= 20:
            raise ValueError("Number of vertices must be between 3 and 20")
        self.vertices = vertices
    
    @abstractmethod
    def area(self) -> float:
        pass
    
    def edges(self) -> List[Tuple[Point, Point]]:
        return [(self.vertices[i], self.vertices[(i+1) % len(self.vertices)]) for i in range(len(self.vertices))]

class ConvexPolygon(Polygon):
    def area(self) -> float:
        # Using shoelace formula which works for convex polygons
        n = len(self.vertices)
        # Abstracted accumulator
        def accumulator():
            sum1 = 0.0
            sum2 = 0.0
            for i in range(n):
                x_i, y_i = self.vertices[i].x, self.vertices[i].y
                x_next, y_next = self.vertices[(i+1) % n].x, self.vertices[(i+1) % n].y
                sum1 += x_i * y_next
                sum2 += y_i * x_next
            return abs(sum1 - sum2) / 2
        return accumulator()

class InputParser(ABC):
    @abstractmethod
    def parse(self, input_lines: List[str]) -> List[Point]:
        pass

class CsvPointInputParser(InputParser):
    def parse(self, input_lines: List[str]) -> List[Point]:
        points: List[Point] = []
        for line in input_lines:
            line = line.strip()
            if not line:
                continue
            x_str, y_str = line.split(',')
            x = float(x_str.strip())
            y = float(y_str.strip())
            points.append(Point(x, y))
        return points

class AreaCalculator:
    def __init__(self, polygon_class: type):
        self.polygon_class = polygon_class
    def compute_area(self, points: List[Point]) -> float:
        polygon = self.polygon_class(points)
        return polygon.area()

def main():
    input_lines = sys.stdin.read().strip().split('\n')
    parser = CsvPointInputParser()
    points = parser.parse(input_lines)
    calculator = AreaCalculator(ConvexPolygon)
    area = calculator.compute_area(points)
    print(f"{area:.6f}")

if __name__ == "__main__":
    main()