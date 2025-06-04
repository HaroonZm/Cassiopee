from typing import List, Tuple
from math import sqrt
from enum import IntEnum

FLOAT_COMPARISON_EPSILON = 1e-10

def are_floats_equal(first_value: float, second_value: float) -> bool:
    return abs(first_value - second_value) < FLOAT_COMPARISON_EPSILON

class PointLocationType(IntEnum):
    COUNTER_CLOCKWISE = 1
    CLOCKWISE = -1
    ONLINE_BACK = 2
    ONLINE_FRONT = -2
    ON_SEGMENT = 0

PL = PointLocationType

class Point2D:

    def __init__(self, coordinate_x: float = 0.0, coordinate_y: float = 0.0) -> None:
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y

    def __repr__(self) -> str:
        return f"Point2D({self.coordinate_x}, {self.coordinate_y})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point2D):
            return NotImplemented
        return are_floats_equal(self.coordinate_x, other.coordinate_x) and \
               are_floats_equal(self.coordinate_y, other.coordinate_y)

    def __add__(self, other: 'Point2D') -> 'Point2D':
        return Point2D(self.coordinate_x + other.coordinate_x, self.coordinate_y + other.coordinate_y)

    def __sub__(self, other: 'Point2D') -> 'Point2D':
        return Point2D(self.coordinate_x - other.coordinate_x, self.coordinate_y - other.coordinate_y)

    def __mul__(self, scalar: float) -> 'Point2D':
        return Point2D(self.coordinate_x * scalar, self.coordinate_y * scalar)

    def __rmul__(self, scalar: float) -> 'Point2D':
        return self * scalar

    def __truediv__(self, scalar: float) -> 'Point2D':
        return Point2D(self.coordinate_x / scalar, self.coordinate_y / scalar)

    def __lt__(self, other: 'Point2D') -> bool:
        if abs(self.coordinate_x - other.coordinate_x) < FLOAT_COMPARISON_EPSILON:
            return self.coordinate_y < other.coordinate_y
        else:
            return self.coordinate_x < other.coordinate_x

    def squared_norm(self) -> float:
        return self.coordinate_x * self.coordinate_x + self.coordinate_y * self.coordinate_y

    def magnitude(self) -> float:
        return sqrt(self.squared_norm())

    def dot_product(self, other: 'Point2D') -> float:
        return self.coordinate_x * other.coordinate_x + self.coordinate_y * other.coordinate_y

    def cross_product(self, other: 'Point2D') -> float:
        return self.coordinate_x * other.coordinate_y - self.coordinate_y * other.coordinate_x

    def is_orthogonal_to(self, other: 'Point2D') -> bool:
        return are_floats_equal(self.dot_product(other), 0.0)

    def is_parallel_to(self, other: 'Point2D') -> bool:
        return are_floats_equal(self.cross_product(other), 0.0)

    def distance_to(self, other: 'Point2D') -> float:
        return (self - other).magnitude()

    def is_on_segment_side(self, segment: 'LineSegment2D') -> bool:
        return segment.direction_vector().dot_product(
            LineSegment2D(segment.point1, self).direction_vector()) >= 0

    def is_between_segment_ends(self, segment: 'LineSegment2D') -> bool:
        return self.is_on_segment_side(segment) and self.is_on_segment_side(segment.reversed())

    def distance_to_line(self, segment: 'LineSegment2D') -> float:
        return abs((self - segment.point1).cross_product(segment.direction_vector())) / segment.length()

    def distance_to_segment(self, segment: 'LineSegment2D') -> float:
        if not self.is_on_segment_side(segment):
            return self.distance_to(segment.point1)
        if not self.is_on_segment_side(segment.reversed()):
            return self.distance_to(segment.point2)
        else:
            return self.distance_to_line(segment)

    def location_relative_to_segment(self, segment: 'LineSegment2D') -> PointLocationType:
        relative_position_vector = self - segment.point1
        cross_value = segment.direction_vector().cross_product(relative_position_vector)

        if cross_value > FLOAT_COMPARISON_EPSILON:
            return PointLocationType.COUNTER_CLOCKWISE

        if cross_value < -FLOAT_COMPARISON_EPSILON:
            return PointLocationType.CLOCKWISE

        if segment.direction_vector().dot_product(relative_position_vector) < 0.0:
            return PointLocationType.ONLINE_BACK

        if segment.direction_vector().squared_norm() < relative_position_vector.squared_norm():
            return PointLocationType.ONLINE_FRONT

        return PointLocationType.ON_SEGMENT

