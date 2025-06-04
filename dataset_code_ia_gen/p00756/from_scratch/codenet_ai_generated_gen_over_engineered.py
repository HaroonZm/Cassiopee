from typing import List, Tuple, Dict, Set
import sys
import math
import itertools

class Disc:
    def __init__(self, index: int, x: int, y: int, r: int, color: int):
        self.index = index
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.covered_by: Set[int] = set()  # indices of discs covering this disc
        self.covers: Set[int] = set()      # indices of discs this disc covers

    def distance_to(self, other: 'Disc') -> float:
        return math.hypot(self.x - other.x, self.y - other.y)

    def is_on_top_of(self, other: 'Disc') -> bool:
        # A disc i is on top of disc j if:
        # i<j (given)
        # and distance between centers < sum of radii (not just tangent)
        if self.index >= other.index:
            return False
        dist = self.distance_to(other)
        # strictly less means disc i covers disc j, not just tangent
        return dist < (self.r + other.r)

    def __repr__(self):
        return f"Disc(idx={self.index}, color={self.color}, x={self.x}, y={self.y}, r={self.r})"

class GameState:
    def __init__(self, discs: List[Disc]):
        self.discs = discs
        self.n = len(discs)
        self.removed: Set[int] = set()
        # Precompute coverage graph
        self._compute_coverage()

    def _compute_coverage(self):
        # For each disc, find which discs it is on top of (covers),
        # and which discs cover it
        for i in range(self.n):
            for j in range(i+1, self.n):
                if self.discs[i].is_on_top_of(self.discs[j]):
                    self.discs[i].covers.add(j)
                    self.discs[j].covered_by.add(i)

    def can_remove(self, i: int) -> bool:
        # A disc can be removed only if no disc (not removed) is on top of it
        if i in self.removed:
            return False
        return all(cov_disc in self.removed for cov_disc in self.discs[i].covered_by)

    def removable_pairs(self) -> List[Tuple[int,int]]:
        # Return list of pairs (i,j) of removable discs of the same color
        # Both must be removable, distinct, and not removed yet
        removable_discs_by_color: Dict[int, List[int]] = {}
        for disc in self.discs:
            if disc.index not in self.removed and self.can_remove(disc.index):
                removable_discs_by_color.setdefault(disc.color, []).append(disc.index)

        pairs = []
        for color, discs_idxs in removable_discs_by_color.items():
            # generate all pairs of indices
            for i1, i2 in itertools.combinations(discs_idxs, 2):
                pairs.append((i1, i2))

        return pairs

    def remove_pair(self, i: int, j: int) -> None:
        # Remove discs i and j from the state
        self.removed.add(i)
        self.removed.add(j)

    def restore_pair(self, i: int, j: int) -> None:
        self.removed.remove(i)
        self.removed.remove(j)

class Solver:
    def __init__(self, discs: List[Disc]):
        self.state = GameState(discs)
        self.max_removed = 0

    def dfs(self, count: int):
        pairs = self.state.removable_pairs()
        if not pairs:
            # No more moves, try to update max
            if count > self.max_removed:
                self.max_removed = count
            return
        # For each choice of removable pair, recurse
        for i, j in pairs:
            self.state.remove_pair(i, j)
            self.dfs(count + 2)
            self.state.restore_pair(i, j)

    def solve(self) -> int:
        self.max_removed = 0
        self.dfs(0)
        return self.max_removed

class InputHandler:
    def __init__(self):
        self.datasets: List[List[Disc]] = []

    def read_input(self) -> None:
        lines = sys.stdin.read().strip().split('\n')
        idx = 0
        while True:
            if idx >= len(lines):
                break
            n = int(lines[idx])
            idx += 1
            if n == 0:
                break
            discs = []
            for i in range(n):
                x, y, r, c = map(int, lines[idx].split())
                idx += 1
                discs.append(Disc(i, x, y, r, c))
            self.datasets.append(discs)

class OutputHandler:
    def print_results(self, results: List[int]) -> None:
        for result in results:
            print(result)

def main():
    input_handler = InputHandler()
    input_handler.read_input()
    results = []
    for discs in input_handler.datasets:
        solver = Solver(discs)
        result = solver.solve()
        results.append(result)
    output_handler = OutputHandler()
    output_handler.print_results(results)

if __name__ == "__main__":
    main()