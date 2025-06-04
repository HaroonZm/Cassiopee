from typing import List, Tuple, Dict, Optional, Set, Iterator
from collections import deque, defaultdict, namedtuple
import sys

class Direction:
    # Representation of directions with rotation logic
    _order = ['E', 'N', 'W', 'S']  # Clockwise order starting at East for convenience
    _vec = {'E': (0,1), 'W': (0,-1), 'N': (-1,0), 'S': (1,0)}
    _right = {'E':'S', 'S':'W', 'W':'N', 'N':'E'}
    _left = {'E':'N', 'N':'W', 'W':'S', 'S':'E'}
    _back = {'E':'W', 'W':'E', 'N':'S', 'S':'N'}

    @classmethod
    def all(cls) -> List[str]:
        return cls._order

    @classmethod
    def vec(cls, d: str) -> Tuple[int,int]:
        return cls._vec[d]

    @classmethod
    def rotate_check_order(cls, d: str) -> List[str]:
        # order of direction to check: right, front, left, back
        return [cls._right[d], d, cls._left[d], cls._back[d]]

class CellType:
    WALL = '#'
    FLOOR = '.'
    EXIT = 'X'

class MazeCell:
    __slots__ = ['r', 'c', 'cell_type']
    def __init__(self, r: int, c: int, cell_type: str):
        self.r = r
        self.c = c
        self.cell_type = cell_type

    def is_walkable(self) -> bool:
        return self.cell_type in (CellType.FLOOR, CellType.EXIT)

    def is_exit(self) -> bool:
        return self.cell_type == CellType.EXIT

class Person:
    __slots__ = ['id', 'r', 'c', 'dir']
    def __init__(self, pid: int, r: int, c: int, direction: str):
        self.id = pid
        self.r = r
        self.c = c
        self.dir = direction

    def pos(self) -> Tuple[int,int]:
        return (self.r, self.c)

    def front_position(self) -> Tuple[int,int]:
        dr, dc = Direction.vec(self.dir)
        return (self.r + dr, self.c + dc)

    def rotate_to(self, new_dir: str):
        self.dir = new_dir

class Maze:
    def __init__(self, width: int, height: int, grid: List[str]):
        self.width = width
        self.height = height
        self.grid = grid
        self.cells = [[MazeCell(r, c, grid[r][c]) for c in range(width)] for r in range(height)]

    def can_walk(self, r: int, c: int) -> bool:
        if 0 <= r < self.height and 0 <= c < self.width:
            return self.cells[r][c].is_walkable()
        return False

    def is_exit(self, r: int, c: int) -> bool:
        if 0 <= r < self.height and 0 <= c < self.width:
            return self.cells[r][c].is_exit()
        return False

