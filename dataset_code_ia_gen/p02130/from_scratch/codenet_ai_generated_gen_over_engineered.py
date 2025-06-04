import sys
from typing import List, Tuple, Optional, Set, Dict
from abc import ABC, abstractmethod


class InputReader:
    def __init__(self):
        self._input_iter = iter(sys.stdin.read().strip().split())

    def read_int(self) -> int:
        return int(next(self._input_iter))

    def read_ints(self, n: int) -> List[int]:
        return [self.read_int() for _ in range(n)]


class Element:
    def __init__(self, a: int, b: int, idx: int):
        self.a = a
        self.b = b
        self.idx = idx

    @property
    def diff(self) -> int:
        return abs(self.a - self.b)

    def __repr__(self):
        return f"Element(idx={self.idx}, a={self.a}, b={self.b})"


class OperationCondition(ABC):
    @abstractmethod
    def is_satisfied(self, element: Element) -> bool:
        pass

    @abstractmethod
    def is_satisfied_pair(self, elem1: Element, elem2: Element) -> bool:
        pass


class DiffRangeCondition(OperationCondition):
    """Condition encapsulating the diff constraints:
    |a_i - b_i| <= A or B <= |a_i - b_i| <= 2A
    and similarly for pairs."""

    def __init__(self, A: int, B: int):
        self.A = A
        self.B = B

    def is_satisfied(self, element: Element) -> bool:
        d = element.diff
        return d <= self.A or (self.B <= d <= 2 * self.A)

    def is_satisfied_pair(self, elem1: Element, elem2: Element) -> bool:
        combined_diff = abs((elem1.a + elem2.a) - (elem1.b + elem2.b))
        return combined_diff <= self.A or (self.B <= combined_diff <= 2 * self.A)


class MaximumOperationCounter:
    def __init__(self, elements: List[Element], condition: OperationCondition):
        self.elements = elements
        self.condition = condition
        self.N = len(elements)
        self.graph: Dict[int, List[int]] = {}
        self.matches: List[Optional[int]] = [-1] * self.N

    def build_graph(self):
        # We can do a sophisticated bipartite approach by splitting elements into two parts,
        # but here we will consider all elements as nodes.
        # Build graph between nodes whose pair satisfies the pair condition
        self.graph = {i: [] for i in range(self.N)}
        for i in range(self.N):
            for j in range(i + 1, self.N):
                if self.condition.is_satisfied_pair(self.elements[i], self.elements[j]):
                    self.graph[i].append(j)
                    self.graph[j].append(i)

    def _dfs(self, u: int, seen: Set[int]) -> bool:
        for v in self.graph[u]:
            if v not in seen:
                seen.add(v)
                # If v is not matched or we can find an augmenting path
                if self.matches[v] == -1 or self._dfs(self.matches[v], seen):
                    self.matches[v] = u
                    self.matches[u] = v
                    return True
        return False

    def maximum_pair_matching(self) -> int:
        # Reset matches for all
        self.matches = [-1] * self.N
        # Because our graph is undirected and pairing is mutual,
        # we pick unmatched nodes and try to find matches.
        result = 0
        for u in range(self.N):
            if self.matches[u] == -1:
                seen = set()
                seen.add(u)
                if self._dfs(u, seen):
                    result += 1
        return result // 2  # each match counted twice

    def count_max_operations(self) -> int:
        # Step 1: Remove all elements that can be removed solo
        removable_indices = [e.idx for e in self.elements if self.condition.is_satisfied(e)]
        removed = set(removable_indices)

        # Step 2: For remaining not yet removed elements, build graph for pairing
        remaining = [e for e in self.elements if e.idx not in removed]

        if not remaining:
            # No pairs to consider
            return len(removed)

        # Build graph among remaining elements
        self.elements = remaining
        self.N = len(remaining)

        self.build_graph()

        # Step 3: Find maximum matching to remove pairs
        pair_count = self.maximum_pair_matching()

        return len(removed) + pair_count


class ProblemSolver:
    def __init__(self):
        self.A: int = 0
        self.B: int = 0
        self.N: int = 0
        self.elements: List[Element] = []

    def read_input(self) -> None:
        reader = InputReader()
        self.N = reader.read_int()
        self.A = reader.read_int()
        self.B = reader.read_int()
        self.elements = [Element(reader.read_int(), reader.read_int(), idx) for idx in range(self.N)]

    def solve(self) -> int:
        condition = DiffRangeCondition(self.A, self.B)
        counter = MaximumOperationCounter(self.elements, condition)
        return counter.count_max_operations()

    def output(self, answer: int) -> None:
        print(answer)


def main():
    solver = ProblemSolver()
    solver.read_input()
    answer = solver.solve()
    solver.output(answer)


if __name__ == "__main__":
    main()