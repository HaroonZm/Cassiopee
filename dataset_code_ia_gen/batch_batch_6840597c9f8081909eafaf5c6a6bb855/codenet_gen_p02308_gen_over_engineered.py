from typing import List, Tuple, Optional
import math
import sys

class Point:
    __slots__ = ['x', 'y']
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __lt__(self, other: 'Point') -> bool:
        if not math.isclose(self.x, other.x, abs_tol=1e-10):
            return self.x < other.x
        return self.y < other.y
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return False
        return math.isclose(self.x, other.x, abs_tol=1e-10) and math.isclose(self.y, other.y, abs_tol=1e-10)
    
    def __repr__(self) -> str:
        return f'Point({self.x}, {self.y})'
    
    def format(self) -> str:
        return f'{self.x:.8f} {self.y:.8f}'

class Vector(Point):
    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y)
    def __mul__(self, scalar: float) -> 'Vector':
        return Vector(self.x * scalar, self.y * scalar)
    def dot(self, other: 'Vector') -> float:
        return self.x * other.x + self.y * other.y
    def norm_sq(self) -> float:
        return self.x**2 + self.y**2
    def norm(self) -> float:
        return math.sqrt(self.norm_sq())

class Line:
    def __init__(self, p1: Point, p2: Point):
        if p1 == p2:
            raise ValueError("Line points must be distinct")
        self.p1 = p1
        self.p2 = p2
        self.dir = Vector(p2.x - p1.x, p2.y - p1.y)  # Direction vector
    
    def parametric_point(self, t: float) -> Point:
        return Point(self.p1.x + t * self.dir.x, self.p1.y + t * self.dir.y)
    
    def __repr__(self) -> str:
        return f'Line({self.p1}, {self.p2})'

class Circle:
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius
    
    def intersection_with_line(self, line: Line) -> List[Point]:
        # Parametric line: P(t) = p1 + t*(p2 - p1)
        # Circle eq: (x - cx)^2 + (y - cy)^2 = r^2
        # Substitute line into circle:
        # (p1.x + t*dx - cx)^2 + (p1.y + t*dy - cy)^2 = r^2
        dx = line.dir.x
        dy = line.dir.y
        fx = line.p1.x - self.center.x
        fy = line.p1.y - self.center.y
        
        a = dx*dx + dy*dy
        b = 2*(fx*dx + fy*dy)
        c = fx*fx + fy*fy - self.radius*self.radius
        
        discriminant = b*b - 4*a*c
        
        if discriminant < -1e-15:
            # No real intersection (problem states must have at least one)
            return []
        elif abs(discriminant) < 1e-15:
            # One intersection (tangent)
            t = -b/(2*a)
            p = line.parametric_point(t)
            return [p, p]
        else:
            sqrt_disc = math.sqrt(discriminant)
            t1 = (-b - sqrt_disc) / (2*a)
            t2 = (-b + sqrt_disc) / (2*a)
            p1 = line.parametric_point(t1)
            p2 = line.parametric_point(t2)
            # Return sorted points
            points = [p1, p2]
            points.sort()
            # If they are same point numerically
            if points[0] == points[1]:
                return [points[0], points[0]]
            return points

class InputParser:
    def __init__(self, stream):
        self.stream = stream
    
    def read_line(self) -> str:
        return self.stream.readline()
    
    def parse_circle(self) -> Circle:
        line = self.read_line()
        cx, cy, r = map(int, line.strip().split())
        return Circle(Point(float(cx), float(cy)), float(r))
    
    def parse_queries(self) -> List[Line]:
        q = int(self.read_line().strip())
        queries = []
        for _ in range(q):
            x1, y1, x2, y2 = map(int, self.read_line().strip().split())
            p1 = Point(float(x1), float(y1))
            p2 = Point(float(x2), float(y2))
            queries.append(Line(p1, p2))
        return queries

class Formatter:
    @staticmethod
    def format_points(points: List[Point]) -> str:
        return f'{points[0].format()} {points[1].format()}'

class CrossPointsSolver:
    def __init__(self, circle: Circle, queries: List[Line]):
        self.circle = circle
        self.queries = queries
    
    def solve(self) -> List[str]:
        results = []
        for line in self.queries:
            cross_points = self.circle.intersection_with_line(line)
            results.append(Formatter.format_points(cross_points))
        return results

def main():
    parser = InputParser(sys.stdin)
    circle = parser.parse_circle()
    queries = parser.parse_queries()
    solver = CrossPointsSolver(circle, queries)
    results = solver.solve()
    print('\n'.join(results))

if __name__ == '__main__':
    main()