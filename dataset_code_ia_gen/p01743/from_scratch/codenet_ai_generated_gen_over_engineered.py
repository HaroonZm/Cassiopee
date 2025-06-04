from abc import ABC, abstractmethod
from typing import List, Tuple
from math import inf


class GraphColoringProblem(ABC):
    @abstractmethod
    def minimal_vertices(self) -> int:
        pass


class CompleteGraphColoring(GraphColoringProblem):
    def __init__(self, color_vertex_counts: List[int]):
        self.color_vertex_counts = color_vertex_counts
        self.n = len(color_vertex_counts)

    def _edges_for_subset_size(self, k: int) -> int:
        # Number of edges in a complete graph of k vertices = k*(k-1)//2
        return k * (k - 1) // 2

    def _feasibility_check(self, m: int) -> bool:
        """
        Check if it is possible to assign vertices (minimum m vertices) so that all sets with a_i vertices
        can color their edges with no overlap of edges.
        This means we want to find a set of m vertices with subsets of size a_i with disjoint edges.
        Since each color i colors all edges among a_i vertices, it colors a_i*(a_i-1)//2 edges.
        The sum of these edges must not exceed total edges in K_m = m*(m-1)//2.
        """

        # Total edges needed to be covered by the union of all color sets (no overlapping edges)
        total_colored_edges = 0
        for a_i in self.color_vertex_counts:
            total_colored_edges += self._edges_for_subset_size(a_i)

        total_possible_edges = self._edges_for_subset_size(m)

        # This is a necessary but not always sufficient condition.
        # However, because there are no overlapping edges, the subsets must fit inside K_m, so this works.
        return total_colored_edges <= total_possible_edges

    def minimal_vertices(self) -> int:
        # We seek minimal m such that feasibility_check(m) == True
        # Lower bound is maximum of a_i (the largest subset)
        left = max(self.color_vertex_counts)
        right = 10**15  # large upper bound to allow binary search

        while left < right:
            mid = (left + right) // 2
            if self._feasibility_check(mid):
                right = mid
            else:
                left = mid + 1
        return left


class InputParser:
    @staticmethod
    def parse_input() -> Tuple[int, List[int]]:
        n = int(input())
        a_list = [int(input()) for _ in range(n)]
        return n, a_list


class OutputPrinter:
    @staticmethod
    def print_result(m: int):
        print(m)


def main():
    # Parse input
    n, a_list = InputParser.parse_input()

    # Solve problem
    problem = CompleteGraphColoring(a_list)
    result = problem.minimal_vertices()

    # Print output
    OutputPrinter.print_result(result)


if __name__ == "__main__":
    main()