class EvacuationSimulator:
    def __init__(self, maze: Maze, persons: List[Person]):
        self.maze = maze
        self.persons = persons
        # person ids to person mapping
        self.pid_map = {p.id:p for p in persons}

    def step(self) -> None:
        # Rotation phase
        # Each person tries to rotate according to rules
        for p in self.persons:
            rotate_dirs = Direction.rotate_check_order(p.dir)
            found_dir = None
            for ndir in rotate_dirs:
                fr, fc = p.r + Direction.vec(ndir)[0], p.c + Direction.vec(ndir)[1]
                if self.maze.can_walk(fr, fc):
                    found_dir = ndir
                    break
            if found_dir is not None:
                p.rotate_to(found_dir)
            # else no direction change

        # Calculate proposed moves
        proposed_moves: Dict[Tuple[int,int], List[Person]] = defaultdict(list)
        for p in self.persons:
            fr, fc = p.front_position()
            if self.maze.can_walk(fr, fc):
                proposed_moves[(fr, fc)].append(p)

        # Determine moves that are allowed according to priority rule
        # For multiple persons wanting same target cell,
        # prefer the one whose current pos is in the order East, North, West, South relative to target
        # Sort persons by priority: East, North, West, South neighbor positions relative to target cell
        def pos_priority(rel_r: int, rel_c: int) -> int:
            # East = (0,1)
            # North = (-1,0)
            # West = (0,-1)
            # South = (1,0)
            if (rel_r, rel_c) == (0,1):
                return 0
            elif (rel_r, rel_c) == (-1,0):
                return 1
            elif (rel_r, rel_c) == (0,-1):
                return 2
            elif (rel_r, rel_c) == (1,0):
                return 3
            else:
                return 4

        allowed_moves: Set[Person] = set()
        # To avoid two persons moving to the same cell, only one per target
        # Also, no two persons can move if their target cells overlap
        # Persons with front cell same omitted except highest priority

        # First filter out conflicts where multiple persons wanna move to identical cell:
        # Person can move only if no one else has its front cell too.

        # However the problem states "目の前のマス目が空いていて、他の人の目の前のマス目になっていない場合は移動します."
        # So if multiple persons have different front cells, no problem.
        # Only if multiple persons aiming same front cell, then apply priority.

        # The problem states: if multiple persons front same cell, choose one of them according to priority.

        # Step 1: For each front cell, if multiple persons want to move there:
        # select one priority person

        # Step 2: Check if any other person wants to move to that front cell - after step 1 everyone has distinct front cell

        # Step 3: After chosen allowed persons, check if front cells of allowed persons collide or not?
        # The problem doesn't mention collisions of target cells between multiple persons, only front cell conflicts.

        # Actually, it says "目の前のマス目が空いていて、他の人の目の前のマス目になっていない場合は移動します."

        # So persons can only move if their front cell is unique among everyone.

        # So let's process accordingly.

        # 1) For each person, find who shares their front cell - remove all but one according to priority order

        chosen_moves: Dict[Tuple[int,int], Person] = {}
        for pos, ps in proposed_moves.items():
            if len(ps)==1:
                # only one person
                chosen_moves[pos] = ps[0]
            else:
                # multiple persons: select one according order East, North, West, South of pos
                # the position of person relative to pos is (pr - rr, pc - cc), so (rel_r, rel_c) = prev_r - r, prev_c - c
                # careful: persons current pos is (pr, pc), target pos is pos (r,c)
                # relative = (pr - r, pc - c)
                def priority_key(p: Person) -> int:
                    rel_r = p.r - pos[0]
                    rel_c = p.c - pos[1]
                    return pos_priority(rel_r, rel_c)
                ps.sort(key=priority_key)
                chosen_moves[pos] = ps[0]

        # Now check candidates if their chosen front cells are unique globally
        # anyone else wanting same cell is rejected

        # But chosen_moves already guarantees unique target key, so unique.

        # Actually everyone not chosen must remain.
        moving_persons = set(chosen_moves.values())

        # Move the allowed persons
        # If after move person on exit cell, remove the person.

        remaining_persons = []
        for p in self.persons:
            if p in moving_persons:
                fr, fc = p.front_position()
                p.r, p.c = fr, fc
            # after move or stand still:
            if not self.maze.is_exit(p.r, p.c):
                remaining_persons.append(p)

        self.persons = remaining_persons

    def all_evacuated(self) -> bool:
        return len(self.persons) == 0

    def simulate(self, max_time: int=180) -> Optional[int]:
        for t in range(1, max_time+1):
            self.step()
            if self.all_evacuated():
                return t
        return None

def parse_input() -> Iterator[Tuple[int,int,List[str]]]:
    # Read from standard input until "0 0"
    for line in sys.stdin:
        if not line.strip():
            continue
        W_H = line.strip().split()
        if len(W_H) != 2:
            continue
        W, H = map(int, W_H)
        if W == 0 and H == 0:
            break
        maze_lines = []
        while len(maze_lines) < H:
            row = sys.stdin.readline()
            if row == '':
                break
            row = row.rstrip('\n')
            if len(row) == W:
                maze_lines.append(row)
        yield (W, H, maze_lines)

def find_persons(maze_lines: List[str]) -> List[Person]:
    # Parse grid for persons
    pid = 0
    persons = []
    for r, line in enumerate(maze_lines):
        for c, ch in enumerate(line):
            if ch in ('E','W','S','N'):
                persons.append(Person(pid, r, c, ch))
                pid += 1
    return persons

def solve():
    for W, H, maze_lines in parse_input():
        maze = Maze(W, H, maze_lines)
        persons = find_persons(maze_lines)
        simulator = EvacuationSimulator(maze, persons)
        res = simulator.simulate()
        print(res if res is not None else "NA")

if __name__ == '__main__':
    solve()