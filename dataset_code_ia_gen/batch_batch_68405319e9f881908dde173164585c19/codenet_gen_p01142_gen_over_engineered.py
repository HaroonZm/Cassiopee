from typing import List, Tuple, Optional, Iterator
from abc import ABC, abstractmethod


class Direction:
    # Directions ordered clockwise: Up, Right, Down, Left
    UP, RIGHT, DOWN, LEFT = range(4)
    VECTORS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    STR = ['UP', 'RIGHT', 'DOWN', 'LEFT']

    @staticmethod
    def turn_left(d: int) -> int:
        return (d + 3) % 4

    @staticmethod
    def turn_right(d: int) -> int:
        return (d + 1) % 4

    @staticmethod
    def opposite(d: int) -> int:
        return (d + 2) % 4


class CellType:
    WALL = '#'
    FLOOR = '.'
    KITCHEN = 'K'
    MASTER = 'M'


class Position:
    __slots__ = ('row', 'col')

    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def move(self, direction: int) -> 'Position':
        dr, dc = Direction.VECTORS[direction]
        return Position(self.row + dr, self.col + dc)

    def __eq__(self, other) -> bool:
        return self.row == other.row and self.col == other.col

    def __hash__(self) -> int:
        return hash((self.row, self.col))

    def __repr__(self):
        return f"Pos(r={self.row},c={self.col})"


class HouseMap:
    def __init__(self, grid: List[str]):
        self.grid = grid
        self.H = len(grid)
        self.W = len(grid[0]) if self.H > 0 else 0

        self.kitchen = None  # Position of K
        self.master = None  # Position of M
        self.floor_cells = set()
        self.outside_walls = []

        self._extract_special_positions()

    def _extract_special_positions(self):
        for r in range(self.H):
            for c in range(self.W):
                ch = self.grid[r][c]
                if ch == CellType.KITCHEN:
                    self.kitchen = Position(r, c)
                elif ch == CellType.MASTER:
                    self.master = Position(r, c)
                if ch != CellType.WALL:
                    self.floor_cells.add(Position(r, c))

    def is_wall(self, pos: Position) -> bool:
        if not (0 <= pos.row < self.H and 0 <= pos.col < self.W):
            # Out of bounds is wall by problem statement outer borders are wall
            return True
        return self.grid[pos.row][pos.col] == CellType.WALL

    def neighbors(self, pos: Position) -> List[Position]:
        nb = []
        for d in range(4):
            n = pos.move(d)
            if not self.is_wall(n):
                nb.append(n)
        return nb

    def free_direction_from(self, pos: Position) -> Optional[int]:
        # According to problem K and M have exactly one free direction
        free_dirs = [d for d in range(4) if not self.is_wall(pos.move(d))]
        if len(free_dirs) != 1:
            return None
        return free_dirs[0]

    def __repr__(self):
        return '\n'.join(self.grid)


class Instruction(ABC):
    @abstractmethod
    def turn(self, direction: int) -> int:
        pass

    @abstractmethod
    def opposite(self) -> 'Instruction':
        pass


class TurnLeft(Instruction):
    def turn(self, direction: int) -> int:
        return Direction.turn_left(direction)

    def opposite(self) -> 'Instruction':
        return TurnRight()

    def __repr__(self):
        return "TurnLeft"


class TurnRight(Instruction):
    def turn(self, direction: int) -> int:
        return Direction.turn_right(direction)

    def opposite(self) -> 'Instruction':
        return TurnLeft()

    def __repr__(self):
        return "TurnRight"


class Program:
    def __init__(self, instructions: List[Instruction]):
        self.instructions = instructions

    def reverse_with_inversion(self) -> 'Program':
        # Reversed instructions with left/right swapped
        inv = [instr.opposite() for instr in reversed(self.instructions)]
        return Program(inv)

    def __repr__(self):
        return f"Program({self.instructions})"


class RobotState:
    __slots__ = ('position', 'direction', 'program', 'prog_index')

    def __init__(self, position: Position, direction: int, program: Program):
        self.position = position
        self.direction = direction
        self.program = program
        self.prog_index = 0

    def clone(self) -> 'RobotState':
        c = RobotState(self.position, self.direction, self.program)
        c.prog_index = self.prog_index
        return c

    def current_instruction(self) -> Optional[Instruction]:
        if self.prog_index < len(self.program.instructions):
            return self.program.instructions[self.prog_index]
        return None

    def next_instruction(self) -> None:
        self.prog_index += 1

    def at_end(self) -> bool:
        return self.prog_index >= len(self.program.instructions)

    def __hash__(self) -> int:
        return hash((self.position, self.direction, self.prog_index))

    def __eq__(self, other) -> bool:
        return (self.position == other.position and
                self.direction == other.direction and
                self.prog_index == other.prog_index)

    def __repr__(self):
        return f"RobotState(pos={self.position},dir={Direction.STR[self.direction]},idx={self.prog_index})"


