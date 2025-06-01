import sys
from abc import ABC, abstractmethod
from typing import List, Tuple, Dict, Set


class HistoricalSiteGraph:
    """
    Abstraction representing the historical sites and the streets connecting them.
    """

    def __init__(self, n_sites: int):
        self.n_sites = n_sites
        # adjacency map: node -> List of (neighbor, distance)
        self.adjacency: Dict[int, List[Tuple[int, int]]] = {i: [] for i in range(n_sites)}

    def add_street(self, site_a: int, site_b: int, distance: int):
        # Add undirected edge between site_a and site_b with given distance
        self.adjacency[site_a].append((site_b, distance))
        self.adjacency[site_b].append((site_a, distance))

    def get_edges(self) -> List[Tuple[int, int, int]]:
        edges = []
        visited = set()
        for u in self.adjacency:
            for v, d in self.adjacency[u]:
                if (v, u) not in visited:
                    edges.append((u, v, d))
                    visited.add((u, v))
        return edges


class LanternPlacementStrategy(ABC):
    """
    Abstract base class for lantern placement strategies.
    Future extensions can implement different lantern placing algorithms.
    """

    @abstractmethod
    def compute_min_lanterns(self, graph: HistoricalSiteGraph) -> int:
        """
        Given a graph, compute the minimal number of lanterns required.
        """
        pass


class MinimumLanternNumberByEdges(LanternPlacementStrategy):
    """
    Implements a concrete strategy to compute the minimal number of lanterns
    given the problem constraints:
    - Lanters are placed at each 100m interval on the roads
    - Distance between historical sites is always multiple of 100 and ≥ 200m
    - Number of lanterns required on an edge = (distance / 100) - 1
    - Lanterns are only placed along the roads, not on the sites themselves
    - Need to cover all sites, so need to cover all edges minimally
    - The minimal set of lanterns can be computed by summing needed lanterns
      for all edges (since the route may not be Hamiltonian)
    """

    def compute_min_lanterns(self, graph: HistoricalSiteGraph) -> int:
        # Explanation:
        # Since each street is to be decorated with lanterns every 100m,
        # and the distance is always multiple of 100m and ≥ 200m,
        # number of lanterns per street = (distance / 100) - 1
        # Lanterns placed on streets only, sites themselves don't have lanterns.
        # Because requirement is to ensure path covers all sites,
        # lanterns on all edges connecting sites are needed.
        # Since we do not require a route that traverses edges exactly once,
        # sum over all edges is minimal.
        edges = graph.get_edges()
        total_lanterns = 0
        for u, v, dist in edges:
            lanterns_on_edge = (dist // 100) - 1
            total_lanterns += lanterns_on_edge
        return total_lanterns


class DataSetParser:
    """
    Encapsulates parsing logic for multiple datasets from input.
    """

    def __init__(self, input_lines: List[str]):
        self.lines = input_lines
        self.index = 0

    def _read_line(self) -> str:
        line = self.lines[self.index].strip()
        self.index += 1
        return line

    def __iter__(self):
        return self

    def __next__(self) -> Tuple[HistoricalSiteGraph, LanternPlacementStrategy]:
        if self.index >= len(self.lines):
            raise StopIteration

        # Read number of historical sites n
        n_line = self._read_line()
        if not n_line.isdigit():
            raise ValueError(f"Invalid input for number of historical sites: '{n_line}'")

        n = int(n_line)
        if n == 0:
            raise StopIteration

        # Read number of streets m
        m_line = self._read_line()
        if not m_line.isdigit():
            raise ValueError(f"Invalid input for number of streets: '{m_line}'")
        m = int(m_line)

        graph = HistoricalSiteGraph(n)

        # Parse m edges
        for _ in range(m):
            edge_line = self._read_line()
            # Format: a,b,d
            parts = edge_line.split(',')
            if len(parts) != 3:
                raise ValueError(f"Invalid edge input line: '{edge_line}'")
            a, b, d = parts
            a = int(a)
            b = int(b)
            d = int(d)
            graph.add_street(a, b, d)

        strategy = MinimumLanternNumberByEdges()
        return (graph, strategy)


def main():
    input_lines = [line for line in sys.stdin if line.strip() != '']
    parser = DataSetParser(input_lines)

    for graph, strategy in parser:
        result = strategy.compute_min_lanterns(graph)
        print(result)


if __name__ == '__main__':
    main()