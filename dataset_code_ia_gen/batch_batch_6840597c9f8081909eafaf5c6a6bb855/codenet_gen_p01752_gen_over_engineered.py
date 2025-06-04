from collections import deque
from enum import Enum
from typing import List, Tuple, Set, Optional


class CellType(Enum):
    EMPTY = '.'
    WALL = '#'
    GOAL = 'G'
    START_UP = '^'
    START_DOWN = 'v'
    START_LEFT = '<'
    START_RIGHT = '>'


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    @classmethod
    def from_char(cls, ch: str) -> 'Direction':
        if ch == '^':
            return cls.UP
        elif ch == 'v':
            return cls.DOWN
        elif ch == '<':
            return cls.LEFT
        elif ch == '>':
            return cls.RIGHT
        else:
            raise ValueError(f'Invalid direction character: {ch}')

    def turn_right(self) -> 'Direction':
        return Direction((self.value + 1) % 4)

    def turn_left(self) -> 'Direction':
        return Direction((self.value - 1) % 4)

    def to_vec(self) -> Tuple[int, int]:
        if self == Direction.UP:
            return (-1, 0)
        elif self == Direction.RIGHT:
            return (0, 1)
        elif self == Direction.DOWN:
            return (1, 0)
        elif self == Direction.LEFT:
            return (0, -1)

    def right_direction(self) -> 'Direction':
        # Direction to the right of current facing
        return self.turn_right()


class Point:
    def __init__(self, r: int, c: int):
        self.r = r
        self.c = c

    def __add__(self, other: Tuple[int,int]) -> 'Point':
        return Point(self.r + other[0], self.c + other[1])

    def neighbors_4(self) -> List['Point']:
        return [Point(self.r + dr, self.c + dc) for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]]

    def __eq__(self, other) -> bool:
        return isinstance(other, Point) and self.r == other.r and self.c == other.c

    def __hash__(self) -> int:
        return hash((self.r, self.c))

    def inside(self, N: int, M: int) -> bool:
        return 0 <= self.r < N and 0 <= self.c < M

    def __repr__(self):
        return f'({self.r},{self.c})'


class RightHandContact:
    """
    Abstraction representing the cell (or point) with which B-kun's right hand is in contact.
    Per problem:
    - Right hand reachable cells relative to facing direction are four:
      front, front-right diagonal, right, back-right diagonal.
    - Right hand must stay in contact the whole time.
    - When changing right hand contact, must be continuous (common point).
    """

    # Offsets for right hand possible positions relative to facing direction
    # Index order: front, front-right diag, right, back-right diag
    right_offsets_by_dir = {
        Direction.UP: [(-1,0), (-1,1), (0,1), (1,1)],
        Direction.RIGHT: [(0,1), (1,1), (1,0), (1,-1)],
        Direction.DOWN: [(1,0), (1,-1), (0,-1), (-1,-1)],
        Direction.LEFT: [(0,-1), (-1,-1), (-1,0), (-1,1)],
    }

    def __init__(self, facing: Direction, index: int, base_pos: Point):
        """
        :param facing: Direction B-kun is facing
        :param index: index in [0..3] corresponding to one of the 4 right-hand positions
        :param base_pos: current B-kun position in grid
        """
        self.facing = facing
        self.index = index  # 0..3
        self.base_pos = base_pos

    def get_pos(self) -> Point:
        offset = self.right_offsets_by_dir[self.facing][self.index]
        return self.base_pos + offset

    def neighbors(self) -> List[int]:
        """
        Possible indices of right hand contact we can change to, which are continuous,
        i.e. share at least one point (corner or edge) with current right hand contact.
        The problem states we cannot 'lose' contact.
        Since these are 4 cells around, adjacency can be considered cells sharing edge or corner
        with current position.

        From index, we can move to indices that are adjacent in these 4 positions.
        Because these 4 cells form a contiguous 'L' shape around right side,
        adjacency can be indexed by common point intersections:
        For simplicity, we define allowed moves between indices manually.
        """
        # Adjacency info between these 4 positions, by index
        # 0 connected to 1
        # 1 connected to 0,2
        # 2 connected to 1,3
        # 3 connected to 2
        adjacency = {
            0: [1],
            1: [0,2],
            2: [1,3],
            3: [2],
        }
        return adjacency[self.index]

    def change_hand(self, new_index: int) -> Optional['RightHandContact']:
        if new_index in self.neighbors():
            return RightHandContact(self.facing, new_index, self.base_pos)
        else:
            return None

    def update_base(self, new_base_pos: Point) -> 'RightHandContact':
        # When B-kun moves, right hand contact moves accordingly (same offset index and facing)
        return RightHandContact(self.facing, self.index, new_base_pos)

    def update_facing(self, new_facing: Direction) -> 'RightHandContact':
        # On facing change, the index must remain the same but offsets change,
        # so right hand must be recomputed accordingly.
        return RightHandContact(new_facing, self.index, self.base_pos)

    def is_on_wall(self, board: List[List[str]]) -> bool:
        pos = self.get_pos()
        if not pos.inside(len(board), len(board[0])):
            return True  # out of bounds considered wall since problem states surrounded by walls
        return board[pos.r][pos.c] == '#'

    def __repr__(self):
        return f'RightHand(facing={self.facing},index={self.index},pos={self.get_pos()})'

    def __eq__(self, other) -> bool:
        return isinstance(other, RightHandContact) and self.facing == other.facing and self.index == other.index and self.base_pos == other.base_pos

    def __hash__(self) -> int:
        return hash((self.facing, self.index, self.base_pos))


