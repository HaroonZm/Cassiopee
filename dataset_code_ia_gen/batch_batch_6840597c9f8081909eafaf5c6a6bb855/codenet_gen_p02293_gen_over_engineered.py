class Point:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    def __sub__(self, other: "Point") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)


class Vector:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    def dot(self, other: "Vector") -> int:
        return self.x * other.x + self.y * other.y

    def cross(self, other: "Vector") -> int:
        return self.x * other.y - self.y * other.x

    def is_parallel_to(self, other: "Vector") -> bool:
        # Two vectors are parallel if their cross product is zero
        return self.cross(other) == 0

    def is_orthogonal_to(self, other: "Vector") -> bool:
        # Two vectors are orthogonal if their dot product is zero
        return self.dot(other) == 0


class Line:
    def __init__(self, p0: Point, p1: Point):
        if p0.x == p1.x and p0.y == p1.y:
            raise ValueError("A line cannot be formed by two identical points")
        self._p0 = p0
        self._p1 = p1
        self._direction = p1 - p0

    @property
    def direction(self) -> Vector:
        return self._direction

    def is_parallel_to(self, other: "Line") -> bool:
        return self.direction.is_parallel_to(other.direction)

    def is_orthogonal_to(self, other: "Line") -> bool:
        return self.direction.is_orthogonal_to(other.direction)


class LineRelationshipEvaluator:
    PARALLEL = "2"
    ORTHOGONAL = "1"
    NONE = "0"

    @staticmethod
    def evaluate(line1: Line, line2: Line) -> str:
        if line1.is_parallel_to(line2):
            return LineRelationshipEvaluator.PARALLEL
        elif line1.is_orthogonal_to(line2):
            return LineRelationshipEvaluator.ORTHOGONAL
        else:
            return LineRelationshipEvaluator.NONE


class QueryProcessor:
    def __init__(self, queries_data: list[tuple[int, int, int, int, int, int, int, int]]):
        self._queries_data = queries_data

    def process(self) -> list[str]:
        results = []
        for data in self._queries_data:
            p0 = Point(data[0], data[1])
            p1 = Point(data[2], data[3])
            p2 = Point(data[4], data[5])
            p3 = Point(data[6], data[7])
            line1 = Line(p0, p1)
            line2 = Line(p2, p3)
            result = LineRelationshipEvaluator.evaluate(line1, line2)
            results.append(result)
        return results


def main():
    import sys

    input_lines = sys.stdin.read().strip().split()
    q = int(input_lines[0])
    coords = input_lines[1:]
    queries = []
    for i in range(q):
        subset = coords[i*8:(i+1)*8]
        point_coords = tuple(map(int, subset))
        queries.append(point_coords)
    processor = QueryProcessor(queries)
    results = processor.process()
    print("\n".join(results))


if __name__ == "__main__":
    main()