class KarakuriSimulator:
    def __init__(self, house_map: HouseMap):
        self.house = house_map

    def _can_move(self, pos: Position, dir_: int) -> bool:
        nxt = pos.move(dir_)
        return not self.house.is_wall(nxt)

    def _simulate_path(self, start_pos: Position, start_dir: int, program: Program,
                       goal: Position) -> bool:
        # Walk simulation states for BFS to check any instruction sequence (including empty)
        # Because instructions must be finite and fixed, the only variable instruction
        # sequence is subset or permutation but the problem states "any finite program".
        # The problem requires deciding if there exists at least one program that succeeds.
        # This implies we must decide reachability with any program.

        # Instead of enumerating all programs (exponential), we model states reachable by
        # starting from initial state and applying all possible instruction sequences.
        # The robot only changes instructions at walls.
        #
        # So nodes of graph = (position, direction, program_index).
        # Actually program index represents instruction to be executed at next wall hit.
        #
        # But since the program is unknown, can any program bring robot from start to goal?
        #
        # The problem states:
        # - Robot moves forward until wall
        # - Then turns left/right according to instruction sequence indexed by prog_index
        # - If program finished, robot stops.
        #
        # So the question: is there any finite instruction sequence such that robot starting
        # walking from start_pos/start_dir reaches goal after program ends (at wall).
        #
        # Key: We consider the machine that at each wall activation can turn left or right.
        # The question is if there's a finite sequence of L/R instructions that leads robot
        # from start to goal.
        #
        # Search or DP approach:
        # We consider states as (position, direction, program_index)
        # But program_index is sequential instructions index, so program length = program_index
        #
        # Since instructions are unknown and finite, we can check if there's any sequence length n
        # such that robot goes to goal. We want minimal n to reach goal.
        #
        # We will perform BFS over (position, direction, program_index)
        # But here instructions are chosen by us, so at each wall hit, robot chooses L or R turn.
        #
        # So from a state (pos, dir, idx), we:
        # 1) Move forward until wall (pos_w, dir)
        # 2) At wall-hit pos_w, choose left or right turn (2 branches)
        # 3) Increment idx by 1
        # 4) Repeat until pos_w == goal and program ended (idx == length)
        #
        # The problem: unknown program length and instructions!
        #
        # To solve:
        # We try BFS on (pos, dir, idx) with idx from 0 to max(n)
        # For idx max, we limit to W*H*4 maximum steps because size is limited.
        #
        # Because segments between wall hit do not depend on instructions,
        # we can try all sequences of L/R up to some max length.
        #
        # We find the minimal program length and ways to reach goal.
        #
        # So let's try BFS with idx limit:
        max_program_length = self.house.H * self.house.W * 4  # heuristic bound

        from collections import deque

        visited = set()
        q = deque()
        init_state = RobotState(start_pos, start_dir, program=None)
        # For simulation we don't need program variable, only index
        # We'll store state tuple (pos, dir, idx)
        # Program variable not used here.
        # We'll track idx in state as BFS depth.
        q.append((start_pos, start_dir, 0))
        visited.add((start_pos, start_dir, 0))

        while q:
            pos, dir_, idx = q.popleft()

            # Move forward until wall or blocked
            cur_pos = pos
            while self._can_move(cur_pos, dir_):
                cur_pos = cur_pos.move(dir_)

            # Check if we stopped on goal and program ended (idx == program length)
            # But program length is any finite length, so if idx == length it stops.
            # We consider program length = idx (because instruction idx executed at this wall)
            # So if robot has executed idx instructions and cannot move forward,
            # the program may end here. This means robot stopped here.
            # So if cur_pos == goal and we stop, we consider success.
            #
            # However the problem states: the robot stops if instructions exhausted.
            # We can choose program length = idx.
            # So if at wall hit, we have no more instructions => stop.

            # If we want to check if there's a program of length idx that stops here on goal:
            # We can return True.
            if cur_pos == goal:
                # We can stop if program ends here, which means no more instructions at idx.
                # So program length = idx
                return True

            if idx == max_program_length:
                # reached maximum possible program length without success
                continue

            # At this wall hit, we can choose next instruction to be left or right turn.
            # Compute next directions
            left_dir = Direction.turn_left(dir_)
            right_dir = Direction.turn_right(dir_)

            # Next states with indexes incremented by 1
            next_idx = idx + 1

            # If blocked on turn means forward step from current position with turned dir blocked,
            # robot stays in same position and executes next instruction.
            # But here we move only after wall hits and turn.
            # Simulation moves only after wall hit and turn.

            # Left turn simulation:
            if self._can_move(cur_pos, left_dir):
                npos = cur_pos
                ndir = left_dir
                if (npos, ndir, next_idx) not in visited:
                    visited.add((npos, ndir, next_idx))
                    q.append((npos, ndir, next_idx))
            else:
                # blocked after turn, stay and advance instruction index
                npos = cur_pos
                ndir = left_dir
                if (npos, ndir, next_idx) not in visited:
                    visited.add((npos, ndir, next_idx))
                    q.append((npos, ndir, next_idx))

            # Right turn simulation:
            if self._can_move(cur_pos, right_dir):
                npos = cur_pos
                ndir = right_dir
                if (npos, ndir, next_idx) not in visited:
                    visited.add((npos, ndir, next_idx))
                    q.append((npos, ndir, next_idx))
            else:
                # blocked after turn, stay and advance instruction index
                npos = cur_pos
                ndir = right_dir
                if (npos, ndir, next_idx) not in visited:
                    visited.add((npos, ndir, next_idx))
                    q.append((npos, ndir, next_idx))

        return False

    def can_reach_goal(self, start_pos: Position, start_dir: int, goal: Position) -> bool:
        # Determine if any program exists that leads from start_pos/start_dir to goal
        return self._simulate_path(start_pos, start_dir, program=None, goal=goal)


