class Vertex:
    def __init__(self, vertex_id: int):
        self.id = vertex_id
        self.adjacent = []
        self.discover_time = None
        self.finish_time = None
        self.color = 'WHITE'  # WHITE = undiscovered, GRAY = discovered, BLACK = finished

    def add_edge(self, to_vertex: 'Vertex'):
        self.adjacent.append(to_vertex)

    def sort_adjacency(self):
        self.adjacent.sort(key=lambda v: v.id)

class Graph:
    def __init__(self, num_vertices: int):
        self.vertices = {vid: Vertex(vid) for vid in range(1, num_vertices + 1)}
        self.time = 0

    def add_edges_from_input(self, edges_info):
        for u, k, *neighbors in edges_info:
            vertex = self.vertices[u]
            for v in neighbors:
                vertex.add_edge(self.vertices[v])
            vertex.sort_adjacency()

    def dfs(self):
        for vertex in self.vertices.values():
            vertex.color = 'WHITE'
            vertex.discover_time = None
            vertex.finish_time = None
        self.time = 0
        for vertex_id in sorted(self.vertices.keys()):
            vertex = self.vertices[vertex_id]
            if vertex.color == 'WHITE':
                self._dfs_visit(vertex)

    def _dfs_visit(self, u: Vertex):
        self.time += 1
        u.discover_time = self.time
        u.color = 'GRAY'
        for v in u.adjacent:
            if v.color == 'WHITE':
                self._dfs_visit(v)
        u.color = 'BLACK'
        self.time += 1
        u.finish_time = self.time

    def get_times(self):
        return [(vid, self.vertices[vid].discover_time, self.vertices[vid].finish_time) for vid in sorted(self.vertices.keys())]

class DFSController:
    def __init__(self):
        self.graph = None

    def read_graph(self):
        n = int(input())
        edges_info = []
        for _ in range(n):
            parts = list(map(int, input().strip().split()))
            edges_info.append(parts)
        self.graph = Graph(n)
        self.graph.add_edges_from_input(edges_info)

    def run_dfs(self):
        self.graph.dfs()

    def output_results(self):
        for vid, d, f in self.graph.get_times():
            print(vid, d, f)

def main():
    controller = DFSController()
    controller.read_graph()
    controller.run_dfs()
    controller.output_results()

if __name__ == "__main__":
    main()