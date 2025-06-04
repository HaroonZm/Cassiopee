class MaximumFlowDinicAlgorithm:

    class Edge:
        def __init__(self, target_vertex, reverse_edge_index, capacity):
            self.target_vertex = target_vertex
            self.reverse_edge_index = reverse_edge_index
            self.capacity = capacity

    def __init__(self, total_vertices):
        self.total_vertices = total_vertices
        self.adjacency_list = [ [] for _ in range(self.total_vertices) ]

    def add_edge(self, from_vertex, to_vertex, capacity):
        forward_edge = self.Edge(to_vertex, len(self.adjacency_list[to_vertex]), capacity)
        backward_edge = self.Edge(from_vertex, len(self.adjacency_list[from_vertex]) - 1, 0)
        self.adjacency_list[from_vertex].append(forward_edge)
        self.adjacency_list[to_vertex].append(backward_edge)

    def add_undirected_edge(self, from_vertex, to_vertex, capacity):
        forward_edge = self.Edge(to_vertex, len(self.adjacency_list[to_vertex]), capacity)
        backward_edge = self.Edge(from_vertex, len(self.adjacency_list[from_vertex]) - 1, capacity)
        self.adjacency_list[from_vertex].append(forward_edge)
        self.adjacency_list[to_vertex].append(backward_edge)

    def breadth_first_search_level_graph(self, source_vertex):
        self.levels = [ -1 for _ in range(self.total_vertices) ]
        self.levels[source_vertex] = 0
        queue = []
        queue.append(source_vertex)
        while queue:
            current_vertex = queue.pop(0)
            for edge in self.adjacency_list[current_vertex]:
                if edge.capacity > 0 and self.levels[edge.target_vertex] < 0:
                    self.levels[edge.target_vertex] = self.levels[current_vertex] + 1
                    queue.append(edge.target_vertex)

    def depth_first_search_augment(self, current_vertex, sink_vertex, available_flow):
        if current_vertex == sink_vertex:
            return available_flow
        for edge_index in range(self.iterators[current_vertex], len(self.adjacency_list[current_vertex])):
            self.iterators[current_vertex] = edge_index
            edge = self.adjacency_list[current_vertex][edge_index]
            if edge.capacity > 0 and self.levels[current_vertex] < self.levels[edge.target_vertex]:
                pushed_flow = self.depth_first_search_augment(
                    edge.target_vertex,
                    sink_vertex,
                    min(available_flow, edge.capacity)
                )
                if pushed_flow > 0:
                    edge.capacity -= pushed_flow
                    reverse_edge = self.adjacency_list[edge.target_vertex][edge.reverse_edge_index]
                    reverse_edge.capacity += pushed_flow
                    return pushed_flow
        return 0

    def compute_maximum_flow(self, source_vertex, sink_vertex):
        infinite_capacity = float("inf")
        total_flow = 0
        while True:
            self.breadth_first_search_level_graph(source_vertex)
            if self.levels[sink_vertex] < 0:
                return total_flow
            self.iterators = [0 for _ in range(self.total_vertices)]
            augmented_flow = self.depth_first_search_augment(source_vertex, sink_vertex, infinite_capacity)
            while augmented_flow > 0:
                total_flow += augmented_flow
                augmented_flow = self.depth_first_search_augment(source_vertex, sink_vertex, infinite_capacity)

def read_integer_list():
    return list(map(int, input().split()))

total_vertices, total_edges = read_integer_list()
maximum_flow_solver = MaximumFlowDinicAlgorithm(total_vertices)

for _ in range(total_edges):
    source, target, capacity = read_integer_list()
    maximum_flow_solver.add_edge(source, target, capacity)

print(maximum_flow_solver.compute_maximum_flow(0, total_vertices - 1))