class DirectionUtilities:
    @staticmethod
    def get_start_direction(house: HouseMap, start_pos: Position) -> Optional[int]:
        # Returns unique free direction from start position (guaranteed by problem)
        return house.free_direction_from(start_pos)


class KarakuriSolver:
    def __init__(self, house: HouseMap):
        self.house = house
        self.simulator = KarakuriSimulator(house)

    def solve(self) -> str:
        # Determine initial directions from kitchen and master
        kdir = DirectionUtilities.get_start_direction(self.house, self.house.kitchen)
        mdir = DirectionUtilities.get_start_direction(self.house, self.house.master)
        if kdir is None or mdir is None:
            # Malformed input but problem guarantees shape
            return "He cannot bring tea to his master."

        # Outward path: from kitchen, forward along kdir, program in forward execution
        reach_master = self.simulator.can_reach_goal(self.house.kitchen, kdir, self.house.master)
        if not reach_master:
            return "He cannot bring tea to his master."

        # Return path: from master, forward along mdir, reverse execution of program
        # The reverse program exists if and only if there's a program that leads back.
        # So test reachability from master -> kitchen:
        # Problem states directions inverted on return, but position forward again.
        # However, from the problem:
        # Reverse execution means reversed instructions with left/right swapped,
        # but robots move exactly the same simulation except order and turn swap.
        # Since we just want existence of any program, test if any program exists for return:
        # The program reverses instructions with sides swapped.

        # The key is the direction on outward and returning start is the free direction from K or M
        # For return we use mdir on master as start direction to kitchen.

        reach_kitchen = self.simulator.can_reach_goal(self.house.master, mdir, self.house.kitchen)
        if not reach_kitchen:
            return "He cannot return to the kitchen."

        # Both reachable
        return "He can accomplish his mission."


def parse_input() -> Iterator[Tuple[int, int, List[str]]]:
    import sys
    lines_iter = iter(sys.stdin.read().rstrip('\n').split('\n'))
    while True:
        try:
            wh = next(lines_iter).strip()
        except StopIteration:
            return
        if wh == '0 0':
            return
        W, H = map(int, wh.split())
        grid = [next(lines_iter) for _ in range(H)]
        yield W, H, grid


def main():
    for W, H, grid in parse_input():
        house = HouseMap(grid)
        solver = KarakuriSolver(house)
        print(solver.solve())


if __name__ == "__main__":
    main()