from abc import ABC, abstractmethod
from typing import List, Tuple


class CostMatrix:
    def __init__(self, matrix: List[List[int]]):
        self._matrix = matrix
        self._size = len(matrix)

    @property
    def size(self) -> int:
        return self._size

    def get_cost(self, from_area: int, to_area: int) -> int:
        return self._matrix[from_area][to_area]

    def total_cost(self, orientation_matrix: List[List[bool]]) -> int:
        total = 0
        for i in range(self._size):
            for j in range(self._size):
                if i != j:
                    # if orientation_matrix[i][j] = True, road is from i->j
                    if orientation_matrix[i][j]:
                        total += self.get_cost(i, j)
        return total


class OrientationStrategy(ABC):
    @abstractmethod
    def compute_orientation(self, cost_matrix: CostMatrix) -> List[List[bool]]:
        """Returns a boolean matrix where True at [i][j] means road is one-way from i to j."""


class OptimalTourOrientation(OrientationStrategy):
    def __init__(self):
        # We add internal steps for potential future improvements (memoization, alternative algorithms)
        self._memo = {}

    def _build_graph(self, cost_matrix: CostMatrix) -> List[List[Tuple[int, int]]]:
        # Generates adjacency list as (neighbor, cost)
        graph = []
        n = cost_matrix.size
        for i in range(n):
            edges = []
            for j in range(n):
                if i != j:
                    edges.append((j, cost_matrix.get_cost(i, j)))
            graph.append(edges)
        return graph

    def compute_orientation(self, cost_matrix: CostMatrix) -> List[List[bool]]:
        n = cost_matrix.size
        graph = self._build_graph(cost_matrix)

        # We will solve the asymmetric Travelling Salesman Path (ATSP) with dynamic programming
        # state: (visited_bitmask, last_node)
        # value: minimal cost to reach last_node having visited 'visited_bitmask'
        # Because first and last nodes need not match, answer is min over last_node with full mask.

        ALL_VISITED = (1 << n) - 1
        dp = [[float('inf')] * n for _ in range(1 << n)]
        parent = [[-1] * n for _ in range(1 << n)]

        # Initialize starting states: from any node with visited mask being only that node
        for i in range(n):
            dp[1 << i][i] = 0  # cost 0 to start at i

        for visited in range(1 << n):
            for last in range(n):
                if dp[visited][last] == float('inf'):
                    continue
                cost_so_far = dp[visited][last]
                for (neighbor, cost) in graph[last]:
                    if (visited >> neighbor) & 1 == 0:
                        new_visited = visited | (1 << neighbor)
                        new_cost = cost_so_far + cost
                        if new_cost < dp[new_visited][neighbor]:
                            dp[new_visited][neighbor] = new_cost
                            parent[new_visited][neighbor] = last

        # Find minimal cost to visit all nodes ending in any node
        end_node = min(range(n), key=lambda x: dp[ALL_VISITED][x])
        min_cost = dp[ALL_VISITED][end_node]

        # Recover path
        path = []
        mask = ALL_VISITED
        current = end_node
        while current != -1:
            path.append(current)
            prev = parent[mask][current]
            if prev == -1:
                break
            mask ^= (1 << current)
            current = prev
        path.reverse()

        # Now, construct orientation matrix: each edge in path is oriented forward,
        # and the opposite edges oriented backward.
        orientation = [[False] * n for _ in range(n)]

        # Orient edges in path direction
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            orientation[u][v] = True

        # For all other edges between pairs, choose the cheaper orientation opposite of chosen (oriented backward)
        # We orient all other edges not in path as backward or if cycle edges, choose minimal.
        # Because problem demands all roads be oriented, and path edges fixed, remaining edges oriented cheapest way.

        # For every pair (i, j), if not in oriented edges, orient towards direction with minimal cost
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if orientation[i][j] or orientation[j][i]:
                    # Already oriented by path edges or their reverse
                    continue
                if cost_matrix.get_cost(i, j) <= cost_matrix.get_cost(j, i):
                    orientation[i][j] = True
                else:
                    orientation[j][i] = True

        return orientation


class RenovationCostCalculator:
    def __init__(self, strategy: OrientationStrategy):
        self._strategy = strategy

    def calculate_min_cost(self, cost_matrix: CostMatrix) -> int:
        orientation = self._strategy.compute_orientation(cost_matrix)
        return cost_matrix.total_cost(orientation)


class InputReader:
    def __init__(self):
        pass

    def read_data(self) -> Tuple[int, List[List[int]]]:
        n = int(input())
        matrix = []
        for _ in range(n):
            row = list(map(int, input().split()))
            matrix.append(row)
        return n, matrix


class SightseeingTourApp:
    def __init__(self):
        self._reader = InputReader()
        self._strategy = OptimalTourOrientation()
        self._calculator = RenovationCostCalculator(self._strategy)

    def run(self):
        n, matrix = self._reader.read_data()
        cost_matrix = CostMatrix(matrix)
        min_cost = self._calculator.calculate_min_cost(cost_matrix)
        print(min_cost)


if __name__ == "__main__":
    app = SightseeingTourApp()
    app.run()