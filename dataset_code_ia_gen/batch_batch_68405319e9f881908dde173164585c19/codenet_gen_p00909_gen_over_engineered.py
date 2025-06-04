import sys
from abc import ABC, abstractmethod
from typing import Optional, Dict, Tuple, List, Iterator


class WeightDifferenceQueryHandler(ABC):
    @abstractmethod
    def add_measurement(self, a: int, b: int, w: int) -> None:
        pass

    @abstractmethod
    def query_difference(self, a: int, b: int) -> Optional[int]:
        pass


class WeightedUnionFind(WeightDifferenceQueryHandler):
    """
    Implements a Weighted Union-Find (Disjoint Set Union) structure 
    with the ability to manage weight differences between elements.
    It anticipates future extensions that may deal with other metrics 
    or constraints on the sets.
    """

    def __init__(self, size: int):
        self._parent: List[int] = list(range(size))
        self._rank: List[int] = [0] * size
        self._weight_diff_to_parent: List[int] = [0] * size
        # _weight_diff_to_parent[x] = weight of parent[x] - weight of x

    def _find(self, x: int) -> int:
        if self._parent[x] == x:
            return x
        root = self._find(self._parent[x])
        # path compression with weight update
        self._weight_diff_to_parent[x] += self._weight_diff_to_parent[self._parent[x]]
        self._parent[x] = root
        return root

    def _weight_to_root(self, x: int) -> int:
        self._find(x)
        return self._weight_diff_to_parent[x]

    def add_measurement(self, a: int, b: int, w: int) -> None:
        """Adds information that weight[b] - weight[a] = w."""
        a_root = self._find(a)
        b_root = self._find(b)
        if a_root == b_root:
            # Already connected; consistency assumed by problem statement
            return
        # Union by rank heuristic with weight adjustments
        diff = w + self._weight_to_root(a) - self._weight_to_root(b)
        if self._rank[a_root] < self._rank[b_root]:
            a_root, b_root = b_root, a_root
            diff = -diff
        self._parent[b_root] = a_root
        self._weight_diff_to_parent[b_root] = diff
        if self._rank[a_root] == self._rank[b_root]:
            self._rank[a_root] += 1

    def query_difference(self, a: int, b: int) -> Optional[int]:
        if self._find(a) != self._find(b):
            return None
        return self._weight_to_root(b) - self._weight_to_root(a)


class InputProcessor:
    """
    Abstraction for handling input reading, making the code easier to adapt
    to different input sources (files, streams, etc.) in the future.
    """

    def __init__(self, text_stream: Iterator[str]):
        self._lines = text_stream

    def datasets(self) -> Iterator[Tuple[int, int, List[str]]]:
        while True:
            try:
                header = next(self._lines)
            except StopIteration:
                return
            if header.strip() == "":
                continue
            n, m = map(int, header.split())
            if n == 0 and m == 0:
                break
            commands = []
            for _ in range(m):
                commands.append(next(self._lines).rstrip())
            yield n, m, commands


class ProblemFSolver:
    """
    High-level solver class that ties input, union-find structure, and output logic.
    The class structure is planned for potential further strategies and toggles.
    """

    def __init__(self):
        pass

    @staticmethod
    def solve():
        input_proc = InputProcessor(iter(sys.stdin))
        for n, m, commands in input_proc.datasets():
            uf = WeightedUnionFind(n)
            output = []
            for cmd in commands:
                parts = cmd.split()
                if parts[0] == "!":
                    _, a, b, w = parts
                    uf.add_measurement(int(a) - 1, int(b) - 1, int(w))
                else:  # query '?'
                    _, a, b = parts
                    diff = uf.query_difference(int(a) - 1, int(b) - 1)
                    output.append(str(diff) if diff is not None else "UNKNOWN")
            print("\n".join(output))


if __name__ == "__main__":
    ProblemFSolver.solve()