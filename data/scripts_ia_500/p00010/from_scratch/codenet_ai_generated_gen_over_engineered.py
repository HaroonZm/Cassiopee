from abc import ABC, abstractmethod
from typing import List, Tuple
import math

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y - other.y)
    
    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)
    
    def __truediv__(self, value: float) -> "Point":
        return Point(self.x / value, self.y / value)
    
    def __mul__(self, value: float) -> "Point":
        return Point(self.x * value, self.y * value)
    
    def distance_to(self, other: "Point") -> float:
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

class Circle:
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius
    
    def __repr__(self):
        return f"Circle(center={self.center}, radius={self.radius})"

class Triangle(ABC):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    
    @abstractmethod
    def circumscribed_circle(self) -> Circle:
        pass

class TriangleEuclidean(Triangle):
    def circumscribed_circle(self) -> Circle:
        # According to the formula from coordinate geometry:
        # https://en.wikipedia.org/wiki/Circumscribed_circle#Cartesian_coordinates_2
        
        x1, y1 = self.p1.x, self.p1.y
        x2, y2 = self.p2.x, self.p2.y
        x3, y3 = self.p3.x, self.p3.y
        
        d = 2 * (x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))
        if abs(d) < 1e-15:
            # Points are collinear or too close -> no circumscribed circle
            raise ValueError("Points are collinear or too close for circumscribed circle")
        
        ux = ((x1**2 + y1**2)*(y2 - y3) + (x2**2 + y2**2)*(y3 - y1) + (x3**2 + y3**2)*(y1 - y2)) / d
        uy = ((x1**2 + y1**2)*(x3 - x2) + (x2**2 + y2**2)*(x1 - x3) + (x3**2 + y3**2)*(x2 - x1)) / d
        
        center = Point(ux, uy)
        radius = center.distance_to(self.p1)
        
        return Circle(center, radius)

class InputParser:
    def __init__(self):
        self.datasets = 0
        self.data: List[List[float]] = []
    
    def read(self):
        import sys
        lines = sys.stdin.read().strip().split('\n')
        self.datasets = int(lines[0])
        for i in range(1, self.datasets + 1):
            parts = list(map(float, lines[i].strip().split()))
            self.data.append(parts)

class Formatter(ABC):
    @abstractmethod
    def format(self, circle: Circle) -> str:
        pass

class FixedPrecisionFormatter(Formatter):
    def __init__(self, precision: int):
        self.precision = precision
    
    def format(self, circle: Circle) -> str:
        return f"{circle.center.x:.{self.precision}f} {circle.center.y:.{self.precision}f} {circle.radius:.{self.precision}f}"

class Controller:
    def __init__(self, parser: InputParser, formatter: Formatter):
        self.parser = parser
        self.formatter = formatter
    
    def solve(self):
        self.parser.read()
        results = []
        for coords in self.parser.data:
            p1 = Point(coords[0], coords[1])
            p2 = Point(coords[2], coords[3])
            p3 = Point(coords[4], coords[5])
            triangle = TriangleEuclidean(p1, p2, p3)
            try:
                circle = triangle.circumscribed_circle()
                results.append(self.formatter.format(circle))
            except Exception as e:
                # If invalid input, output zero circle according to a safe fallback
                results.append("0.000 0.000 0.000")
        print("\n".join(results))

if __name__ == "__main__":
    parser = InputParser()
    formatter = FixedPrecisionFormatter(3)
    controller = Controller(parser, formatter)
    controller.solve()