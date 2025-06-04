class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __sub__(self, other: 'Point') -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y)

    def __add__(self, other: 'Vector') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def dot(self, other: 'Vector') -> float:
        return self.x * other.x + self.y * other.y

    def scale(self, scalar: float) -> 'Vector':
        return Vector(self.x * scalar, self.y * scalar)

    def length_squared(self) -> float:
        return self.x * self.x + self.y * self.y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
        self.direction = p2 - p1
        if self.direction.length_squared() == 0:
            raise ValueError("p1 and p2 cannot be the same point")

    def project(self, p: Point) -> Point:
        """Project point p orthogonally onto the line defined by p1 and p2."""
        p1_to_p = p - self.p1
        t = p1_to_p.dot(self.direction) / self.direction.length_squared()
        projection_vector = self.direction.scale(t)
        projection_point = self.p1 + projection_vector
        return projection_point


class Projector:
    def __init__(self, p1x: int, p1y: int, p2x: int, p2y: int):
        self.line = Line(Point(p1x, p1y), Point(p2x, p2y))

    def project_points(self, points: list) -> list:
        projected = []
        for p in points:
            proj = self.line.project(Point(p[0], p[1]))
            projected.append(proj)
        return projected


class InputParser:
    @staticmethod
    def parse_initial_line(line: str):
        parts = line.strip().split()
        p1x, p1y, p2x, p2y = map(int, parts)
        return p1x, p1y, p2x, p2y

    @staticmethod
    def parse_queries(q: int, lines: list):
        points = []
        for i in range(q):
            x, y = map(int, lines[i].strip().split())
            points.append((x, y))
        return points


class Formatter:
    @staticmethod
    def format_point(point: Point) -> str:
        return f"{point.x:.10f} {point.y:.10f}"


def main():
    import sys
    input_lines = sys.stdin.read().strip().split('\n')
    p1x, p1y, p2x, p2y = InputParser.parse_initial_line(input_lines[0])
    q = int(input_lines[1])
    points = InputParser.parse_queries(q, input_lines[2:2+q])
    projector = Projector(p1x, p1y, p2x, p2y)
    projections = projector.project_points(points)
    for proj in projections:
        print(Formatter.format_point(proj))


if __name__ == "__main__":
    main()