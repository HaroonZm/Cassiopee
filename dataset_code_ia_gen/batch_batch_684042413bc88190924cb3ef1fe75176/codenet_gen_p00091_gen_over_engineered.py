from typing import List, Tuple, Dict, Iterator, Optional
from abc import ABC, abstractmethod
from collections import Counter, deque
import copy

Coordinate = Tuple[int, int]

class DyeSize(ABC):
    """Abstract base class representing the dye size with its diffusion pattern."""
    size_value: int
    diffusion_pattern: List[Coordinate]

    @classmethod
    @abstractmethod
    def valid_positions(cls, center: Coordinate) -> Iterator[Coordinate]:
        """Yield all affected coordinates on the cloth for a given center."""
        pass

    @classmethod
    def fits_in_field(cls, center: Coordinate, field_size: int) -> bool:
        """Check if the diffusion fits fully inside the field (0<=x,y<field_size)."""
        for x_off, y_off in cls.diffusion_pattern:
            x, y = center[0] + x_off, center[1] + y_off
            if not (0 <= x < field_size and 0 <= y < field_size):
                return False
        return True

    @classmethod
    def affected_cells(cls, center: Coordinate) -> List[Coordinate]:
        """Return all coordinates affected by placing dye at center."""
        return [(center[0] + dx, center[1] + dy) for dx, dy in cls.diffusion_pattern]

class SmallDye(DyeSize):
    size_value = 1
    diffusion_pattern = [
        (0, 0),
        (-1, 0), (1, 0), (0, -1), (0, 1)
    ]

    @classmethod
    def valid_positions(cls, center: Coordinate) -> Iterator[Coordinate]:
        # Always 5 cells, but must be inside boundaries
        if cls.fits_in_field(center, 10):
            yield center

class MediumDye(DyeSize):
    size_value = 2
    diffusion_pattern = [
        (0,0),
        (-1,0),(1,0),(0,-1),(0,1),
        (-1,-1), (-1,1), (1,-1), (1,1)
    ]

    @classmethod
    def valid_positions(cls, center: Coordinate) -> Iterator[Coordinate]:
        if cls.fits_in_field(center,10):
            yield center

class LargeDye(DyeSize):
    size_value = 3
    diffusion_pattern = [
        (0,0),
        (-1,0),(1,0),(0,-1),(0,1),
        (-2,0),(2,0),(0,-2),(0,2),
        (-1,-1), (-1,1), (1,-1), (1,1)
    ]

    @classmethod
    def valid_positions(cls, center: Coordinate) -> Iterator[Coordinate]:
        if cls.fits_in_field(center,10):
            yield center

ALL_DYE_CLASSES = [LargeDye, MediumDye, SmallDye]

class Cloth:
    def __init__(self, grid: List[List[int]]):
        self.size = 10
        # Deep copy to avoid mutation outside
        self.grid = copy.deepcopy(grid)

    def increment_cells(self, cells: List[Coordinate]) -> None:
        for x,y in cells:
            self.grid[y][x] += 1

    def decrement_cells(self, cells: List[Coordinate]) -> None:
        for x,y in cells:
            self.grid[y][x] -= 1

    def can_subtract(self, cells: List[Coordinate]) -> bool:
        # Check if all affected cells have at least 1 in grid (to subtract 1 safely)
        for x,y in cells:
            if not (0 <= x < self.size and 0 <= y < self.size):
                return False
            if self.grid[y][x] <= 0:
                return False
        return True

    def is_all_zero(self) -> bool:
        return all(all(v == 0 for v in row) for row in self.grid)

    def to_tuple(self) -> Tuple[Tuple[int,...], ...]:
        return tuple(tuple(row) for row in self.grid)

class DyePlacement:
    def __init__(self, x: int, y: int, dye_class: DyeSize):
        self.x = x
        self.y = y
        self.dye_class = dye_class

    def affected_cells(self) -> List[Coordinate]:
        return self.dye_class.affected_cells((self.x, self.y))

    def __repr__(self):
        return f'{self.dye_class.size_value} {self.x} {self.y}'

class DyeReconstructor:
    def __init__(self, drops_count: int, final_cloth: Cloth):
        self.drops_count = drops_count
        self.final_cloth = final_cloth
        self.size = final_cloth.size
        self.solutions: List[List[DyePlacement]] = []
        self.seen_states = set()

    def is_possible_placement(self, placement: DyePlacement, cloth: Cloth) -> bool:
        return cloth.can_subtract(placement.affected_cells())

    def backtrack(self, cloth: Cloth,
                  depth: int,
                  placements: List[DyePlacement]) -> Optional[List[DyePlacement]]:
        # Memoize by state and remaining depth to reduce computations
        state_key = (cloth.to_tuple(), depth)
        if state_key in self.seen_states:
            return None
        self.seen_states.add(state_key)

        if depth == 0:
            if cloth.is_all_zero():
                return placements[:]
            else:
                return None

        # Try all possible placements from large to small dye at all valid positions
        for dye_cls in ALL_DYE_CLASSES:
            max_c = self.size - 1
            # Because diffusion pattern fits fully, allowed positions are those where the dye fits
            for y in range(self.size):
                for x in range(self.size):
                    if dye_cls.fits_in_field((x,y), self.size):
                        placement = DyePlacement(x, y, dye_cls)
                        if self.is_possible_placement(placement, cloth):
                            # Try this placement: subtract affected cells from cloth grid
                            cloth.decrement_cells(placement.affected_cells())
                            placements.append(placement)
                            result = self.backtrack(cloth, depth - 1, placements)
                            if result is not None:
                                return result
                            placements.pop()
                            # Restore cloth grid
                            cloth.increment_cells(placement.affected_cells())
        return None

def main():
    from sys import stdin, stdout
    n = int(stdin.readline())
    grid = []
    for _ in range(10):
        grid.append(list(map(int, stdin.readline().split())))
    cloth = Cloth(grid)
    reconstructor = DyeReconstructor(n, cloth)
    answer = reconstructor.backtrack(cloth, n, [])
    # Output as requested: For each drop, line with x y size (size 3,2,1), order any
    # Solution stores (x,y,size). Output format: size x y
    # But spec requires: size x y as "size x y" or "x y size" ?
    # Problem states: output n lines with x y size (size 3=large,2=medium,1=small)
    # output n lines x y size separated by space
    if answer is not None:
        for dp in answer:
            stdout.write(f'{dp.x} {dp.y} {dp.dye_class.size_value}\n')
    else:
        # Problem does not state what to do if no solution
        pass

if __name__ == '__main__':
    main()