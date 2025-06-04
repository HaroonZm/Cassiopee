import sys
import math
from abc import ABC, abstractmethod
from typing import Tuple, Iterator, List


class Triangle(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class IsoscelesTriangle(Triangle):
    def __init__(self, base: float, side: float):
        self.base = base
        self.side = side

    def area(self) -> float:
        # Using Heron's formula
        s = (self.base + 2 * self.side) / 2
        area = math.sqrt(s * (s - self.base) * (s - self.side) * (s - self.side))
        return area


class ExtendedSkinAreaOptimizer:
    """
    This class models the original triangle ABC and the problem of
    adding slack length x on the two equal sides AC=BC, creating new triangles ADC and BEC
    on the outside of ABC, maximizing the total visible area M.
    """

    def __init__(self, a: float, l: float, x: float):
        self.a = a
        self.l = l
        self.x = x

    def original_area(self) -> float:
        """Area of original isosceles triangle ABC"""
        base = self.a
        side = self.l
        return IsoscelesTriangle(base, side).area()

    def max_extended_area(self) -> float:
        """
        Compute the maximum combined area M = area(ABC) + area(ADC) + area(BEC)
        according to the problem constraints.
        """

        # By problem geometry, the maximum area is achieved when
        # the slack length x is split equally on both sides AC and BC,
        # and the new triangles ADC and BEC are "folded outwards" symmetrically
        # forming a larger isosceles figure with the total length l + x on each side
        # The known formula from analysis:
        # max area = (a/4)* sqrt(4(l+x)^2 - a^2)

        extended_side = self.l + self.x
        # Check for numerical correctness, 4(side)^2 - base^2 must be >= 0
        val = 4 * (extended_side ** 2) - (self.a ** 2)
        if val < 0:
            val = 0

        max_area = (self.a / 4) * math.sqrt(val)
        return max_area


class InputParser:
    """
    Parses input lines of format "a l x" until EOF, yielding tuples of (a, l, x)
    """

    def __init__(self, stream):
        self.stream = stream

    def parse(self) -> Iterator[Tuple[int, int, int]]:
        for line in self.stream:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) != 3:
                continue
            try:
                a, l, x = map(int, parts)
                yield a, l, x
            except Exception:
                continue


class AreaPrinter:
    """
    Responsible for output formatting of the area result
    """

    @staticmethod
    def print_area(area: float):
        # Print with precision such that difference <= 10^-5
        print(f"{area:.10f}")


def main():
    parser = InputParser(sys.stdin)
    printer = AreaPrinter()

    for a, l, x in parser.parse():
        optimizer = ExtendedSkinAreaOptimizer(a, l, x)
        max_area = optimizer.max_extended_area()
        printer.print_area(max_area)


if __name__ == "__main__":
    main()