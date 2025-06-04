from abc import ABC, abstractmethod
from typing import Dict, List, Tuple, Optional
import sys


class WeightedDirectedGraph(ABC):
    @abstractmethod
    def vertices(self) -> List[int]:
        pass

    @abstractmethod
    def edges(self) -> List[Tuple[int, int, int]]:
        pass

    @abstractmethod
    def neighbors(self, vertex: int) -> List[Tuple[int, int]]:
        """Returns list of (neighbor_vertex, edge_weight)"""
        pass

    @abstractmethod
    def edge_weight(self, source: int, target: int) -> Optional[int]:
        pass


class AdjacencyListWeightedDirectedGraph(WeightedDirectedGraph):
    def __init__(self, vertex_count: int):
        self._vertex_count = vertex_count
        self._adjacency: Dict[int, List[Tuple[int, int]]] = {v: [] for v in range(vertex_count)}

    def add_edge(self, source: int, target: int, weight: int) -> None:
        self._adjacency[source].append((target, weight))

    def vertices(self) -> List[int]:
        return list(range(self._vertex_count))

    def edges(self) -> List[Tuple[int, int, int]]:
        all_edges = []
        for v, nbrs in self._adjacency.items():
            for (t, w) in nbrs:
                all_edges.append((v, t, w))
        return all_edges

    def neighbors(self, vertex: int) -> List[Tuple[int, int]]:
        return self._adjacency[vertex]

    def edge_weight(self, source: int, target: int) -> Optional[int]:
        for (nbr, w) in self._adjacency[source]:
            if nbr == target:
                return w
        return None


class TSPSolutionStrategy(ABC):
    @abstractmethod
    def solve(self, graph: WeightedDirectedGraph) -> int:
        pass


class DynamicProgrammingTSPStrategy(TSPSolutionStrategy):
    def solve(self, graph: WeightedDirectedGraph) -> int:
        V = graph.vertices()
        n = len(V)
        ALL_VISITED = (1 << n) - 1

        # dp[mask][i] = minimal cost to visit set mask ending at vertex i
        dp = [[sys.maxsize] * n for _ in range(1 << n)]

        # start from vertex 0 for canonical TSP start/end (arbitrary but consistent)
        dp[1][0] = 0

        for mask in range(1 << n):
            for last in range(n):
                if dp[mask][last] == sys.maxsize:
                    continue
                if (mask & (1 << last)) == 0:
                    continue
                for (nbr, w) in graph.neighbors(last):
                    if mask & (1 << nbr):
                        # already visited
                        continue
                    new_mask = mask | (1 << nbr)
                    new_cost = dp[mask][last] + w
                    if new_cost < dp[new_mask][nbr]:
                        dp[new_mask][nbr] = new_cost

        # close the cycle: return to vertex 0
        res = sys.maxsize
        for i in range(n):
            if dp[ALL_VISITED][i] == sys.maxsize:
                continue
            w = graph.edge_weight(i, 0)
            if w is None:
                continue
            candidate = dp[ALL_VISITED][i] + w
            if candidate < res:
                res = candidate

        return res if res != sys.maxsize else -1


class TSPContext:
    def __init__(self, graph: WeightedDirectedGraph, strategy: TSPSolutionStrategy):
        self._graph = graph
        self._strategy = strategy

    def find_shortest_cycle(self) -> int:
        return self._strategy.solve(self._graph)


class Parser(ABC):
    @abstractmethod
    def parse(self) -> Tuple[WeightedDirectedGraph, int, int]:
        pass


class StdInParser(Parser):
    def parse(self) -> Tuple[WeightedDirectedGraph, int, int]:
        # Reads input from stdin, returns graph, |V|, |E|
        vertex_edge_line = sys.stdin.readline().strip()
        while vertex_edge_line == '':
            vertex_edge_line = sys.stdin.readline().strip()
        V, E = map(int, vertex_edge_line.split())
        graph = AdjacencyListWeightedDirectedGraph(V)
        for _ in range(E):
            s, t, d = map(int, sys.stdin.readline().strip().split())
            graph.add_edge(s, t, d)
        return graph, V, E


def main():
    parser = StdInParser()
    graph, V, E = parser.parse()
    strategy = DynamicProgrammingTSPStrategy()
    context = TSPContext(graph, strategy)
    answer = context.find_shortest_cycle()
    print(answer)


if __name__ == "__main__":
    main()