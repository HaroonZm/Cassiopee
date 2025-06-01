from abc import ABC, abstractmethod
from math import sqrt
from typing import List, Iterator, Optional


class Dimension(ABC):
    @abstractmethod
    def minimal_enclosing_circle_diameter(self) -> float:
        pass


class Parallelepiped(Dimension):
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def minimal_enclosing_circle_diameter(self) -> float:
        # To pass through a circular hole without touching, cheese's minimal enclosing circle diameter must be <= hole diameter.
        # We consider the minimal diameter of a circle that can enclose the cheese in some orientation.
        # The minimal enclosing circle diameter is the minimal diagonal of a rectangle formed by any two dimensions.
        # Since the cheese can be rotated, the minimal diameter is the minimal length of the rectangle diagonal from any pair of edges.
        diagonals = [
            sqrt(self.a ** 2 + self.b ** 2),
            sqrt(self.b ** 2 + self.c ** 2),
            sqrt(self.a ** 2 + self.c ** 2),
        ]
        return min(diagonals)


class Hole(ABC):
    @abstractmethod
    def can_pass(self, cheese: Dimension) -> bool:
        pass


class CircularHole(Hole):
    def __init__(self, radius: float):
        self.radius = radius

    def can_pass(self, cheese: Dimension) -> bool:
        # Cheese must fit inside the diameter of the hole, strictly less or equal to hole diameter (2*radius)
        diameter = cheese.minimal_enclosing_circle_diameter()
        return diameter <= 2 * self.radius


class InputParser:
    def __init__(self, lines: Iterator[str]):
        self.lines = lines

    def parse_next_dataset(self) -> Optional[tuple[Parallelepiped, List[CircularHole]]]:
        while True:
            try:
                line = next(self.lines).strip()
            except StopIteration:
                return None

            if not line:
                continue
            parts = line.split()
            if len(parts) != 3:
                # Expected always 3 numbers for cheese dimensions or end case
                continue
            a, b, c = map(int, parts)
            if a == 0 and b == 0 and c == 0:
                return None  # End of input
            cheese = Parallelepiped(a, b, c)
            break

        # Number of holes
        n = int(next(self.lines).strip())
        holes: List[CircularHole] = []
        for _ in range(n):
            r = float(next(self.lines).strip())
            holes.append(CircularHole(r))
        return cheese, holes


class JerryCheeseTransporter:
    def __init__(self):
        self.parser = InputParser(iter(self._read_all_lines()))

    def _read_all_lines(self) -> List[str]:
        # For realistic usage, we'd read from stdin
        # But to keep abstraction and possible extension, we provide this method to override or mock
        import sys
        return sys.stdin.read().strip().split('\n')

    def run(self):
        while True:
            dataset = self.parser.parse_next_dataset()
            if dataset is None:
                break
            cheese, holes = dataset
            results = self._evaluate_holes(cheese, holes)
            for result in results:
                print(result)

    def _evaluate_holes(self, cheese: Parallelepiped, holes: List[CircularHole]) -> List[str]:
        results = []
        for hole in holes:
            if hole.can_pass(cheese):
                results.append("OK")
            else:
                results.append("NA")
        return results


if __name__ == "__main__":
    transporter = JerryCheeseTransporter()
    transporter.run()