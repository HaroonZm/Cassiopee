class Coordinate:
    def __init__(self, x: int, y: int):
        self.x = x  # 1-based
        self.y = y  # 1-based

    def neighbors_in_blast_range(self):
        # Returns all coordinates within 3 units up, down, left, right (manhattan distance along axis only)
        coords = []
        # Up to 3 cells up
        for dy in range(1, 4):
            ny = self.y - dy
            if 1 <= ny <= 8:
                coords.append(Coordinate(self.x, ny))
        # Up to 3 cells down
        for dy in range(1, 4):
            ny = self.y + dy
            if 1 <= ny <= 8:
                coords.append(Coordinate(self.x, ny))
        # Left
        for dx in range(1, 4):
            nx = self.x - dx
            if 1 <= nx <= 8:
                coords.append(Coordinate(nx, self.y))
        # Right
        for dx in range(1, 4):
            nx = self.x + dx
            if 1 <= nx <= 8:
                coords.append(Coordinate(nx, self.y))
        return coords

    def __eq__(self, other):
        if not isinstance(other, Coordinate):
            return False
        return (self.x == other.x) and (self.y == other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"Coord({self.x},{self.y})"

class BombGrid:
    WIDTH = 8
    HEIGHT = 8

    def __init__(self, grid_lines):
        # grid_lines: list of 8 strings of length 8, '0' or '1'
        # store boolean for bomb presence: True if bomb exists, False otherwise
        self._bombs = [[cell == '1' for cell in line] for line in grid_lines]

    def has_bomb(self, coord: Coordinate):
        return self._bombs[coord.y - 1][coord.x - 1]

    def remove_bomb(self, coord: Coordinate):
        self._bombs[coord.y - 1][coord.x - 1] = False

    def get_all_bombs_coordinates(self):
        bombs = []
        for y in range(1, 9):
            for x in range(1, 9):
                if self.has_bomb(Coordinate(x, y)):
                    bombs.append(Coordinate(x, y))
        return bombs

    def __str__(self):
        # return 8 lines of "0"/"1"
        return "\n".join("".join('1' if self._bombs[y][x] else '0' for x in range(8)) for y in range(8))


class ExplosionSimulator:
    def __init__(self, bomb_grid: BombGrid):
        self.board = bomb_grid
        self.exploded = set()  # Coordinates of exploded bombs

    def simulate(self, initial_explosion: Coordinate):
        # If no bomb at initial location, explosion does nothing
        if not self.board.has_bomb(initial_explosion):
            return

        # BFS queue of bombs to explode
        from collections import deque
        queue = deque([initial_explosion])
        self.exploded.add(initial_explosion)

        while queue:
            current = queue.popleft()
            # Remove the bomb from the board (explode it)
            self.board.remove_bomb(current)
            # Determine next bombs affected by blast
            affected_coords = current.neighbors_in_blast_range()
            for coord in affected_coords:
                if coord not in self.exploded and self.board.has_bomb(coord):
                    self.exploded.add(coord)
                    queue.append(coord)


class InputParser:
    def __init__(self, raw_lines):
        self.lines = raw_lines
        self.current_index = 0

    def read_int(self):
        while self.current_index < len(self.lines):
            line = self.lines[self.current_index].strip()
            self.current_index += 1
            if line != '':
                return int(line)
        raise EOFError()

    def read_grid(self):
        grid = []
        count = 0
        while count < 8:
            line = self.lines[self.current_index].rstrip('\n')
            self.current_index += 1
            if line == '':
                # Empty line in between should be avoided here
                continue
            grid.append(line)
            count += 1
        return grid

    def read_coordinates(self):
        # read two lines with X and Y
        while self.current_index < len(self.lines) and self.lines[self.current_index].strip() == '':
            self.current_index += 1
        x = int(self.lines[self.current_index].strip())
        self.current_index +=1
        while self.current_index < len(self.lines) and self.lines[self.current_index].strip() == '':
            self.current_index += 1
        y = int(self.lines[self.current_index].strip())
        self.current_index += 1
        return Coordinate(x, y)


class DataSet:
    def __init__(self, grid_lines, initial_bomb: Coordinate):
        self.grid = BombGrid(grid_lines)
        self.initial = initial_bomb

    def run_simulation(self):
        exploder = ExplosionSimulator(self.grid)
        exploder.simulate(self.initial)
        return self.grid.__str__()


class ProblemSolver:
    def __init__(self, raw_input_lines):
        self.parser = InputParser(raw_input_lines)
        self.datasets = []

    def parse_all(self):
        n = self.parser.read_int()
        for _ in range(n):
            # Read potential blank line before each dataset
            while self.parser.current_index < len(self.parser.lines) and self.parser.lines[self.parser.current_index].strip() == '':
                self.parser.current_index +=1
            grid = self.parser.read_grid()
            initial = self.parser.read_coordinates()
            self.datasets.append(DataSet(grid, initial))

    def solve_all(self):
        results = []
        for i, dataset in enumerate(self.datasets, 1):
            res = dataset.run_simulation()
            results.append((i, res))
        return results

def main():
    import sys
    lines = sys.stdin.readlines()
    solver = ProblemSolver(lines)
    solver.parse_all()
    results = solver.solve_all()
    for i, res in results:
        print(f"Data {i}:")
        print(res)

if __name__ == '__main__':
    main()