class State:
    """
    The state of B-kun:
    - Position on grid (row,col)
    - Facing direction
    - Right hand contact index (0-3)
    """
    def __init__(self, pos: Point, facing: Direction, right_contact_idx: int):
        self.pos = pos
        self.facing = facing
        self.right_contact_idx = right_contact_idx

    def to_tuple(self) -> Tuple[int,int,int,int]:
        # Used for visited
        return (self.pos.r, self.pos.c, self.facing.value, self.right_contact_idx)

    def __repr__(self):
        return f'State(pos={self.pos},facing={self.facing},right_contact={self.right_contact_idx})'


class GridMap:
    def __init__(self, N: int, M: int, raw_map: List[str]):
        self.N = N
        self.M = M
        self.board = raw_map
        # Parse start and goal
        self.start_pos: Optional[Point] = None
        self.start_dir: Optional[Direction] = None
        self.goal_pos: Optional[Point] = None
        self._parse_map()

    def _parse_map(self):
        for r in range(self.N):
            for c in range(self.M):
                ch = self.board[r][c]
                if ch == 'G':
                    self.goal_pos = Point(r,c)
                elif ch in ['^','v','<','>']:
                    self.start_pos = Point(r,c)
                    self.start_dir = Direction.from_char(ch)

    def is_empty(self, p: Point) -> bool:
        # Empty means '.' or 'G' or start position (which is indicated by '^','v','<','>')
        if not p.inside(self.N, self.M):
            return False
        ch = self.board[p.r][p.c]
        return ch in {'.', 'G', '^', 'v', '<', '>'}

    def is_wall(self, p: Point) -> bool:
        if not p.inside(self.N, self.M):
            return True
        return self.board[p.r][p.c] == '#'

    def is_goal(self, p: Point) -> bool:
        return p == self.goal_pos


