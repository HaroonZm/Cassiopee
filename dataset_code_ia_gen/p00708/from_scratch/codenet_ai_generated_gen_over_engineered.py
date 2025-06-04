from typing import List, Tuple
from math import sqrt
import sys


class AbstractMetricSpaceElement:
    def distance_to(self, other: "AbstractMetricSpaceElement") -> float:
        raise NotImplementedError


class Point3D(AbstractMetricSpaceElement):
    __slots__ = ("x", "y", "z")

    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, other: "Point3D") -> float:
        return sqrt(
            (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2
        )


class Sphere(AbstractMetricSpaceElement):
    __slots__ = ("center", "radius")

    def __init__(self, center: Point3D, radius: float) -> None:
        self.center = center
        self.radius = radius

    def distance_to(self, other: "Sphere") -> float:
        # Distance from surface to surface: center to center minus radii
        center_distance = self.center.distance_to(other.center)
        surface_distance = center_distance - (self.radius + other.radius)
        return max(surface_distance, 0.0)

    def touches_or_overlaps(self, other: "Sphere") -> bool:
        # True if spheres touch or overlap or one encloses the other
        center_distance = self.center.distance_to(other.center)
        return center_distance <= self.radius + other.radius


class CorridorsGraph:
    class Edge:
        __slots__ = ("u", "v", "weight")

        def __init__(self, u: int, v: int, weight: float) -> None:
            self.u = u
            self.v = v
            self.weight = weight

        def __lt__(self, other: "CorridorsGraph.Edge") -> bool:
            # For sorting edges by ascending weight
            return self.weight < other.weight

    def __init__(self, nodes_count: int):
        self.n = nodes_count
        self.edges: List[CorridorsGraph.Edge] = []

    def add_edge(self, u: int, v: int, weight: float) -> None:
        self.edges.append(CorridorsGraph.Edge(u, v, weight))

    def minimum_spanning_tree_weight(self) -> float:
        # Using Kruskal's algorithm
        self.edges.sort()
        dsu = DisjointSetUnion(self.n)
        total_weight = 0.0
        for edge in self.edges:
            if not dsu.same_set(edge.u, edge.v):
                dsu.union(edge.u, edge.v)
                total_weight += edge.weight
        return total_weight


class DisjointSetUnion:
    __slots__ = ("parent", "rank")

    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> None:
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            if self.rank[rootA] < self.rank[rootB]:
                self.parent[rootA] = rootB
            else:
                self.parent[rootB] = rootA
                if self.rank[rootA] == self.rank[rootB]:
                    self.rank[rootA] += 1

    def same_set(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)


class SpaceStationConnectivityPlanner:
    def __init__(self, cells: List[Sphere]):
        self.cells = cells
        self.n = len(cells)
        self.dsu_initial = DisjointSetUnion(self.n)

    def build_initial_connectivity(self) -> None:
        # Connect cells that touch or overlap naturally
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.cells[i].touches_or_overlaps(self.cells[j]):
                    self.dsu_initial.union(i, j)

    def compute_corridor_edges(self) -> List[CorridorsGraph.Edge]:
        # Create edges between cells for corridors where needed
        edges = []
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if not self.dsu_initial.same_set(i, j):
                    dist = self.cells[i].distance_to(self.cells[j])
                    edges.append(CorridorsGraph.Edge(i, j, dist))
        return edges

    def plan(self) -> float:
        self.build_initial_connectivity()
        graph = CorridorsGraph(self.n)

        # Add zero length edges for touching/overlapping cells
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.cells[i].touches_or_overlaps(self.cells[j]):
                    graph.add_edge(i, j, 0.0)

        # Add corridor edges between unconnected sets
        corridor_edges = self.compute_corridor_edges()
        graph.edges.extend(corridor_edges)

        # MST on graph with zero-length natural edges effectively
        return graph.minimum_spanning_tree_weight()


def parse_input() -> List[List[Sphere]]:
    datasets = []
    input_lines = sys.stdin.read().strip().split("\n")
    index = 0
    while index < len(input_lines):
        n = int(input_lines[index])
        index += 1
        if n == 0:
            break
        cells = []
        for _ in range(n):
            x_str, y_str, z_str, r_str = input_lines[index].split()
            index += 1
            point = Point3D(float(x_str), float(y_str), float(z_str))
            r = float(r_str)
            cells.append(Sphere(point, r))
        datasets.append(cells)
    return datasets


def main() -> None:
    datasets = parse_input()
    planner_class = SpaceStationConnectivityPlanner
    for cells in datasets:
        planner = planner_class(cells)
        result = planner.plan()
        print(f"{result:.3f}")


if __name__ == "__main__":
    main()