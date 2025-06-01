from typing import List, Tuple
from abc import ABC, abstractmethod
from itertools import permutations
import sys

class Cake:
    def __init__(self, radius: int):
        self.radius = radius

    def diameter(self) -> int:
        return 2 * self.radius

class Container(ABC):
    @abstractmethod
    def can_accommodate(self, cakes: List[Cake]) -> bool:
        ...

class Box(Container):
    def __init__(self, length: int):
        self.length = length

    def can_accommodate(self, cakes: List[Cake]) -> bool:
        arrangement_solver = ArrangementSolver(self.length, cakes)
        return arrangement_solver.solve()

class ArrangementSolver:
    def __init__(self, box_length: int, cakes: List[Cake]):
        self.box_length = box_length
        self.cakes = cakes

    def solve(self) -> bool:
        """
        Try all permutations to check if cakes can be placed side-by-side without overlapping 
        beyond box length, with all cakes touching the bottom line.
        """
        for perm in permutations(self.cakes):
            if self._fits_in_line(perm):
                return True
        return False

    def _fits_in_line(self, cakes_perm: Tuple[Cake]) -> bool:
        """
        Given an order, determine whether cakes placed tangent to each other starting at position 0
        fit into the box of length self.box_length.
        """

        # Place the first cake center at radius distance from the box start (0)
        positions = [cakes_perm[0].radius]

        # Sequentially determine each cake center position so that it just touches the previous cake
        for i in range(1, len(cakes_perm)):
            prev = cakes_perm[i-1]
            curr = cakes_perm[i]

            # Distance between centers to avoid overlap is sum of radii
            dist = prev.radius + curr.radius
            # Minimal position of current cake center = previous center + dist
            pos = positions[-1] + dist
            positions.append(pos)

        # The last cake center + its radius must not exceed box length
        last_cake = cakes_perm[-1]
        total_length = positions[-1] + last_cake.radius

        if total_length <= self.box_length:
            return True
        return False

class ProblemSolver:
    def __init__(self):
        self.data_sets: List[Tuple[int, List[int]]] = []

    def read_input(self):
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) < 2:
                continue
            length = int(parts[0])
            radii = list(map(int, parts[1:]))
            self.data_sets.append((length, radii))

    def solve_all(self):
        for length, radii in self.data_sets:
            box = Box(length)
            cakes = [Cake(r) for r in radii]
            result = box.can_accommodate(cakes)
            print("OK" if result else "NA")

def main():
    ps = ProblemSolver()
    ps.read_input()
    ps.solve_all()

if __name__ == "__main__":
    main()