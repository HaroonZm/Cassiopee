#!/usr/bin/env python3

from typing import List
from math import sqrt

# Tolerance used to compare floating point numbers for equality.
EPS = 1e-10

def float_equal(x: float, y: float) -> bool:
    """
    Compare two floating point numbers for approximate equality, using a tolerance.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        bool: True if x and y are close (difference less than EPS), False otherwise.
    """
    return abs(x - y) < EPS

class Point:
    """
    Class that represents a point or a vector in 2D Euclidean space.
    Supports common vector operations and comparisons.
    """

    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        """
        Initialize a Point with coordinates (x, y).

        Args:
            x (float, optional): X-coordinate. Defaults to 0.0.
            y (float, optional): Y-coordinate. Defaults to 0.0.
        """
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """
        String representation of Point for debugging.

        Returns:
            str: String describing the point.
        """
        return "Point({}, {})".format(self.x, self.y)

    def __eq__(self, other: object) -> bool:
        """
        Compare Points for equality, with floating-point tolerance.

        Args:
            other (object): The object to compare to.

        Returns:
            bool: True if both points are equal, False otherwise.
        """
        if not isinstance(other, Point):
            return NotImplemented
        return float_equal(self.x, other.x) and float_equal(self.y, other.y)

    def __add__(self, other: 'Point') -> 'Point':
        """
        Add two points as vectors.

        Args:
            other (Point): The point/vector to add.

        Returns:
            Point: The resulting point.
        """
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Point') -> 'Point':
        """
        Subtract two points as vectors.

        Args:
            other (Point): The point/vector to subtract.

        Returns:
            Point: The result of subtraction.
        """
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, k: float) -> 'Point':
        """
        Scale the vector by a scalar k.

        Args:
            k (float): Scalar value.

        Returns:
            Point: Scaled vector.
        """
        return Point(self.x * k, self.y * k)

    def __rmul__(self, k: float) -> 'Point':
        """
        Allow left multiplication by a scalar.

        Args:
            k (float): Scalar value.

        Returns:
            Point: Scaled vector.
        """
        return self * k

    def __truediv__(self, k: float) -> 'Point':
        """
        Divide the vector by a scalar k.

        Args:
            k (float): Scalar value.

        Returns:
            Point: Scaled vector.
        """
        return Point(self.x / k, self.y / k)

    def __lt__(self, other: 'Point') -> bool:
        """
        Compare Points for less-than, using x first, then y; with floating-point tolerance.

        Args:
            other (Point): The point to compare to.

        Returns:
            bool: True if self is less than other, False otherwise.
        """
        return self.y < other.y if abs(self.x - other.x) < EPS else self.x < other.x

    def norm(self) -> float:
        """
        Compute the squared length of the vector.

        Returns:
            float: The squared magnitude (norm) of the vector.
        """
        return self.x * self.x + self.y * self.y

    def abs(self) -> float:
        """
        Compute the Euclidean norm (length) of the vector.

        Returns:
            float: The magnitude (length) of the vector.
        """
        return sqrt(self.norm())

    def dot(self, other: 'Point') -> float:
        """
        Compute the dot product of self and another vector.

        Args:
            other (Point): The other vector.

        Returns:
            float: The dot product.
        """
        return self.x * other.x + self.y * other.y

    def cross(self, other: 'Point') -> float:
        """
        Compute the 2D cross product (scalar).

        Args:
            other (Point): The other vector.

        Returns:
            float: The cross product (determinant).
        """
        return self.x * other.y - self.y * other.x

    def is_orthogonal(self, other: 'Point') -> bool:
        """
        Check if two vectors are orthogonal (perpendicular).

        Args:
            other (Point): The other vector.

        Returns:
            bool: True if vectors are orthogonal, False otherwise.
        """
        return float_equal(self.dot(other), 0.0)

    def is_parallel(self, other: 'Point') -> bool:
        """
        Check if two vectors are parallel.

        Args:
            other (Point): The other vector.

        Returns:
            bool: True if vectors are parallel, False otherwise.
        """
        return float_equal(self.cross(other), 0.0)

