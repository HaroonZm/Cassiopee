class Point:
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    def __sub__(self, other: 'Point') -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y)


class Vector:
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    def dot(self, other: 'Vector') -> float:
        return self.x * other.x + self.y * other.y

    def cross(self, other: 'Vector') -> float:
        return self.x * other.y - self.y * other.x

    def length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5


class Triangle:
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self._p1 = p1
        self._p2 = p2
        self._p3 = p3
        self._area = abs((p2 - p1).cross(p3 - p1)) / 2.0

    def area(self) -> float:
        return self._area

    def contains_point(self, p: Point) -> bool:
        # Using barycentric coordinates method
        v0 = self._p3 - self._p1
        v1 = self._p2 - self._p1
        v2 = p - self._p1

        dot00 = v0.dot(v0)
        dot01 = v0.dot(v1)
        dot02 = v0.dot(v2)
        dot11 = v1.dot(v1)
        dot12 = v1.dot(v2)

        denom = dot00 * dot11 - dot01 * dot01
        if denom == 0:
            return False  # degenerate triangle

        inv_denom = 1 / denom
        u = (dot11 * dot02 - dot01 * dot12) * inv_denom
        v = (dot00 * dot12 - dot01 * dot02) * inv_denom

        # Allow points on edges or vertices
        return (u >= -1e-10) and (v >= -1e-10) and (u + v <= 1 + 1e-10)


class InputParser:
    def __init__(self):
        pass

    def __iter__(self):
        import sys
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            tokens = line.split()
            if len(tokens) != 8:
                continue
            try:
                coords = list(map(float, tokens))
                yield coords
            except ValueError:
                continue


class TrianglePointInclusionSolver:
    def __init__(self):
        self._parser = InputParser()

    def solve(self):
        for coords in self._parser:
            x1, y1, x2, y2, x3, y3, xp, yp = coords
            p1 = Point(x1, y1)
            p2 = Point(x2, y2)
            p3 = Point(x3, y3)
            p = Point(xp, yp)
            triangle = Triangle(p1, p2, p3)
            if triangle.contains_point(p):
                print("YES")
            else:
                print("NO")


if __name__ == "__main__":
    solver = TrianglePointInclusionSolver()
    solver.solve()