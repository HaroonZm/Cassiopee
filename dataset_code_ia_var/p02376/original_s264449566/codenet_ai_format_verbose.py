import collections

class MaximumFlowDinicAlgorithm:
    """Dinic's Algorithm for computing the maximum flow in a flow network.
       Time Complexity: O(EV^2)
    """

    class FlowEdge:
        def __init__(self, destination_vertex, capacity, reverse_edge_index):
            self.destination_vertex = destination_vertex
            self.capacity = capacity
            self.reverse_edge_index = reverse_edge_index

    def __init__(self, number_of_vertices):
        """
        number_of_vertices: Total number of vertices in the graph.
        adjacency_list: Stores edges for each vertex.
        """
        self.number_of_vertices = number_of_vertices
        self.adjacency_list = [
            [] for _ in range(number_of_vertices)
        ]

    def add_edge(self, from_vertex, to_vertex, edge_capacity):
        forward_edge = self.FlowEdge(
            to_vertex,
            edge_capacity,
            len(self.adjacency_list[to_vertex])
        )
        backward_edge = self.FlowEdge(
            from_vertex,
            0,
            len(self.adjacency_list[from_vertex]) - 1
        )
        self.adjacency_list[from_vertex].append(forward_edge)
        self.adjacency_list[to_vertex].append(backward_edge)

    def dinic_maximum_flow(self, source_vertex, sink_vertex):
        """
        Computes and returns the maximum flow from source_vertex to sink_vertex.
        """
        INF = float('inf')
        total_maximum_flow = 0

        while True:
            self._bfs_construct_level_graph(source_vertex)
            if self.level_of_vertex[sink_vertex] < 0:
                return total_maximum_flow

            self.iteration_counter_for_vertex = [0] * self.number_of_vertices

            while True:
                current_flow = self._dfs_find_augmenting_path(source_vertex, sink_vertex, INF)
                if current_flow > 0:
                    total_maximum_flow += current_flow
                else:
                    break

    def _dfs_find_augmenting_path(self, current_vertex, sink_vertex, available_flow):
        """
        Depth-First Search to find an augmenting path and update residual capacities.
        Returns the amount of flow sent along the found path.
        """
        if current_vertex == sink_vertex:
            return available_flow

        for edge_search_index in range(
            self.iteration_counter_for_vertex[current_vertex],
            len(self.adjacency_list[current_vertex])
        ):
            self.iteration_counter_for_vertex[current_vertex] = edge_search_index
            edge = self.adjacency_list[current_vertex][edge_search_index]

            if (edge.capacity > 0 and
                self.level_of_vertex[current_vertex] < self.level_of_vertex[edge.destination_vertex]):

                flow_to_push = self._dfs_find_augmenting_path(
                    edge.destination_vertex,
                    sink_vertex,
                    min(available_flow, edge.capacity)
                )
                if flow_to_push > 0:
                    edge.capacity -= flow_to_push
                    reverse_edge = self.adjacency_list[edge.destination_vertex][edge.reverse_edge_index]
                    reverse_edge.capacity += flow_to_push
                    return flow_to_push
        return 0

    def _bfs_construct_level_graph(self, start_vertex):
        """
        Breadth-First Search to compute shortest path levels from start_vertex.
        Populates self.level_of_vertex for use in DFS.
        """
        vertex_queue = collections.deque()
        self.level_of_vertex = [-1] * self.number_of_vertices
        vertex_queue.append(start_vertex)
        self.level_of_vertex[start_vertex] = 0

        while vertex_queue:
            current_vertex = vertex_queue.popleft()
            for edge in self.adjacency_list[current_vertex]:
                if (edge.capacity > 0 and 
                    self.level_of_vertex[edge.destination_vertex] < 0):
                    self.level_of_vertex[edge.destination_vertex] = self.level_of_vertex[current_vertex] + 1
                    vertex_queue.append(edge.destination_vertex)

if __name__ == '__main__':

    number_of_vertices, number_of_edges = map(int, input().split())
    max_flow_solver = MaximumFlowDinicAlgorithm(number_of_vertices)
    source_vertex = 0
    sink_vertex = number_of_vertices - 1

    for _ in range(number_of_edges):
        edge_start_vertex, edge_end_vertex, edge_capacity = map(int, input().split())
        max_flow_solver.add_edge(edge_start_vertex, edge_end_vertex, edge_capacity)

    print(max_flow_solver.dinic_maximum_flow(source_vertex, sink_vertex))