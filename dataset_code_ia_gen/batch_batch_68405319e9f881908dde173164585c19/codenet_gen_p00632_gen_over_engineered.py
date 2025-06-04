class Position:
    __slots__ = ('row', 'col')

    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def __eq__(self, other):
        return isinstance(other, Position) and self.row == other.row and self.col == other.col

    def __hash__(self):
        return hash((self.row, self.col))

    def copy(self):
        return Position(self.row, self.col)

    def neighbors(self, deltas):
        for dr, dc in deltas:
            yield Position(self.row + dr, self.col + dc)

class MovementPattern:
    _DIR_MAP = {
        '5': (0, 0),
        '8': (-1, 0),
        '6': (0, 1),
        '4': (0, -1),
        '2': (1, 0),
    }

    def __init__(self, pattern_str: str):
        self.pattern = [self._DIR_MAP[ch] for ch in pattern_str]
        self.length = len(self.pattern)

    def move_at(self, step: int, pos: Position, grid) -> Position:
        dr, dc = self.pattern[step % self.length]
        new_r, new_c = pos.row + dr, pos.col + dc
        if not grid.in_bounds(new_r, new_c):
            # Stays if out of bounds
            return pos
        if grid.is_wall_for_ghost(new_r, new_c) or grid.is_block_for_ghost(new_r, new_c) == False:
            # Ghost can enter '#' but not other blocks. We'll clarify grid checks later.
            # The problem statement states: '#' can be entered only by ghost, '.' by both.
            # So here we just allow ghost movement into '#' or '.'.
            tile = grid.tile(new_r, new_c)
            if tile not in ['.', '#']:
                return pos
            return Position(new_r, new_c)
        # else no restriction to move
        return Position(new_r, new_c)

class Grid:
    def __init__(self, h: int, w: int, tiles: list[str]):
        self.H = h
        self.W = w
        self.grid = tiles

    def in_bounds(self, r: int, c: int) -> bool:
        return 0 <= r < self.H and 0 <= c < self.W

    def tile(self, r: int, c: int) -> str:
        return self.grid[r][c]

    def can_walk(self, r: int, c: int) -> bool:
        # For girl only: '.' means walkable, '#' no
        if not self.in_bounds(r, c):
            return False
        return self.tile(r, c) == '.'

    def can_ghost_enter(self, r: int, c: int) -> bool:
        # Ghost can enter '.' or '#'
        if not self.in_bounds(r, c):
            return False
        return self.tile(r, c) in ('.', '#')

    def is_block_for_girl(self, r: int, c: int) -> bool:
        # True if girl can walk there ('.')
        return self.can_walk(r, c)

    def is_block_for_ghost(self, r: int, c: int) -> bool:
        # True if ghost can enter there ('.' or '#')
        return self.can_ghost_enter(r, c)

class Entity:
    def __init__(self, pos: Position):
        self.pos = pos

    def can_move(self, to: Position, grid: Grid) -> bool:
        raise NotImplementedError

    def legal_moves(self, grid: Grid):
        raise NotImplementedError

class Girl(Entity):
    _deltas = [(0,0), (-1,0), (1,0), (0,-1), (0,1)]  # stay, N, S, W, E

    def can_move(self, to: Position, grid: Grid) -> bool:
        # Girl can move onto '.' but not '#'
        return grid.in_bounds(to.row, to.col) and grid.tile(to.row, to.col) == '.'

    def legal_moves(self, grid: Grid):
        # returns iterable of possible positions
        for dr, dc in self._deltas:
            nr, nc = self.pos.row + dr, self.pos.col + dc
            if self.can_move(Position(nr, nc), grid):
                yield Position(nr, nc)
            else:
                if not grid.in_bounds(nr, nc):
                    # move rejected, stays instead
                    if dr == 0 and dc == 0:
                        yield Position(nr, nc)  # stay on self.pos
                # else no yield -- forbidden move

class Ghost(Entity):
    def __init__(self, pos: Position, movement_pattern: MovementPattern):
        super().__init__(pos)
        self.pattern = movement_pattern

    def move_by_pattern(self, step: int, grid: Grid) -> Position:
        dr, dc = self.pattern.pattern[step % self.pattern.length]
        nr, nc = self.pos.row + dr, self.pos.col + dc
        if not grid.in_bounds(nr, nc):
            return self.pos  # stay
        tile = grid.tile(nr, nc)
        if tile not in ['.', '#']:
            return self.pos
        # ghost allowed on '.' or '#'
        return Position(nr, nc)

