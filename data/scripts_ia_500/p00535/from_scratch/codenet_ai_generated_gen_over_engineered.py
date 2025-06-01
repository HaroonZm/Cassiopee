from __future__ import annotations
from typing import List, Tuple, Set, Dict, Protocol
import sys
import collections


class Coordinate:
    __slots__ = ('row', 'col')

    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col

    def neighbors(self, max_row: int, max_col: int) -> List[Coordinate]:
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        result = []
        for dr, dc in directions:
            nr, nc = self.row + dr, self.col + dc
            if 0 <= nr < max_row and 0 <= nc < max_col:
                result.append(Coordinate(nr, nc))
        return result

    def __hash__(self) -> int:
        return hash((self.row, self.col))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Coordinate):
            return False
        return self.row == other.row and self.col == other.col


class CellType(Protocol):
    def is_sandcastle(self) -> bool:
        ...

    def strength(self) -> int:
        ...


class SandcastleCell:
    __slots__ = ('strength_val',)

    def __init__(self, strength_val: int) -> None:
        self.strength_val = strength_val

    def is_sandcastle(self) -> bool:
        return True

    def strength(self) -> int:
        return self.strength_val


class PlainCell:
    __slots__ = ()

    def __init__(self) -> None:
        pass

    def is_sandcastle(self) -> bool:
        return False

    def strength(self) -> int:
        return 0


class SandcastleGrid:
    __slots__ = ('height', 'width', 'grid')

    def __init__(self, height: int, width: int, grid_data: List[str]) -> None:
        self.height = height
        self.width = width
        self.grid: List[List[CellType]] = [
            [self._parse_cell(ch) for ch in row] for row in grid_data
        ]

    def _parse_cell(self, ch: str) -> CellType:
        if ch == '.':
            return PlainCell()
        else:
            return SandcastleCell(int(ch))

    def is_in_bounds(self, coord: Coordinate) -> bool:
        return 0 <= coord.row < self.height and 0 <= coord.col < self.width

    def cell_at(self, coord: Coordinate) -> CellType:
        return self.grid[coord.row][coord.col]

    def set_plain(self, coord: Coordinate) -> None:
        self.grid[coord.row][coord.col] = PlainCell()

    def count_plain_neighbors(self, coord: Coordinate) -> int:
        count = 0
        for n in coord.neighbors(self.height, self.width):
            if not self.cell_at(n).is_sandcastle():
                count += 1
        return count


class WaveCollapseSimulator:
    __slots__ = ('grid', 'waves_count', 'candidates')

    def __init__(self, grid: SandcastleGrid) -> None:
        self.grid = grid
        self.waves_count = 0
        # Initially all castle cells potentially can collapse if neighbors are plains:
        self.candidates: Set[Coordinate] = set(
            Coordinate(r, c)
            for r in range(self.grid.height)
            for c in range(self.grid.width)
            if self.grid.grid[r][c].is_sandcastle()
        )

    def simulate(self) -> int:
        """
        Runs the simulation until stable state achieved,
        returns the number of waves that cause any collapse.
        """
        while True:
            to_collapse = self._find_collapsing_cells()
            if not to_collapse:
                break
            self._apply_collapse(to_collapse)
            self.waves_count += 1
        return self.waves_count

    def _find_collapsing_cells(self) -> Set[Coordinate]:
        collapsing: Set[Coordinate] = set()
        for coord in self.candidates:
            cell = self.grid.cell_at(coord)
            if cell.is_sandcastle():
                plains_adjacent = self.grid.count_plain_neighbors(coord)
                if plains_adjacent >= cell.strength():
                    collapsing.add(coord)
        return collapsing

    def _apply_collapse(self, collapsing_cells: Set[Coordinate]) -> None:
        # Update cells to plain and update candidates to neighbors (because neighbors might now collapse)
        new_candidates: Set[Coordinate] = set()
        for coord in collapsing_cells:
            self.grid.set_plain(coord)
        for coord in collapsing_cells:
            # neighbors might be affected next iteration
            for n in coord.neighbors(self.grid.height, self.grid.width):
                if self.grid.cell_at(n).is_sandcastle():
                    new_candidates.add(n)
        # Candidates for next iteration: all non-collapsed cells that neighbor collapsed cells
        # plus any that were candidates but not collapsed (some might remain)
        # To avoid redundant large sets, keep intersection with existing candidates
        self.candidates = new_candidates


def read_input() -> Tuple[int, int, List[str]]:
    input = sys.stdin.readline
    H, W = map(int, input().split())
    grid_lines = [input().rstrip('\n') for _ in range(H)]
    return H, W, grid_lines


def main() -> None:
    H, W, grid_data = read_input()
    grid = SandcastleGrid(H, W, grid_data)
    simulator = WaveCollapseSimulator(grid)
    answer = simulator.simulate()
    print(answer)


if __name__ == '__main__':
    main()