class BkunPathfinder:
    def __init__(self, grid: GridMap):
        self.grid = grid

    def initial_right_hand_index(self) -> int:
        """
        From problem statement:
        - Initially, B-kun's right hand is touching the wall to the right of direction faced.
        So the right contact index must be such that the contact cell is wall initially.
        Among 4 right hand candidates for starting direction, identify which index is wall.
        According to problem, must select that index.

        If multiple, choose any (doesn't clarify multiple possible, only one guaranteed).
        """
        facing = self.grid.start_dir
        base_pos = self.grid.start_pos
        for idx in range(4):
            rh = RightHandContact(facing, idx, base_pos)
            if rh.is_on_wall(self.grid.board):
                return idx
        # If none found, problem states boundary is walls, so must be some wall adjacent.
        # If none found, return 0 as fallback (should never happen)
        return 0

    def bfs_min_steps(self) -> int:
        start_pos = self.grid.start_pos
        start_dir = self.grid.start_dir
        start_rh_idx = self.initial_right_hand_index()

        initial_state = State(start_pos, start_dir, start_rh_idx)
        visited = set()
        visited.add(initial_state.to_tuple())

        # We keep track of visited positions for distance computation,
        # but problem wants minimal unique cells visited count.
        # We'll track path length by number of unique visited cells.

        # BFS queue holds tuples (state, set of visited cells, steps)
        # steps count number of unique cells visited including start

        q = deque()
        q.append((initial_state, frozenset({start_pos}), 1))

        while q:
            state, visited_cells, dist = q.popleft()
            pos = state.pos
            facing = state.facing
            rh_idx = state.right_contact_idx
            rh_contact = RightHandContact(facing, rh_idx, pos)

            if self.grid.is_goal(pos):
                return dist

            # 1) Try move forward if no wall
            forward_vec = facing.to_vec()
            front_pos = pos + forward_vec
            if front_pos.inside(self.grid.N, self.grid.M) and not self.grid.is_wall(front_pos):
                # Update right hand contact after move (same index, same facing, base_pos updated)
                new_rh_contact = rh_contact.update_base(front_pos)
                if not new_rh_contact.is_on_wall(self.grid.board):
                    # Right hand must be on wall after moving if was on wall before (so no losing contact)
                    # Actually no, problem states must never lose contact => must remain touching wall.
                    # If new right hand pos not wall → invalid
                    pass
                else:
                    new_state = State(front_pos, facing, rh_idx)
                    t = new_state.to_tuple()
                    if t not in visited:
                        visited.add(t)
                        new_visited_cells = visited_cells | {front_pos}
                        q.append((new_state, new_visited_cells, len(new_visited_cells)))

            # 2) Turn right: facing changes, right hand contact updates, must still be on wall
            new_facing = facing.turn_right()
            new_rh_contact = rh_contact.update_facing(new_facing)
            if new_rh_contact.is_on_wall(self.grid.board):
                new_state = State(pos, new_facing, rh_idx)
                t = new_state.to_tuple()
                if t not in visited:
                    visited.add(t)
                    q.append((new_state, visited_cells, dist))

            # 3) Turn left: facing changes left, update right hand contact, must still be on wall
            new_facing = facing.turn_left()
            new_rh_contact = rh_contact.update_facing(new_facing)
            if new_rh_contact.is_on_wall(self.grid.board):
                new_state = State(pos, new_facing, rh_idx)
                t = new_state.to_tuple()
                if t not in visited:
                    visited.add(t)
                    q.append((new_state, visited_cells, dist))

            # 4) Change right hand contact index (neighbors of rh_idx)
            neighbors = rh_contact.neighbors()
            for new_idx in neighbors:
                new_rh_contact = RightHandContact(facing, new_idx, pos)
                if new_rh_contact.is_on_wall(self.grid.board):
                    new_state = State(pos, facing, new_idx)
                    t = new_state.to_tuple()
                    if t not in visited:
                        visited.add(t)
                        q.append((new_state, visited_cells, dist))

        return -1


def main():
    N, M = map(int, input().split())
    raw_map = [input() for _ in range(N)]
    grid = GridMap(N, M, raw_map)
    pathfinder = BkunPathfinder(grid)
    ans = pathfinder.bfs_min_steps()
    print(ans)


if __name__ == '__main__':
    main()