class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __sub__(self, other: 'Point') -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def cross(self, other: 'Vector') -> int:
        return self.x * other.y - self.y * other.x

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


class Polygon:
    def __init__(self, points: list[Point]):
        self.points = points
        self.n = len(points)

    def _get_vector(self, i: int) -> Vector:
        return self.points[(i + 1) % self.n] - self.points[i]

    def is_convex(self) -> bool:
        # We expect the polygon points to be given CCW. The polygon is convex iff
        # all cross products of adjacent edges have the same sign (all <=0 or all >=0),
        # but since it's CCW, we expect all cross products to be >= 0.
        
        cross_sign = 0
        for i in range(self.n):
            v1 = self._get_vector(i)
            v2 = self._get_vector((i + 1) % self.n)
            cross = v1.cross(v2)
            if cross != 0:
                if cross_sign == 0:
                    cross_sign = 1 if cross > 0 else -1
                else:
                    if (cross > 0 and cross_sign < 0) or (cross < 0 and cross_sign > 0):
                        return False
        return True


class PolygonFactory:
    @staticmethod
    def from_input_lines(lines: list[str]) -> Polygon:
        n = int(lines[0])
        points = []
        for i in range(1, n + 1):
            x_str, y_str = lines[i].strip().split()
            points.append(Point(int(x_str), int(y_str)))
        return Polygon(points)


class ConvexityChecker:
    def __init__(self, polygon: Polygon):
        self.polygon = polygon

    def check(self) -> int:
        return 1 if self.polygon.is_convex() else 0


class App:
    def __init__(self):
        self.polygon = None
        self.checker = None

    def read_input(self):
        import sys
        lines = []
        n = int(sys.stdin.readline())
        lines.append(str(n))
        for _ in range(n):
            lines.append(sys.stdin.readline())
        self.polygon = PolygonFactory.from_input_lines(lines)

    def run(self):
        self.checker = ConvexityChecker(self.polygon)
        result = self.checker.check()
        print(result)


if __name__ == '__main__':
    app = App()
    app.read_input()
    app.run()