from collections import deque
from typing import List, Tuple, Set, Dict, Iterable

class Color:
    RED = 'R'
    GREEN = 'G'
    BROWN = 'B'
    ALL = {RED, GREEN, BROWN}

    @staticmethod
    def others(color: str) -> Set[str]:
        return Color.ALL - {color}

class Coordinate:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def neighbors(self, max_x: int, max_y: int) -> List['Coordinate']:
        candidates = [(self.x-1, self.y), (self.x+1, self.y), (self.x, self.y-1), (self.x, self.y+1)]
        return [Coordinate(nx, ny) for nx, ny in candidates if 0 <= nx < max_x and 0 <= ny < max_y]

    def __eq__(self, other):
        if not isinstance(other, Coordinate):
            return False
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))

class Grid:
    def __init__(self, width: int, height: int, cells: List[List[str]]):
        self.width = width
        self.height = height
        self.cells = [row[:] for row in cells]

    def clone(self) -> 'Grid':
        return Grid(self.width, self.height, [row[:] for row in self.cells])

    def get_color(self, coord: Coordinate) -> str:
        return self.cells[coord.y][coord.x]

    def set_color(self, coord: Coordinate, color: str):
        self.cells[coord.y][coord.x] = color

    def flood_fill_from_origin(self, new_color: str) -> None:
        origin = Coordinate(0, 0)
        original_color = self.get_color(origin)
        if original_color == new_color:
            return
        to_update = self._connected_cells_of_color(origin, original_color)
        for coord in to_update:
            self.set_color(coord, new_color)

    def _connected_cells_of_color(self, start: Coordinate, color: str) -> Set[Coordinate]:
        # BFS to find connected cells of the same color starting from start
        visited = set()
        queue = deque([start])
        while queue:
            coord = queue.popleft()
            if coord in visited:
                continue
            visited.add(coord)
            for neighbor in coord.neighbors(self.width, self.height):
                if neighbor not in visited and self.get_color(neighbor) == color:
                    queue.append(neighbor)
        return visited

    def is_uniform_color(self) -> bool:
        first_color = self.cells[0][0]
        for row in self.cells:
            for c in row:
                if c != first_color:
                    return False
        return True

    def to_immutable(self) -> Tuple[Tuple[str, ...], ...]:
        return tuple(tuple(row) for row in self.cells)

class FloodFillGameSolver:
    def __init__(self, grid: Grid):
        self.grid = grid

    def solve_min_steps(self) -> int:
        initial_state = self.grid.to_immutable()
        visited: Set[Tuple[Tuple[str, ...], ...]] = set()
        queue = deque([(initial_state, 0)])

        while queue:
            state, steps = queue.popleft()
            if self._is_uniform_state(state):
                return steps
            if state in visited:
                continue
            visited.add(state)
            current_color = state[0][0]
            for next_color in Color.ALL:
                if next_color == current_color:
                    continue
                next_state = self._simulate_flood(state, next_color)
                if next_state not in visited:
                    queue.append((next_state, steps + 1))
        return -1  # If never solved (should not happen)

    def _is_uniform_state(self, state: Tuple[Tuple[str, ...], ...]) -> bool:
        first = state[0][0]
        for row in state:
            for c in row:
                if c != first:
                    return False
        return True

    def _simulate_flood(self, state: Tuple[Tuple[str, ...], ...], new_color: str) -> Tuple[Tuple[str, ...], ...]:
        height = len(state)
        width = len(state[0])
        original_color = state[0][0]
        if original_color == new_color:
            return state
        # BFS to find connected cells from (0,0) with original_color
        visited = set()
        queue = deque([(0,0)])
        state_list = [list(row) for row in state]
        while queue:
            x, y = queue.popleft()
            if (x,y) in visited:
                continue
            visited.add((x,y))
            if state_list[y][x] != original_color:
                continue
            state_list[y][x] = new_color
            for nx, ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if 0 <= nx < width and 0 <= ny < height:
                    if (nx, ny) not in visited and state_list[ny][nx] == original_color:
                        queue.append((nx, ny))
        return tuple(tuple(row) for row in state_list)

def parse_input_lines(lines: Iterable[str]) -> List[Grid]:
    grids = []
    line_iter = iter(lines)
    while True:
        try:
            line = next(line_iter).strip()
            if line == '':
                continue
            x_str, y_str = line.split()
            x, y = int(x_str), int(y_str)
            if x == 0 and y == 0:
                break
            cells = []
            for _ in range(y):
                row = next(line_iter).strip().split()
                cells.append(row)
            grids.append(Grid(x, y, cells))
        except StopIteration:
            break
    return grids

def main():
    import sys
    grids = parse_input_lines(sys.stdin)
    for grid in grids:
        solver = FloodFillGameSolver(grid)
        print(solver.solve_min_steps())

if __name__ == '__main__':
    main()