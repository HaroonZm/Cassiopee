from typing import List, Tuple, Optional, Set
from abc import ABC, abstractmethod
from collections import deque

class Position:
    __slots__ = ['row', 'col']
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
    def __eq__(self, other):
        return self.row == other.row and self.col == other.col
    def __hash__(self):
        return hash((self.row, self.col))
    def __repr__(self):
        return f"Position({self.row},{self.col})"
    def neighbors(self) -> List['Position']:
        return [Position(self.row, self.col-1), Position(self.row, self.col+1)]

class BlockColor(str):
    pass

class Cell:
    __slots__ = ['color', 'empty']
    def __init__(self, c: str):
        if c == '.':
            self.empty = True
            self.color = None
        else:
            self.empty = False
            self.color = BlockColor(c)
    def is_empty(self) -> bool:
        return self.empty
    def __repr__(self):
        return '.' if self.empty else self.color

class Field:
    def __init__(self, h: int, w: int, n: int, grid: List[str]):
        self.h = h
        self.w = w
        self.n = n
        self.cells: List[List[Cell]] = [[Cell(ch) for ch in row] for row in grid]
    def in_bounds(self, pos: Position) -> bool:
        return 0 <= pos.row < self.h and 0 <= pos.col < self.w
    def cell(self, pos: Position) -> Cell:
        return self.cells[pos.row][pos.col]
    def swap(self, pos1: Position, pos2: Position) -> None:
        self.cells[pos1.row][pos1.col], self.cells[pos2.row][pos2.col] = self.cells[pos2.row][pos2.col], self.cells[pos1.row][pos1.col]
    def all_positions(self) -> List[Position]:
        return [Position(r, c) for r in range(self.h) for c in range(self.w)]
    def copy(self) -> 'Field':
        copied_grid = [''.join(self.cells[r][c].__repr__() for c in range(self.w)) for r in range(self.h)]
        return Field(self.h, self.w, self.n, copied_grid)
    def __repr__(self):
        return '\n'.join(''.join(str(self.cells[r][c]) for c in range(self.w)) for r in range(self.h))

class BlockMatcher(ABC):
    @abstractmethod
    def find_sequences_to_remove(self, field: Field) -> Set[Position]:
        pass

class LinearBlockMatcher(BlockMatcher):
    def __init__(self, min_length: int):
        self.min_length = min_length
    def find_sequences_to_remove(self, field: Field) -> Set[Position]:
        to_remove: Set[Position] = set()

        # Horizontal check
        for r in range(field.h):
            c = 0
            while c < field.w:
                cell = field.cells[r][c]
                if cell.is_empty():
                    c += 1
                    continue
                color = cell.color
                length = 1
                for cc in range(c+1, field.w):
                    if not field.cells[r][cc].is_empty() and field.cells[r][cc].color == color:
                        length += 1
                    else:
                        break
                if length >= self.min_length:
                    for cc in range(c, c+length):
                        to_remove.add(Position(r, cc))
                c += length

        # Vertical check
        for c in range(field.w):
            r = 0
            while r < field.h:
                cell = field.cells[r][c]
                if cell.is_empty():
                    r += 1
                    continue
                color = cell.color
                length = 1
                for rr in range(r+1, field.h):
                    if not field.cells[rr][c].is_empty() and field.cells[rr][c].color == color:
                        length += 1
                    else:
                        break
                if length >= self.min_length:
                    for rr in range(r, r+length):
                        to_remove.add(Position(rr, c))
                r += length
        return to_remove

class BlockRemover:
    def remove_blocks(self, field: Field, positions: Set[Position]) -> None:
        for pos in positions:
            field.cells[pos.row][pos.col] = Cell('.')

class GravitySimulator:
    def apply_gravity(self, field: Field) -> bool:
        changed = False
        for c in range(field.w):
            stack = []
            for r in range(field.h-1, -1, -1):
                if not field.cells[r][c].is_empty():
                    stack.append(field.cells[r][c])
            for r in range(field.h-1, -1, -1):
                if stack:
                    top = stack.pop(0)
                    if field.cells[r][c].is_empty() or field.cells[r][c].color != top.color:
                        changed = True
                    field.cells[r][c] = top
                else:
                    if not field.cells[r][c].is_empty():
                        changed = True
                    field.cells[r][c] = Cell('.')
        return changed

class ChainReactionSimulator:
    def __init__(self, matcher: BlockMatcher, remover: BlockRemover, gravity: GravitySimulator):
        self.matcher = matcher
        self.remover = remover
        self.gravity = gravity

    def simulate_until_stable(self, field: Field) -> Field:
        while True:
            positions_to_remove = self.matcher.find_sequences_to_remove(field)
            if not positions_to_remove:
                break
            self.remover.remove_blocks(field, positions_to_remove)
            # Now repeatedly apply gravity until no block moves
            while self.gravity.apply_gravity(field):
                pass
        return field

class EnnichiGame:
    def __init__(self, field: Field):
        self.field = field
        self.matcher = LinearBlockMatcher(field.n)
        self.remover = BlockRemover()
        self.gravity = GravitySimulator()
        self.simulator = ChainReactionSimulator(self.matcher, self.remover, self.gravity)

    def can_clear_all_blocks_by_one_swap(self) -> bool:
        # We try all horizontal adjacent pairs to swap
        for r in range(self.field.h):
            for c in range(self.field.w-1):
                pos1 = Position(r, c)
                pos2 = Position(r, c+1)
                # Must be horizontally adjacent, always true here
                # Swap and simulate
                # Skip if both cells empty, no point
                if self.field.cell(pos1).is_empty() and self.field.cell(pos2).is_empty():
                    continue
                field_copy = self.field.copy()
                field_copy.swap(pos1, pos2)
                # Because the problem states no initial sequences of n or more blocks and no falling blocks,
                # after swap we simulate chain reactions
                self.simulator.simulate_until_stable(field_copy)
                if self.all_blocks_cleared(field_copy):
                    return True
        return False

    def all_blocks_cleared(self, field: Field) -> bool:
        for r in range(field.h):
            for c in range(field.w):
                if not field.cells[r][c].is_empty():
                    return False
        return True

def main():
    h, w, n = map(int, input().split())
    grid = [input().rstrip() for _ in range(h)]

    field = Field(h, w, n, grid)
    game = EnnichiGame(field)
    if game.can_clear_all_blocks_by_one_swap():
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()