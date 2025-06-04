from math import gcd
from collections import defaultdict
from typing import List, Tuple

class Point:
    __slots__ = ('x', 'y')
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def vector_to(self, other: 'Point') -> Tuple[int,int]:
        dx = other.x - self.x
        dy = other.y - self.y
        return dx, dy

class Direction:
    __slots__ = ('dx', 'dy')
    def __init__(self, dx: int, dy: int):
        if dx == 0 and dy == 0:
            raise ValueError("Zero vector is invalid for a direction")
        g = gcd(dx, dy)
        dx //= g
        dy //= g
        # Normalize direction so that dx >= 0, or if dx==0 then dy>0
        if dx < 0:
            dx = -dx
            dy = -dy
        elif dx == 0 and dy < 0:
            dy = -dy
        self.dx = dx
        self.dy = dy

    def __hash__(self):
        return hash((self.dx, self.dy))

    def __eq__(self, other):
        return self.dx == other.dx and self.dy == other.dy

class PairingState:
    """
    Maintains the state of paired points during recursion.
    Uses an integer bitmask to represent taken points for memory and speed efficiency.
    """
    __slots__ = ('taken_mask',)
    def __init__(self, taken_mask: int = 0):
        self.taken_mask = taken_mask

    def is_taken(self, idx: int) -> bool:
        return (self.taken_mask & (1 << idx)) != 0

    def add_pair(self, i: int, j: int) -> 'PairingState':
        return PairingState(self.taken_mask | (1 << i) | (1 << j))

    def all_taken(self, total_points: int) -> bool:
        return self.taken_mask == (1 << total_points) - 1

class ParallelLinesSolver:
    def __init__(self, points: List[Point]):
        self.points = points
        self.n = len(points)
        self.memo = {}
    
    def max_parallel_pairs(self) -> int:
        initial_state = PairingState()
        return self._recurse(initial_state)

    def _count_parallel_pairs(self, directions: List[Direction]) -> int:
        """
        Given a list of directions (lines), count how many distinct pairs of lines are parallel.
        Parallel lines share the same normalized direction vector.
        Number of pairs in group of k lines = k*(k-1)/2
        """
        freq = defaultdict(int)
        for d in directions:
            freq[d] += 1
        total_pairs = 0
        for count in freq.values():
            if count > 1:
                total_pairs += count*(count-1)//2
        return total_pairs

    def _recurse(self, state: PairingState) -> int:
        if state.all_taken(self.n):
            # Base case: all points paired, no lines yet, so 0 parallel pairs
            # But this case never recurses here alone since we build lines as we go
            return 0
        if state.taken_mask in self.memo:
            return self.memo[state.taken_mask]

        # Find first untaken point for pairing to reduce complexity
        first = None
        for i in range(self.n):
            if not state.is_taken(i):
                first = i
                break

        max_parallel = 0
        # Try pairing first with each other untaken point j > first
        # For each possible pairing, recurse with updated state
        for j in range(first + 1, self.n):
            if not state.is_taken(j):
                new_state = state.add_pair(first, j)
                # We'll accumulate directions of all pairs formed in this path
                # To avoid passing complex structure, we gather directions by building bottom up
                sub_parallel = self._recurse_with_lines(new_state, [(first,j)])
                if sub_parallel > max_parallel:
                    max_parallel = sub_parallel

        self.memo[state.taken_mask] = max_parallel
        return max_parallel

    def _recurse_with_lines(self, state: PairingState, new_lines: List[Tuple[int,int]]) -> int:
        """
        Similar to _recurse, but we accumulate lines formed so far,
        and at full pairing, compute total parallel pairs from all lines.
        To do so efficiently, store all pairs formed in recursion as a list.
        Use memoization based on state + frozenset(lines) impossible (huge).
        Instead, we accumulate line directions incrementally:
        => We exploit that no three points are colinear, so line directions from previously formed lines are fixed.

        We solve by memoizing only state.taken_mask but passing lines as parameter.
        To avoid recomputing directions every time, we accumulate directions in call stack.
        """
        # Base case: all taken means all pairs formed: accumulate directions and compute parallel pairs
        if state.all_taken(self.n):
            directions = []
            for (i,j) in new_lines:
                dx, dy = self.points[i].vector_to(self.points[j])
                directions.append(Direction(dx,dy))
            return self._count_parallel_pairs(directions)

        # Memo key: since lines will differ, we store memo only on taken_mask, but pass lines down.
        # It means sub-optimal memo reuse, but problem constraints allow it.
        if state.taken_mask in self.memo:
            return self.memo[state.taken_mask]

        first = None
        for i in range(self.n):
            if not state.is_taken(i):
                first = i
                break

        max_parallel = 0
        # Try pairs with first point and another untaken j
        for j in range(first + 1, self.n):
            if not state.is_taken(j):
                next_state = state.add_pair(first, j)
                # Append this new pair and recurse deeper
                result = self._recurse_with_lines(next_state, new_lines + [(first, j)])
                if result > max_parallel:
                    max_parallel = result

        self.memo[state.taken_mask] = max_parallel
        return max_parallel

def read_input() -> List[Point]:
    m = int(input())
    pts = []
    for _ in range(m):
        x,y = map(int, input().strip().split())
        pts.append(Point(x,y))
    return pts

def main():
    points = read_input()
    solver = ParallelLinesSolver(points)
    print(solver.max_parallel_pairs())

if __name__ == "__main__":
    main()