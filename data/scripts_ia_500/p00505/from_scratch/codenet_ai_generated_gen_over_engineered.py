from abc import ABC, abstractmethod
from typing import List, Tuple, Optional, Iterator


class TriangleType:
    ACUTE = "鋭角三角形"
    RIGHT = "直角三角形"
    OBTUSE = "鈍角三角形"

    @classmethod
    def all_types(cls):
        return [cls.ACUTE, cls.RIGHT, cls.OBTUSE]


class TriangleSideLengths:
    def __init__(self, sides: List[int]):
        if len(sides) != 3:
            raise ValueError("Exactly three side lengths must be provided.")
        self.sides = sorted(sides)

    @property
    def a(self):
        return self.sides[0]

    @property
    def b(self):
        return self.sides[1]

    @property
    def c(self):
        return self.sides[2]

    def is_valid_triangle(self) -> bool:
        # Triangle inequality theorem
        return self.a + self.b > self.c

    def classify_angle(self) -> str:
        a2 = self.a ** 2
        b2 = self.b ** 2
        c2 = self.c ** 2
        if a2 + b2 > c2:
            return TriangleType.ACUTE
        elif a2 + b2 == c2:
            return TriangleType.RIGHT
        else:
            return TriangleType.OBTUSE


class TriangleStats:
    def __init__(self):
        self.total_triangles = 0
        self.acute_count = 0
        self.right_count = 0
        self.obtuse_count = 0

    def record_triangle(self, triangle_type: str):
        self.total_triangles += 1
        if triangle_type == TriangleType.ACUTE:
            self.acute_count += 1
        elif triangle_type == TriangleType.RIGHT:
            self.right_count += 1
        elif triangle_type == TriangleType.OBTUSE:
            self.obtuse_count += 1

    def summary(self) -> str:
        # order: total triangles, right, acute, obtuse
        return f"{self.total_triangles} {self.right_count} {self.acute_count} {self.obtuse_count}"


class TriangleProcessor(ABC):
    def __init__(self):
        self.stats = TriangleStats()

    @abstractmethod
    def get_next_sides(self) -> Optional[TriangleSideLengths]:
        pass

    def process(self) -> None:
        while True:
            sides = self.get_next_sides()
            if sides is None:
                # No more input, break safely
                break
            if not sides.is_valid_triangle():
                # Output summary and break on invalid triangle
                print(self.stats.summary())
                break
            triangle_type = sides.classify_angle()
            self.stats.record_triangle(triangle_type)


class InputTriangleProcessor(TriangleProcessor):
    def __init__(self, input_source: Iterator[str]):
        super().__init__()
        self.input_source = input_source

    def get_next_sides(self) -> Optional[TriangleSideLengths]:
        while True:
            try:
                line = next(self.input_source)
            except StopIteration:
                return None
            stripped = line.strip()
            if not stripped:
                continue
            parts = stripped.split()
            # Only consider first 3 integers if there are more
            try:
                values = [int(part) for part in parts[:3]]
            except ValueError:
                # If any part is not integer, ignore this line and continue
                continue
            # Validate sides according to problem constraints
            if any(v <= 0 or v > 100 for v in values):
                continue
            return TriangleSideLengths(values)


def main():
    import sys

    processor = InputTriangleProcessor(iter(sys.stdin))
    processor.process()


if __name__ == "__main__":
    main()