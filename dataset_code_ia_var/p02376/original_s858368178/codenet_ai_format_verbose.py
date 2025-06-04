from collections import deque

class FlowEdge:
    def __init__(self, destination_node_index, current_flow, capacity, reverse_edge_index, is_reverse_edge):
        self.destination_node_index = destination_node_index
        self.current_flow = current_flow
        self.capacity = capacity
        self.reverse_edge_index = reverse_edge_index
        self.is_reverse_edge = is_reverse_edge

class DinicMaxFlowSolver:
    def __init__(self, total_number_of_nodes: int):
        assert total_number_of_nodes > 0

        self.adjacency_list = [list() for _ in range(total_number_of_nodes)]
        self.shortest_distance_from_source = [None] * total_number_of_nodes
        self.current_edge_index_checked = [None] * total_number_of_nodes

    def add_edge(self, from_node_index: int, to_node_index: int, edge_capacity: int):
        forward_edge = FlowEdge(
            destination_node_index=to_node_index,
            current_flow=0,
            capacity=edge_capacity,
            reverse_edge_index=len(self.adjacency_list[to_node_index]),
            is_reverse_edge=False
        )
        backward_edge = FlowEdge(
            destination_node_index=from_node_index,
            current_flow=edge_capacity,
            capacity=edge_capacity,
            reverse_edge_index=len(self.adjacency_list[from_node_index]),
            is_reverse_edge=True
        )
        self.adjacency_list[from_node_index].append(forward_edge)
        self.adjacency_list[to_node_index].append(backward_edge)

    def compute_maximum_flow(self, source_node_index: int, sink_node_index: int):
        maximum_flow = 0

        while True:
            self._compute_shortest_distances_with_bfs(source_node_index)
            if self.shortest_distance_from_source[sink_node_index] < 0:
                return maximum_flow

            self.current_edge_index_checked = [0] * len(self.current_edge_index_checked)
            while True:
                flow_found_in_dfs = self._find_augmenting_path_with_dfs(
                    current_node_index=source_node_index,
                    sink_node_index=sink_node_index,
                    flow_to_push=10 ** 10
                )
                if flow_found_in_dfs > 0:
                    maximum_flow += flow_found_in_dfs
                else:
                    break

    def _compute_shortest_distances_with_bfs(self, source_node_index: int):
        total_nodes = len(self.shortest_distance_from_source)
        self.shortest_distance_from_source = [-1] * total_nodes
        bfs_queue = deque()
        bfs_queue.append(source_node_index)
        self.shortest_distance_from_source[source_node_index] = 0

        while len(bfs_queue):
            current_node_index = bfs_queue.popleft()

            for edge in self.adjacency_list[current_node_index]:
                residual_capacity = edge.capacity - edge.current_flow
                if residual_capacity > 0 and self.shortest_distance_from_source[edge.destination_node_index] < 0:
                    self.shortest_distance_from_source[edge.destination_node_index] = \
                        self.shortest_distance_from_source[current_node_index] + 1
                    bfs_queue.append(edge.destination_node_index)

    def _find_augmenting_path_with_dfs(self, current_node_index: int, sink_node_index: int, flow_to_push: int):
        if current_node_index == sink_node_index:
            return flow_to_push

        number_of_edges = len(self.adjacency_list[current_node_index])
        edge_search_start = self.current_edge_index_checked[current_node_index]

        while edge_search_start < number_of_edges:
            edge = self.adjacency_list[current_node_index][edge_search_start]
            residual_capacity = edge.capacity - edge.current_flow

            if (residual_capacity > 0 and
                self.shortest_distance_from_source[current_node_index] <
                self.shortest_distance_from_source[edge.destination_node_index]):

                pushed_flow = self._find_augmenting_path_with_dfs(
                    current_node_index=edge.destination_node_index,
                    sink_node_index=sink_node_index,
                    flow_to_push=min(flow_to_push, residual_capacity)
                )

                if pushed_flow > 0:
                    edge.current_flow += pushed_flow
                    self.adjacency_list[edge.destination_node_index][edge.reverse_edge_index].current_flow -= pushed_flow
                    return pushed_flow

            self.current_edge_index_checked[current_node_index] = edge_search_start + 1
            edge_search_start += 1

        return 0

def main():
    total_number_of_vertices, total_number_of_edges = map(int, input().split())
    max_flow_solver = DinicMaxFlowSolver(total_number_of_vertices)

    for _ in range(total_number_of_edges):
        from_node_index, to_node_index, edge_capacity = map(int, input().split())
        max_flow_solver.add_edge(from_node_index, to_node_index, edge_capacity)

    print(max_flow_solver.compute_maximum_flow(0, total_number_of_vertices - 1))

if __name__ == '__main__':
    main()