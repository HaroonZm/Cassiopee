class Graph:
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.edges = []

    def add_edge(self, source, target, weight):
        self.edges.append(Edge(source, target, weight))

    def bellman_ford(self, source):
        distance = [float('inf')] * self.vertex_count
        distance[source] = 0

        # Relax edges |V| - 1 times
        for i in range(self.vertex_count - 1):
            updated = False
            for edge in self.edges:
                if distance[edge.source] != float('inf') and distance[edge.source] + edge.weight < distance[edge.target]:
                    distance[edge.target] = distance[edge.source] + edge.weight
                    updated = True
            if not updated:
                break

        # Check for negative cycles reachable from source
        for edge in self.edges:
            if distance[edge.source] != float('inf') and distance[edge.source] + edge.weight < distance[edge.target]:
                return None  # Negative cycle detected

        return distance


class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight


class ShortestPathSolver:
    def __init__(self, graph, source):
        self.graph = graph
        self.source = source
        self.distances = None
        self.negative_cycle = False

    def solve(self):
        self.distances = self.graph.bellman_ford(self.source)
        if self.distances is None:
            self.negative_cycle = True

    def output_results(self):
        if self.negative_cycle:
            print("NEGATIVE CYCLE")
        else:
            for dist in self.distances:
                if dist == float('inf'):
                    print("INF")
                else:
                    print(dist)


class InputParser:
    @staticmethod
    def parse_input():
        vertex_count, edge_count, source = map(int, input().split())
        graph = Graph(vertex_count)
        for _ in range(edge_count):
            s, t, d = map(int, input().split())
            graph.add_edge(s, t, d)
        return graph, source


def main():
    graph, source = InputParser.parse_input()
    solver = ShortestPathSolver(graph, source)
    solver.solve()
    solver.output_results()


if __name__ == "__main__":
    main()