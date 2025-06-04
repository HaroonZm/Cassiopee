class WallGrid:
    def __init__(self, horizontal_lines, vertical_lines):
        self.height = len(horizontal_lines)  # Number of horizontal lines = rows + 1
        self.width = len(horizontal_lines[0])  # Number of cols + 1
        self.horizontal = horizontal_lines  # list of strings, horizontal walls
        self.vertical = vertical_lines      # list of strings, vertical walls

    def has_horizontal_wall(self, row, col):
        # horizontal line at row between col and col+1: 0 <= row < height, 0 <= col < width-1
        return self.horizontal[row][col] == '1'

    def has_vertical_wall(self, row, col):
        # vertical line at col between row and row+1: 0 <= row < height-1, 0 <= col < width
        return self.vertical[row][col] == '1'

class Point:
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y
    def __hash__(self):
        return hash((self.x, self.y))
    def __repr__(self):
        return f"({self.x},{self.y})"

class Direction:
    directions = ['U', 'R', 'D', 'L']
    # dx, dy in order U, R, D, L
    moves = {'U': (0,-1), 'R': (1,0), 'D': (0,1), 'L': (-1,0)}
    right_turn = {'U':'R', 'R':'D', 'D':'L', 'L':'U'}
    left_turn  = {'U':'L', 'L':'D', 'D':'R', 'R':'U'}

class RightHandPathFinder:
    def __init__(self, grid: WallGrid, start: Point, start_direction: str):
        self.grid = grid
        self.pos = start
        self.dir = start_direction
        self.path = []

    def wall_on_right(self):
        # Determine position to check for wall on the right side of current direction and position
        # For orientation we note:
        # We stand at a vertex, edges are between vertices
        # We'll check the grid structure (walls between (row,col) points)
        x, y = self.pos.x, self.pos.y
        d = self.dir
        # To check wall on the right, we convert (pos, dir) into an edge
        # We must carefully map each facing & position to the appropriate wall in grid.

        # Facing directions: U, R, D, L
        # Right of facing:
        # U -> R
        # R -> D
        # D -> L
        # L -> U
        right = Direction.right_turn[d]

        if right == 'U':
            # horizontal wall above current vertex between (x,y-1) and (x+1,y-1)
            if y == 0:
                return True  # out of bounds considered wall
            return self.grid.has_horizontal_wall(y-1, x)
        elif right == 'R':
            # vertical wall to right of current vertex between (x,y) and (x,y+1)
            if x == self.grid.width - 1:
                return True
            return self.grid.has_vertical_wall(y, x)
        elif right == 'D':
            # horizontal wall below current vertex between (x,y) and (x+1,y)
            if y == self.grid.height - 1:
                return True
            return self.grid.has_horizontal_wall(y, x)
        elif right == 'L':
            # vertical wall to left of current vertex between (x-1,y) and (x-1,y+1)
            if x == 0:
                return True
            return self.grid.has_vertical_wall(y, x-1)

    def wall_ahead(self):
        x, y = self.pos.x, self.pos.y
        d = self.dir

        if d == 'U':
            if y == 0:
                return True
            return self.grid.has_horizontal_wall(y-1, x)
        elif d == 'R':
            if x == self.grid.width -1:
                return True
            return self.grid.has_vertical_wall(y, x)
        elif d == 'D':
            if y == self.grid.height -1:
                return True
            return self.grid.has_horizontal_wall(y, x)
        elif d == 'L':
            if x == 0:
                return True
            return self.grid.has_vertical_wall(y, x-1)

    def step_forward(self):
        dx, dy = Direction.moves[self.dir]
        self.pos = Point(self.pos.x + dx, self.pos.y + dy)
        self.path.append(self.dir)

    def turn_right(self):
        self.dir = Direction.right_turn[self.dir]

    def turn_left(self):
        self.dir = Direction.left_turn[self.dir]

    def find_path(self):
        start_pos = self.pos
        start_dir = self.dir
        first_loop = True

        while first_loop or (self.pos != start_pos or self.dir != start_dir):
            first_loop = False
            # Wall on right?
            if not self.wall_on_right():
                self.turn_right()
                self.step_forward()
            else:
                if not self.wall_ahead():
                    self.step_forward()
                else:
                    self.turn_left()
        return ''.join(self.path)

def parse_input(lines):
    # lines: 9 lines of input, odd lines horizontal walls, even lines vertical walls
    horizontal_lines = [lines[i] for i in range(0,9,2)]  # 0,2,4,6,8
    vertical_lines = [lines[i] for i in range(1,9,2)]    # 1,3,5,7
    return horizontal_lines, vertical_lines

def main():
    lines = [input().rstrip() for _ in range(9)]
    horizontal_lines, vertical_lines = parse_input(lines)
    grid = WallGrid(horizontal_lines, vertical_lines)

    # Point A: left-top corner vertex with x=0,y=0
    start = Point(0,0)
    # Facing direction: we are on A, wall on right means edge to the right from A must be a wall (guaranteed)
    # So we place our right hand on wall on right => we face downwards, because wall is right of start when facing down.
    # But from the problem statement or common reasoning, initial facing is down, because with right hand on wall to right => facing direction must be down (so that wall at right is top horizontal wall)
    # We test directions to match sample output. The output starts with 'R', so starting direction likely 'R'.
    # It's stated "点 A に立って壁に右手をつき、壁に右手をついたまま..." 
    # The problem states the 1st char of line 1 (horizontal lines top) is always '1' for wall at (0,0 right), so wall at right side of A.
    # So if player faces 'U', wall is at right (to right of vertex facing U is edge to right). So initial direction 'U' works, and with right hand on wall, wall is on the right.
    # But with facing U, first move is R (sample output) which means turn right and move right. Alternately, facing right from start is more natural.

    # Test facing 'U', simulate next step:
    # we will trust problem statement: The initial direction is up (U)
    start_direction = 'U'

    rhpf = RightHandPathFinder(grid, start, start_direction)
    path = rhpf.find_path()
    print(path)

if __name__ == '__main__':
    main()