# For consistency, we alias Vector as Point.
Vector = Point

class Segment:
    """
    Represents a segment or a line in 2D space, defined by two points p1 and p2.
    Provides geometric operations and comparisons.
    """

    def __init__(self, p1: Point = None, p2: Point = None) -> None:
        """
        Initialize a Segment with two points.

        Args:
            p1 (Point, optional): First endpoint. Defaults to origin if None.
            p2 (Point, optional): Second endpoint. Defaults to origin if None.
        """
        self.p1: Point = Point() if p1 is None else p1
        self.p2: Point = Point() if p2 is None else p2

    def __repr__(self) -> str:
        """
        String representation of Segment for debugging.

        Returns:
            str: String describing the segment.
        """
        return "Segment({}, {})".format(self.p1, self.p2)

    def __eq__(self, other: object) -> bool:
        """
        Check equality for Segments.

        Args:
            other (object): The object to compare.

        Returns:
            bool: True if segments are equal, False otherwise.
        """
        if not isinstance(other, Segment):
            return NotImplemented
        return self.p1 == other.p1 and self.p2 == other.p2

    def vector(self) -> Vector:
        """
        Return the vector representing the direction of the segment.

        Returns:
            Vector: The vector p2 - p1.
        """
        return self.p2 - self.p1

    def is_orthogonal(self, other: 'Segment') -> bool:
        """
        Check if this segment is orthogonal (perpendicular) to another.

        Args:
            other (Segment): The other segment.

        Returns:
            bool: True if segments are orthogonal, False otherwise.
        """
        return self.vector().is_orthogonal(other.vector())

    def is_parallel(self, other: 'Segment') -> bool:
        """
        Check if this segment is parallel to another.

        Args:
            other (Segment): The other segment.

        Returns:
            bool: True if segments are parallel, False otherwise.
        """
        return self.vector().is_parallel(other.vector())

    def projection(self, p: Point) -> Point:
        """
        Project point p orthogonally onto this segment (line).

        Args:
            p (Point): The point to project.

        Returns:
            Point: The projected point on the line.
        """
        v = self.vector()
        vp = p - self.p1
        # (v.dot(vp) / v.norm()) gives the scale for projection on v
        return v.dot(vp) / v.norm() * v + self.p1

    def reflection(self, p: Point) -> Point:
        """
        Return the reflection of point p over this segment (line).

        Args:
            p (Point): The point to reflect.

        Returns:
            Point: The reflected point.
        """
        x = self.projection(p)
        return p + 2 * (x - p)

# Alias for a line object; all methods apply equally to lines and segments for the required operations.
Line = Segment

class Circle:
    """
    Represents a circle in 2D space, defined by center and radius.
    """

    def __init__(self, c: Point = None, r: float = 0.0) -> None:
        """
        Initialize a Circle with center and radius.

        Args:
            c (Point, optional): Center of the circle. Defaults to origin if None.
            r (float, optional): Radius of the circle. Defaults to 0.0.
        """
        self.c: Point = Point() if c is None else c
        self.r: float = r

    def __eq__(self, other: object) -> bool:
        """
        Check equality for circles.

        Args:
            other (object): The object to compare.

        Returns:
            bool: True if circles have same center and radius, False otherwise.
        """
        if not isinstance(other, Circle):
            return NotImplemented
        return self.c == other.c and self.r == other.r

    def __repr__(self) -> str:
        """
        String representation of Circle for debugging.

        Returns:
            str: String describing the circle.
        """
        return "Circle({}, {})".format(self.c, self.r)

def main() -> None:
    """
    Entry point of the program.
    Reads a line (as two points) and several points,
    then prints the reflection of each point over that line.
    Input & output are assumed in a format compatible with competitive programming problems.
    """
    # Read coordinates for the line
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    l = Line(p1, p2)

    # Read number of queries
    q = int(input())

    # Process each query: reflect point (x, y) over line l and print result
    for _ in range(q):
        x, y = [int(x) for x in input().split()]
        p = Point(x, y)
        a = l.reflection(p)
        print(a.x, a.y)

if __name__ == "__main__":
    main()