from collections import deque
from typing import Tuple, Set, Dict, Optional, List


class HexGrid:
    """
    Representation of a hexagonal grid with axial coordinates.
    """

    # Directions mapping according to problem statement (Figure 2)
    # Using (dx, dy) for axial coordinates on the hex grid.
    # The directions are numbered 0 to 5, plus "stay in place".
    DIRECTIONS: List[Tuple[int, int]] = [
        (+1, 0),    # 0
        (+1, -1),   # 1
        (0, -1),    # 2
        (-1, 0),    # 3
        (-1, +1),   # 4
        (0, +1),    # 5
    ]

    def __init__(self, lx: int, ly: int, furniture: Set[Tuple[int, int]]):
        self.lx = lx
        self.ly = ly
        self.furniture = furniture

    def in_bounds(self, x: int, y: int) -> bool:
        return -self.lx <= x <= self.lx and -self.ly <= y <= self.ly

    def passable(self, x: int, y: int) -> bool:
        return (x, y) not in self.furniture

    def neighbors(self, x: int, y: int) -> List[Tuple[int, int, int]]:
        """
        Returns all possible moves including staying in place.
        Each move returns the new coordinate and the direction used for that move.
        Direction 0-5 is moving in that direction, 6 is staying in place.
        """
        result = []
        # moves in directions 0..5
        for d, (dx, dy) in enumerate(self.DIRECTIONS):
            nx, ny = x + dx, y + dy
            if self.in_bounds(nx, ny) and self.passable(nx, ny):
                result.append((nx, ny, d))
        # staying in place
        result.append((x, y, 6))
        return result


class SisterInstruction:
    """
    Sister's instruction generator as per the problem:
    The direction at time t is given by: (x * y * t) % 6
    """

    @staticmethod
    def direction(t: int, x: int, y: int) -> Optional[int]:
        # At time t: direction = (x * y * t) mod 6
        if t == 0:
            # time starts at 1 minute past first instruction
            return None
        return (x * y * t) % 6


class State:
    """
    State for BFS representing current position and time.
    """
    __slots__ = ['x', 'y', 't']

    def __init__(self, x: int, y: int, t: int):
        self.x = x
        self.y = y
        self.t = t

    def __hash__(self):
        return hash((self.x, self.y, self.t))

    def __eq__(self, other):
        return (self.x, self.y, self.t) == (other.x, other.y, other.t)


class IgnoreCounter:
    """
    Tracker for the minimal number of ignores for each state.
    """

    def __init__(self):
        self.data: Dict[State, int] = {}

    def visited(self, state: State) -> bool:
        return state in self.data

    def cost(self, state: State) -> int:
        return self.data.get(state, float('inf'))

    def update(self, state: State, cost: int):
        if state not in self.data or cost < self.data[state]:
            self.data[state] = cost
            return True
        return False


class MovementsSolver:
    """
    Solver that uses modified BFS to find minimal ignoring count.
    """

    def __init__(self, sx: int, sy: int, gx: int, gy: int,
                 furniture: Set[Tuple[int, int]], lx: int, ly: int):
        self.sx = sx
        self.sy = sy
        self.gx = gx
        self.gy = gy
        self.grid = HexGrid(lx, ly, furniture)
        self.lx = lx
        self.ly = ly

    def solve(self) -> int:
        """
        Solves for minimal number of instruction ignores to reach goal.
        Returns -1 if impossible.
        """
        max_time = 3000  # heuristic upper bound -- problem note about "数千程度"
        # use deque for BFS
        from heapq import heappush, heappop

        start_state = State(self.sx, self.sy, 0)
        ignore_counter = IgnoreCounter()
        ignore_counter.update(start_state, 0)
        # Priority queue keyed by (ignores, time)
        pq = []
        heappush(pq, (0, 0, start_state))

        while pq:
            ignores, t, state = heappop(pq)

            if (state.x, state.y) == (self.gx, self.gy):
                return ignores

            if t >= max_time:
                continue

            # sister's instruction at next time state t+1
            instr_dir = SisterInstruction.direction(t + 1, state.x, state.y)
            # For each possible move from current pos:
            for nx, ny, move_dir in self.grid.neighbors(state.x, state.y):
                # Check if obeying sister's instruction:
                # Instruction only for directions 0..5 (moves), no instruction for staying (6)
                obey = (move_dir == instr_dir)
                ignore_count = ignores + (0 if obey else 1)

                new_state = State(nx, ny, t + 1)
                if ignore_counter.update(new_state, ignore_count):
                    heappush(pq, (ignore_count, t + 1, new_state))

        return -1


def main():
    import sys

    input = sys.stdin.readline
    sx, sy, gx, gy = map(int, input().split())
    n = int(input())
    furniture = set()
    for _ in range(n):
        x, y = map(int, input().split())
        furniture.add((x, y))
    lx, ly = map(int, input().split())

    solver = MovementsSolver(sx, sy, gx, gy, furniture, lx, ly)
    ans = solver.solve()
    print(ans)


if __name__ == "__main__":
    main()