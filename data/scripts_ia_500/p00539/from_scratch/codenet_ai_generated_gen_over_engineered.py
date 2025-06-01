import sys
import heapq
from typing import List, Tuple, Dict, Set

class Graph:
    def __init__(self, n: int):
        self.n = n
        self.adj: List[List[Tuple[int, int]]] = [[] for _ in range(n + 1)]
        self.edges: List[Tuple[int, int, int]] = []

    def add_edge(self, a: int, b: int, d: int):
        self.adj[a].append((b, d))
        self.adj[b].append((a, d))
        self.edges.append((a, b, d))

class DistanceSolver:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.dist: List[int] = [float('inf')] * (self.graph.n + 1)

    def dijkstra_from(self, start: int):
        self.dist[start] = 0
        pq: List[Tuple[int, int]] = [(0, start)]
        while pq:
            curr_d, u = heapq.heappop(pq)
            if self.dist[u] < curr_d:
                continue
            for v, w in self.graph.adj[u]:
                nd = curr_d + w
                if nd < self.dist[v]:
                    self.dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        return self.dist

class EdgeFilter:
    def __init__(self, graph: Graph, distances: List[int], X: int):
        self.graph = graph
        self.distances = distances
        self.X = X
        self.within_set: Set[int] = {i for i, d in enumerate(distances) if d <= X and i != 0}

    def is_within(self, u: int) -> bool:
        return u in self.within_set or (u == 1 and self.distances[1] <= self.X)

    def filter_edges(self) -> List[Tuple[int, int, int]]:
        # Edges connecting two nodes both within distance <= X should be removed (use tunnel)
        # Others remain and are repaired
        repaired_edges = []
        for a, b, d in self.graph.edges:
            a_within = self.is_within(a)
            b_within = self.is_within(b)
            if a_within and b_within:
                continue
            repaired_edges.append((a, b, d))
        return repaired_edges

class CostCalculator:
    def __init__(self, base_cost: int, repaired_edges: List[Tuple[int, int, int]]):
        self.base_cost = base_cost
        self.repaired_edges = repaired_edges

    def total_cost(self) -> int:
        repair_cost = sum(d for _, _, d in self.repaired_edges)
        return self.base_cost + repair_cost

class JOIParkOptimizer:
    def __init__(self, graph: Graph, C: int):
        self.graph = graph
        self.C = C
        self.dist_solver = DistanceSolver(graph)
        self.distances = self.dist_solver.dijkstra_from(1)

    def objective(self, X: int) -> int:
        edge_filter = EdgeFilter(self.graph, self.distances, X)
        repaired_edges = edge_filter.filter_edges()
        cost_calculator = CostCalculator(self.C * X, repaired_edges)
        return cost_calculator.total_cost()

    def find_min_cost(self) -> int:
        # Possible X values are distances from node 1 to each node
        candidate_Xs = sorted(set(d for d in self.distances if d != float('inf')))
        candidate_Xs.append(0)  # consider zero too
        candidate_Xs = list(set(candidate_Xs))
        candidate_Xs.sort()
        
        # Ternary or linear search due to possible non convexity, but here linear over distinct distances is feasible
        min_cost = float('inf')
        for X in candidate_Xs:
            cost = self.objective(X)
            if cost < min_cost:
                min_cost = cost
        return min_cost

def main():
    input = sys.stdin.readline
    N, M, C = map(int, input().split())
    graph = Graph(N)
    for _ in range(M):
        A, B, D = map(int, input().split())
        graph.add_edge(A, B, D)
    optimizer = JOIParkOptimizer(graph, C)
    print(optimizer.find_min_cost())

if __name__ == "__main__":
    sys.setrecursionlimit(10**7)
    main()