class State:
    __slots__ = ('girl_pos', 'ghost_pos', 'ghost_step')

    def __init__(self, girl_pos: Position, ghost_pos: Position, ghost_step: int):
        self.girl_pos = girl_pos
        self.ghost_pos = ghost_pos
        self.ghost_step = ghost_step

    def __hash__(self):
        return hash((self.girl_pos.row, self.girl_pos.col, self.ghost_pos.row, self.ghost_pos.col, self.ghost_step))

    def __eq__(self, other):
        return (self.girl_pos == other.girl_pos and self.ghost_pos == other.ghost_pos and self.ghost_step == other.ghost_step)

class Game:
    def __init__(self, h, w, tiles, pattern_str):
        self.grid = Grid(h, w, tiles)
        self.pattern = MovementPattern(pattern_str)
        self.girl = None
        self.ghost = None
        self._prepare_entities()
        self.time_limit = 10000  # safety cap to prevent infinite loops

    def _prepare_entities(self):
        girl_pos = ghost_pos = None
        for r in range(self.grid.H):
            for c in range(self.grid.W):
                ch = self.grid.tile(r, c)
                if ch == 'A':
                    girl_pos = Position(r, c)
                elif ch == 'B':
                    ghost_pos = Position(r, c)
        self.girl = Girl(girl_pos)
        self.ghost = Ghost(ghost_pos, self.pattern)

    def earliest_encounter(self):
        from collections import deque
        # State: (girl_pos, ghost_pos, ghost_step)
        initial = State(self.girl.pos, self.ghost.pos, 0)
        queue = deque()
        queue.append((0, initial))
        visited = set()
        visited.add((initial.girl_pos.row, initial.girl_pos.col, initial.ghost_pos.row, initial.ghost_pos.col, initial.ghost_step))

        girl_moves = [(0,0), (-1,0), (1,0), (0,-1), (0,1)]  # stay,N,S,W,E

        while queue:
            time, state = queue.popleft()
            if time > self.time_limit:
                break
            # Check encounter at current time
            if state.girl_pos == state.ghost_pos:
                return (time, state.girl_pos.row, state.girl_pos.col)
            next_ghost_step = (state.ghost_step + 1) % self.pattern.length
            # ghost moves according to pattern
            next_ghost_pos = self.pattern_move(state.ghost_pos, state.ghost_step)
            # Girl tries all moves
            for dr, dc in girl_moves:
                new_girl_r, new_girl_c = state.girl_pos.row + dr, state.girl_pos.col + dc
                new_girl_pos = Position(new_girl_r, new_girl_c)
                if not self.grid.in_bounds(new_girl_r, new_girl_c):
                    new_girl_pos = state.girl_pos  # stays
                elif self.grid.tile(new_girl_r, new_girl_c) != '.':
                    new_girl_pos = state.girl_pos  # stays
                # If girl attempts to move out and fails, counts as staying, so we just use state.girl_pos
                # Actually this logic covers that already
                new_state_tuple = (new_girl_pos.row, new_girl_pos.col, next_ghost_pos.row, next_ghost_pos.col, next_ghost_step)
                if new_state_tuple not in visited:
                    visited.add(new_state_tuple)
                    if new_girl_pos == next_ghost_pos:
                        # Encounter at next time
                        return (time + 1, new_girl_pos.row, new_girl_pos.col)
                    new_state = State(new_girl_pos, next_ghost_pos, next_ghost_step)
                    queue.append((time + 1, new_state))
        return None

    def pattern_move(self, ghost_pos: Position, step: int) -> Position:
        dr, dc = self.pattern.pattern[step % self.pattern.length]
        nr, nc = ghost_pos.row + dr, ghost_pos.col + dc
        if not self.grid.in_bounds(nr, nc):
            return ghost_pos
        tile = self.grid.tile(nr, nc)
        if tile not in ['.', '#']:
            return ghost_pos
        return Position(nr, nc)

def main():
    import sys
    input = sys.stdin.readline
    while True:
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
            if not line:
                return
        H, W = map(int, line.strip().split())
        if H == 0 and W == 0:
            break
        grid_lines = []
        read_lines = 0
        while read_lines < H:
            line = sys.stdin.readline()
            if not line:
                return
            if line.strip() == '':
                continue
            grid_lines.append(line.rstrip('\n'))
            read_lines += 1
        pattern_line = ''
        while pattern_line.strip() == '':
            pattern_line = sys.stdin.readline()
            if not pattern_line:
                return
        pattern = pattern_line.strip()
        game = Game(H, W, grid_lines, pattern)
        ans = game.earliest_encounter()
        if ans is None:
            print("impossible")
        else:
            print(*ans)

if __name__ == "__main__":
    main()