Vector2D = Point2D

class LineSegment2D:

    def __init__(self, point1: Point2D = None, point2: Point2D = None) -> None:
        self.point1: Point2D = Point2D() if point1 is None else point1
        self.point2: Point2D = Point2D() if point2 is None else point2

    def __repr__(self) -> str:
        return f"LineSegment2D({self.point1}, {self.point2})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, LineSegment2D):
            return NotImplemented
        return self.point1 == other.point1 and self.point2 == other.point2

    def direction_vector(self) -> Vector2D:
        return self.point2 - self.point1

    def reversed(self) -> 'LineSegment2D':
        return LineSegment2D(self.point2, self.point1)

    def length(self) -> float:
        return self.point1.distance_to(self.point2)

    def is_orthogonal_to(self, other: 'LineSegment2D') -> bool:
        return self.direction_vector().is_orthogonal_to(other.direction_vector())

    def is_parallel_to(self, other: 'LineSegment2D') -> bool:
        return self.direction_vector().is_parallel_to(other.direction_vector())

    def projection_of_point(self, point: Point2D) -> Point2D:
        segment_vector = self.direction_vector()
        vector_from_point1 = point - self.point1
        projection_ratio = segment_vector.dot_product(vector_from_point1) / segment_vector.squared_norm()
        return projection_ratio * segment_vector + self.point1

    def reflection_of_point(self, point: Point2D) -> Point2D:
        projected_point = self.projection_of_point(point)
        return point + 2 * (projected_point - point)

    def intersection_ratios_with(self, other_segment: 'LineSegment2D') -> Tuple[float, float]:
        vector_a = self.direction_vector()
        vector_b = other_segment.direction_vector()
        offset_vector = self.point1 - other_segment.point1
        denominator = vector_a.cross_product(vector_b)
        s_ratio = vector_b.cross_product(offset_vector) / denominator
        t_ratio = vector_a.cross_product(offset_vector) / denominator
        return s_ratio, t_ratio

    def does_intersect_with(self, other_segment: 'LineSegment2D') -> bool:
        location1 = self.point1.location_relative_to_segment(other_segment)
        location2 = self.point2.location_relative_to_segment(other_segment)
        location3 = other_segment.point1.location_relative_to_segment(self)
        location4 = other_segment.point2.location_relative_to_segment(self)

        return location1 * location2 * location3 * location4 == 0 or \
            (location1 * location2 == -1 and location3 * location4 == -1)

    def intersection_point_with(self, other_segment: 'LineSegment2D') -> Point2D:
        s_ratio, _ = self.intersection_ratios_with(other_segment)
        return self.point1 + s_ratio * self.direction_vector()

    def minimum_distance_to_segment(self, other_segment: 'LineSegment2D') -> float:
        if not self.is_parallel_to(other_segment) and self.does_intersect_with(other_segment):
            return 0
        else:
            return min(
                self.point1.distance_to_segment(other_segment),
                self.point2.distance_to_segment(other_segment),
                other_segment.point1.distance_to_segment(self),
                other_segment.point2.distance_to_segment(self))

Line2D = LineSegment2D

class Circle2D:

    def __init__(self, center_point: Point2D = None, radius_value: float = 0.0) -> None:
        self.center: Point2D = Point2D() if center_point is None else center_point
        self.radius: float = radius_value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Circle2D):
            return NotImplemented
        return self.center == other.center and self.radius == other.radius

    def __repr__(self) -> str:
        return f"Circle2D({self.center}, {self.radius})"

def main() -> None:
    number_of_queries = int(input())

    for _ in range(number_of_queries):
        x0, y0, x1, y1, x2, y2, x3, y3 = [int(value) for value in input().split()]

        first_segment = LineSegment2D(Point2D(x0, y0), Point2D(x1, y1))
        second_segment = LineSegment2D(Point2D(x2, y2), Point2D(x3, y3))

        print(1 if first_segment.does_intersect_with(second_segment) else 0)

if __name__ == "__main__":
    main()