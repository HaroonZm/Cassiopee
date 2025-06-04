from typing import List
from math import sqrt

CONSTANT_EPSILON = 1e-10

def is_float_equal(value_a: float, value_b: float) -> bool:
    return abs(value_a - value_b) < CONSTANT_EPSILON

class Point2D:

    def __init__(self, coord_x: float = 0.0, coord_y: float = 0.0) -> None:
        self.coord_x = coord_x
        self.coord_y = coord_y

    def __repr__(self) -> str:
        return f"Point2D({self.coord_x}, {self.coord_y})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point2D):
            return NotImplemented
        return is_float_equal(self.coord_x, other.coord_x) and is_float_equal(self.coord_y, other.coord_y)

    def __add__(self, other: 'Point2D') -> 'Point2D':
        return Point2D(self.coord_x + other.coord_x, self.coord_y + other.coord_y)

    def __sub__(self, other: 'Point2D') -> 'Point2D':
        return Point2D(self.coord_x - other.coord_x, self.coord_y - other.coord_y)

    def __mul__(self, scalar: float) -> 'Point2D':
        return Point2D(self.coord_x * scalar, self.coord_y * scalar)

    def __rmul__(self, scalar: float) -> 'Point2D':
        return self * scalar

    def __truediv__(self, scalar: float) -> 'Point2D':
        return Point2D(self.coord_x / scalar, self.coord_y / scalar)

    def __lt__(self, other: 'Point2D') -> bool:
        if abs(self.coord_x - other.coord_x) < CONSTANT_EPSILON:
            return self.coord_y < other.coord_y
        return self.coord_x < other.coord_x

    def get_squared_norm(self) -> float:
        return self.coord_x * self.coord_x + self.coord_y * self.coord_y

    def get_norm(self) -> float:
        return sqrt(self.get_squared_norm())

    def get_dot_product(self, other: 'Point2D') -> float:
        return self.coord_x * other.coord_x + self.coord_y * other.coord_y

    def get_cross_product(self, other: 'Point2D') -> float:
        return self.coord_x * other.coord_y - self.coord_y * other.coord_x

    def is_orthogonal_to(self, other: 'Point2D') -> bool:
        return is_float_equal(self.get_dot_product(other), 0.0)

    def is_parallel_to(self, other: 'Point2D') -> bool:
        return is_float_equal(self.get_cross_product(other), 0.0)

Vector2D = Point2D

class Segment2D:

    def __init__(self, endpoint_a: Point2D = None, endpoint_b: Point2D = None) -> None:
        self.endpoint_a: Point2D = Point2D() if endpoint_a is None else endpoint_a
        self.endpoint_b: Point2D = Point2D() if endpoint_b is None else endpoint_b

    def __repr__(self) -> str:
        return f"Segment2D({self.endpoint_a}, {self.endpoint_b})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Segment2D):
            return NotImplemented
        return self.endpoint_a == other.endpoint_a and self.endpoint_b == other.endpoint_b

    def get_vector(self) -> Vector2D:
        return self.endpoint_b - self.endpoint_a

    def is_orthogonal_to(self, other: 'Segment2D') -> bool:
        return self.get_vector().is_orthogonal_to(other.get_vector())

    def is_parallel_to(self, other: 'Segment2D') -> bool:
        return self.get_vector().is_parallel_to(other.get_vector())

Line2D = Segment2D

class Circle2D:

    def __init__(self, center_point: Point2D = None, radius: float = 0.0) -> None:
        self.center_point: Point2D = Point2D() if center_point is None else center_point
        self.radius: float = radius

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Circle2D):
            return NotImplemented
        return self.center_point == other.center_point and self.radius == other.radius

    def __repr__(self) -> str:
        return f"Circle2D({self.center_point}, {self.radius})"

def classify_segment_relationship(segment_a: Segment2D, segment_b: Segment2D) -> int:
    if segment_a.is_parallel_to(segment_b):
        return 2
    elif segment_a.is_orthogonal_to(segment_b):
        return 1
    else:
        return 0

def main_program() -> None:
    query_count = int(input())
    for _ in range(query_count):
        segment_one = Segment2D()
        segment_two = Segment2D()
        coords = [int(token) for token in input().split()]
        segment_one.endpoint_a.coord_x = coords[0]
        segment_one.endpoint_a.coord_y = coords[1]
        segment_one.endpoint_b.coord_x = coords[2]
        segment_one.endpoint_b.coord_y = coords[3]
        segment_two.endpoint_a.coord_x = coords[4]
        segment_two.endpoint_a.coord_y = coords[5]
        segment_two.endpoint_b.coord_x = coords[6]
        segment_two.endpoint_b.coord_y = coords[7]
        print(classify_segment_relationship(segment_one, segment_two))

if __name__ == "__main__":
    main_program()