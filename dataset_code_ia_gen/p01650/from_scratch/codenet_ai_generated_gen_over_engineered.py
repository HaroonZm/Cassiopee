from collections import deque
from typing import List, Tuple, Optional, Dict, Set, FrozenSet


class CellType:
    ROCK = '#'
    FREE = '.'

    @staticmethod
    def is_free(cell: str) -> bool:
        return cell != CellType.ROCK


class Jewel:
    def __init__(self, lower_char: str):
        self.type = lower_char

    def hole_char(self) -> str:
        return self.type.upper()


class Hole:
    def __init__(self, upper_char: str):
        self.type = upper_char

    def jewel_char(self) -> str:
        return self.type.lower()


class Position:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def __hash__(self):
        return hash((self.row, self.col))

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __add__(self, other: Tuple[int, int]) -> 'Position':
        return Position(self.row + other[0], self.col + other[1])


class Maze:
    def __init__(self, grid: List[List[str]]):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0]) if self.height > 0 else 0

    def in_bounds(self, pos: Position) -> bool:
        return 0 <= pos.row < self.height and 0 <= pos.col < self.width

    def at(self, pos: Position) -> str:
        return self.grid[pos.row][pos.col]

    def is_free(self, pos: Position) -> bool:
        return CellType.is_free(self.at(pos))

    def neighbors(self, pos: Position) -> List[Position]:
        # Only right and down moves allowed
        candidates = [Position(pos.row, pos.col + 1), Position(pos.row + 1, pos.col)]
        return [c for c in candidates if self.in_bounds(c) and self.is_free(c)]


class JewelStack:
    def __init__(self, stack: Tuple[str, ...] = ()):
        self.stack = stack

    def push(self, c: str) -> 'JewelStack':
        return JewelStack(self.stack + (c,))

    def pop(self) -> Tuple[Optional['JewelStack'], Optional[str]]:
        if not self.stack:
            return None, None
        return JewelStack(self.stack[:-1]), self.stack[-1]

    def top(self) -> Optional[str]:
        if not self.stack:
            return None
        return self.stack[-1]

    def __hash__(self):
        return hash(self.stack)

    def __eq__(self, other):
        return self.stack == other.stack


class State:
    def __init__(self, pos: Position, bag: JewelStack, placed_count: int):
        self.pos = pos
        self.bag = bag
        self.placed_count = placed_count

    def __hash__(self):
        # Position + bag stack contents
        return hash((self.pos, self.bag))

    def __eq__(self, other):
        return self.pos == other.pos and self.bag == other.bag

    def __lt__(self, other):
        # For priority queues if needed
        return self.placed_count > other.placed_count


class MazeSolver:
    def __init__(self, maze: Maze):
        self.maze = maze
        self.start = Position(0, 0)
        self.goal = Position(maze.height - 1, maze.width - 1)

    def maximize_placed_jewels(self) -> int:
        from heapq import heappush, heappop

        # Priority queue for max placed jewels (simulate max heap with negative placed_count)
        heap = []
        initial_state = State(self.start, JewelStack(), 0)
        heappush(heap, (-initial_state.placed_count, initial_state))

        # visited: Dict[(row, col, bag_stack_tuple)] = max_placed_found
        visited: Dict[Tuple[int, int, Tuple[str, ...]], int] = {}

        max_placed = -1

        while heap:
            neg_placed_count, state = heappop(heap)
            placed = -neg_placed_count

            key = (state.pos.row, state.pos.col, state.bag.stack)
            if key in visited and visited[key] >= placed:
                continue
            visited[key] = placed

            if state.pos == self.goal:
                max_placed = max(max_placed, placed)
                continue

            cell = self.maze.at(state.pos)

            # Generate next states:

            next_positions = self.maze.neighbors(state.pos)

            for nxt in next_positions:
                nxt_cell = self.maze.at(nxt)

                # If cell is free '.', no action needed
                if nxt_cell == CellType.FREE:
                    new_state = State(nxt, state.bag, placed)
                    heappush(heap, (-new_state.placed_count, new_state))
                    continue

                # If jewel cell lowercase letter
                if nxt_cell.islower():
                    # Two choices: pick or skip
                    # Skip jewel
                    skip_state = State(nxt, state.bag, placed)
                    heappush(heap, (-skip_state.placed_count, skip_state))

                    # Pick jewel
                    new_bag = state.bag.push(nxt_cell)
                    pick_state = State(nxt, new_bag, placed)
                    heappush(heap, (-pick_state.placed_count, pick_state))
                    continue

                # If hole cell uppercase letter
                if nxt_cell.isupper():
                    # Two choices: place or skip
                    # Skip placement:
                    skip_state = State(nxt, state.bag, placed)
                    heappush(heap, (-skip_state.placed_count, skip_state))

                    # Place jewel if possible
                    if state.bag.top() == nxt_cell.lower():
                        after_pop, popped_jewel = state.bag.pop()
                        place_state = State(nxt, after_pop, placed + 1)
                        heappush(heap, (-place_state.placed_count, place_state))
                    continue

                # Rock cell is filtered out by neighbors check, no else needed

        return max_placed


class InputParser:
    @staticmethod
    def read_problem_sets() -> List[Maze]:
        mazes = []
        while True:
            try:
                line = input()
                if not line:
                    continue
                H_W = line.split()
                if len(H_W) != 2:
                    continue
                H, W = map(int, H_W)
                if H == 0 and W == 0:
                    break
                grid = []
                for _ in range(H):
                    row = input()
                    while len(row) != W:
                        row = input()
                    grid.append(list(row))
                mazes.append(Maze(grid))
            except EOFError:
                break
        return mazes


def main():
    mazes = InputParser.read_problem_sets()
    results = []
    for maze in mazes:
        solver = MazeSolver(maze)
        res = solver.maximize_placed_jewels()
        results.append(str(res))
    print('\n'.join(results))


if __name__ == '__main__':
    main()