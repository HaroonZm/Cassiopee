from typing import List, Tuple, Dict, Optional, Iterator
import heapq
import sys

class Vertex:
    __slots__ = ['id']
    def __init__(self, id: int):
        self.id = id
    def __repr__(self):
        return f"Vertex({self.id})"

class Edge:
    __slots__ = ['source', 'target', 'weight']
    def __init__(self, source: Vertex, target: Vertex, weight: int):
        self.source = source
        self.target = target
        self.weight = weight
    def __repr__(self):
        return f"Edge({self.source.id}->{self.target.id}, w={self.weight})"

class Graph:
    def __init__(self, vertices: List[Vertex]):
        self.vertices = vertices
        # adjacency list keyed by vertex ID to List of edges
        self.adj_list: Dict[int, List[Edge]] = {v.id: [] for v in vertices}

    def add_edge(self, edge: Edge) -> None:
        self.adj_list[edge.source.id].append(edge)

    def neighbors(self, vertex: Vertex) -> Iterator[Edge]:
        return iter(self.adj_list[vertex.id])

class ShortestPathSolver:
    def __init__(self, graph: Graph, source: Vertex):
        self.graph = graph
        self.source = source
        self.distances: List[Optional[int]] = [None] * len(graph.vertices)

    def initialize(self) -> None:
        for i in range(len(self.distances)):
            self.distances[i] = float('inf')
        self.distances[self.source.id] = 0

    def compute(self) -> List[Optional[int]]:
        self.initialize()
        queue: List[Tuple[int, int]] = []
        heapq.heappush(queue, (0, self.source.id))
        
        while queue:
            current_dist, u_id = heapq.heappop(queue)
            if current_dist > self.distances[u_id]:
                continue
            u_vertex = self.graph.vertices[u_id]
            for edge in self.graph.neighbors(u_vertex):
                alt = current_dist + edge.weight
                if alt < self.distances[edge.target.id]:
                    self.distances[edge.target.id] = alt
                    heapq.heappush(queue, (alt, edge.target.id))
        # convert float('inf') to None for absent paths
        return [dist if dist != float('inf') else None for dist in self.distances]

class InputParser:
    def __init__(self, stream=sys.stdin):
        self.stream = stream

    def parse(self) -> Tuple[Graph, Vertex]:
        line = self._read_nonempty()
        V, E, r = map(int, line.split())
        vertices = [Vertex(i) for i in range(V)]
        graph = Graph(vertices)
        for _ in range(E):
            line = self._read_nonempty()
            s_i, t_i, d_i = map(int, line.split())
            edge = Edge(vertices[s_i], vertices[t_i], d_i)
            graph.add_edge(edge)
        source_vertex = vertices[r]
        return graph, source_vertex

    def _read_nonempty(self) -> str:
        line = ''
        while line.strip() == '':
            line = self.stream.readline()
        return line.strip()

class OutputFormatter:
    def __init__(self, distances: List[Optional[int]], output_stream=sys.stdout):
        self.distances = distances
        self.output_stream = output_stream

    def format_and_print(self) -> None:
        for dist in self.distances:
            if dist is None:
                print("INF", file=self.output_stream)
            else:
                print(dist, file=self.output_stream)

class SingleSourceShortestPathApp:
    def __init__(self):
        self.parser = InputParser()
        self.graph: Optional[Graph] = None
        self.source: Optional[Vertex] = None
        self.solver: Optional[ShortestPathSolver] = None

    def run(self):
        self.graph, self.source = self.parser.parse()
        self.solver = ShortestPathSolver(self.graph, self.source)
        distances = self.solver.compute()
        formatter = OutputFormatter(distances)
        formatter.format_and_print()

if __name__ == "__main__":
    app = SingleSourceShortestPathApp()
    app.run()