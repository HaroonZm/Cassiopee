class Direction:
    _directions = ['N', 'E', 'S', 'W']
    _deltas = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}
    _right_turn = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}

    def __init__(self, symbol: str):
        if symbol not in self._directions:
            raise ValueError(f"Invalid direction symbol: {symbol}")
        self.symbol = symbol

    def right(self) -> 'Direction':
        return Direction(self._right_turn[self.symbol])

    def delta(self):
        return self._deltas[self.symbol]

    def __str__(self):
        return self.symbol

    def __eq__(self, other):
        if not isinstance(other, Direction):
            return False
        return self.symbol == other.symbol

    def __hash__(self):
        return hash(self.symbol)

class Position:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def move(self, delta_row: int, delta_col: int) -> 'Position':
        return Position(self.row + delta_row, self.col + delta_col)

    def __eq__(self, other):
        if not isinstance(other, Position):
            return False
        return self.row == other.row and self.col == other.col

    def __hash__(self):
        return hash((self.row, self.col))

    def __str__(self):
        return f"{self.row} {self.col}"

class Maze:
    def __init__(self, grid, initial_pos: Position, initial_dir: Direction):
        self.grid = grid
        self.H = len(grid)
        self.W = len(grid[0])
        self.robot_pos = initial_pos
        self.robot_dir = initial_dir

    def is_in_bounds(self, pos: Position):
        return 1 <= pos.row <= self.H and 1 <= pos.col <= self.W

    def is_empty(self, pos: Position):
        if not self.is_in_bounds(pos):
            return False
        cell = self.grid[pos.row-1][pos.col-1]
        return cell == '.'

    def can_move_forward(self):
        delta_r, delta_c = self.robot_dir.delta()
        next_pos = self.robot_pos.move(delta_r, delta_c)
        return self.is_empty(next_pos)

    def step(self):
        if self.can_move_forward():
            delta_r, delta_c = self.robot_dir.delta()
            self.robot_pos = self.robot_pos.move(delta_r, delta_c)
            return True
        else:
            self.robot_dir = self.robot_dir.right()
            return False

    def simulate(self, L: int) -> Position:
        # Because L can be very large (up to 10^18), naive simulation is impossible.
        # The robot behavior is deterministic; states = (Position, Direction) finite.
        # Use cycle detection: Floyd's Tortoise and Hare algorithm.

        seen = dict()  # maps (pos, dir) -> step at which visited
        steps = 0
        pos_dir = (self.robot_pos, self.robot_dir)
        seen[pos_dir] = 0

        # a function to advance one step (one forward move or one turn+try again until move)
        # But per problem, one step means one forward move; turning happens instantly if blocked.
        # So simulate per forward move.

        while steps < L:
            moved = self.step()
            if moved:
                steps += 1
                pos_dir = (self.robot_pos, self.robot_dir)
                if pos_dir in seen:
                    # cycle detected
                    cycle_start = seen[pos_dir]
                    cycle_length = steps - cycle_start
                    remaining = L - steps
                    skip_cycles = remaining // cycle_length
                    steps += skip_cycles * cycle_length
                    # now we only need to simulate remaining steps after skipping cycles
                    seen.clear()
                seen[pos_dir] = steps
            else:
                # rotate right and try move again on next loop iteration
                # but rotation alone doesn't count as a step; we loop until moved or corner case
                # step not increased here; repeat until succeed move forward or turns 4 times (should always move)
                pass

        return self.robot_pos, self.robot_dir

class InputParser:
    def __init__(self):
        pass

    def parse_dataset(self):
        while True:
            line = ''
            while line.strip() == '':
                line = input()
            H, W, L = map(int, line.strip().split())
            if H == 0 and W == 0 and L == 0:
                break
            grid = []
            initial_pos = None
            initial_dir = None
            for i in range(1, H+1):
                row = list(input())
                for j in range(1, W+1):
                    c = row[j-1]
                    if c in ['N', 'E', 'S', 'W']:
                        initial_pos = Position(i, j)
                        initial_dir = Direction(c)
                        row[j-1] = '.'  # replace robot position with empty cell
                grid.append(row)
            yield H, W, L, grid, initial_pos, initial_dir

class Solution:
    def __init__(self):
        self.parser = InputParser()

    def run(self):
        for H, W, L, grid, initial_pos, initial_dir in self.parser.parse_dataset():
            maze = Maze(grid, initial_pos, initial_dir)
            final_pos, final_dir = maze.simulate(L)
            print(final_pos.row, final_pos.col, final_dir)

if __name__ == '__main__':
    Solution().run()