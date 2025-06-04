from collections import deque

class DinicMaxFlow:
    class FlowEdge:
        def __init__(self, destination_vertex, capacity, reverse_edge_index):
            self.destination_vertex = destination_vertex
            self.capacity = capacity
            self.reverse_edge_index = reverse_edge_index

    def __init__(self, total_vertices, infinite_capacity=10**9+7):
        self.total_vertices = total_vertices
        self.infinite_capacity = infinite_capacity
        self.vertex_levels = [-1] * total_vertices
        self.current_edge_iterators = [0] * total_vertices
        self.adjacency_list = [[] for _ in range(total_vertices)]

    def add_edge(self, start_vertex, end_vertex, edge_capacity):
        forward_edge = self.FlowEdge(end_vertex, edge_capacity, len(self.adjacency_list[end_vertex]))
        backward_edge = self.FlowEdge(start_vertex, 0, len(self.adjacency_list[start_vertex]) - 1)
        self.adjacency_list[start_vertex].append(forward_edge)
        self.adjacency_list[end_vertex].append(backward_edge)

    def build_level_graph_by_bfs(self, source_vertex):
        self.vertex_levels = [-1] * self.total_vertices
        queue = deque()
        self.vertex_levels[source_vertex] = 0
        queue.append(source_vertex)

        while queue:
            current_vertex = queue.popleft()
            for edge in self.adjacency_list[current_vertex]:
                if edge.capacity > 0 and self.vertex_levels[edge.destination_vertex] < 0:
                    self.vertex_levels[edge.destination_vertex] = self.vertex_levels[current_vertex] + 1
                    queue.append(edge.destination_vertex)

    def find_augmenting_path_by_dfs(self, current_vertex, sink_vertex, flow_amount):
        if current_vertex == sink_vertex:
            return flow_amount

        while self.current_edge_iterators[current_vertex] < len(self.adjacency_list[current_vertex]):
            edge_index = self.current_edge_iterators[current_vertex]
            edge = self.adjacency_list[current_vertex][edge_index]

            if edge.capacity > 0 and self.vertex_levels[current_vertex] < self.vertex_levels[edge.destination_vertex]:
                possible_flow = self.find_augmenting_path_by_dfs(
                    edge.destination_vertex, sink_vertex, min(flow_amount, edge.capacity)
                )
                if possible_flow > 0:
                    edge.capacity -= possible_flow
                    self.adjacency_list[edge.destination_vertex][edge.reverse_edge_index].capacity += possible_flow
                    return possible_flow

            self.current_edge_iterators[current_vertex] += 1

        return 0

    def compute_maximum_flow(self, source_vertex, sink_vertex):
        total_flow = 0

        while True:
            self.build_level_graph_by_bfs(source_vertex)
            if self.vertex_levels[sink_vertex] < 0:
                return total_flow

            self.current_edge_iterators = [0] * self.total_vertices

            while True:
                sent_flow = self.find_augmenting_path_by_dfs(
                    source_vertex, sink_vertex, self.infinite_capacity
                )
                if sent_flow == 0:
                    break
                total_flow += sent_flow


def main():
    number_of_vertices, number_of_edges = map(int, input().split())

    maximum_flow_solver = DinicMaxFlow(number_of_vertices)

    for edge_index in range(number_of_edges):
        source_vertex, destination_vertex, edge_capacity = map(int, input().split())
        maximum_flow_solver.add_edge(source_vertex, destination_vertex, edge_capacity)

    print(maximum_flow_solver.compute_maximum_flow(0, number_of_vertices - 1))


if __name__ == '__main__':
    main()