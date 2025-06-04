from collections import deque

class DinicAlgorithm:
    def __init__(self, total_number_of_nodes):
        self.total_nodes = total_number_of_nodes
        self.adjacency_list = [[] for _ in range(total_number_of_nodes)]

    def add_directed_edge(self, start_node, end_node, capacity):
        forward_edge = [end_node, capacity, None]
        forward_edge[2] = backward_edge = [start_node, 0, forward_edge]
        self.adjacency_list[start_node].append(forward_edge)
        self.adjacency_list[end_node].append(backward_edge)

    def add_bidirectional_edge(self, node_u, node_v, capacity_uv, capacity_vu):
        forward_edge = [node_v, capacity_uv, None]
        forward_edge[2] = backward_edge = [node_u, capacity_vu, forward_edge]
        self.adjacency_list[node_u].append(forward_edge)
        self.adjacency_list[node_v].append(backward_edge)

    def build_level_graph(self, source_node, sink_node):
        self.levels = node_levels = [None] * self.total_nodes
        processing_queue = deque([source_node])
        node_levels[source_node] = 0
        while processing_queue:
            current_node = processing_queue.popleft()
            next_level = node_levels[current_node] + 1
            for adjacent_node, capacity, _ in self.adjacency_list[current_node]:
                if capacity and node_levels[adjacent_node] is None:
                    node_levels[adjacent_node] = next_level
                    processing_queue.append(adjacent_node)
        return node_levels[sink_node] is not None

    def find_blocking_flow(self, current_node, sink_node, flow_to_push):
        if current_node == sink_node:
            return flow_to_push
        node_levels = self.levels
        for edge in self.iterators[current_node]:
            adjacent_node, capacity, reverse_edge = edge
            if capacity and node_levels[current_node] < node_levels[adjacent_node]:
                possible_flow = self.find_blocking_flow(adjacent_node, sink_node, min(flow_to_push, capacity))
                if possible_flow:
                    edge[1] -= possible_flow
                    reverse_edge[1] += possible_flow
                    return possible_flow
        return 0

    def compute_maximum_flow(self, source_node, sink_node):
        total_flow = 0
        INFINITE_CAPACITY = 10**9 + 7
        while self.build_level_graph(source_node, sink_node):
            self.iterators = list(map(iter, self.adjacency_list))
            flow_pushed = INFINITE_CAPACITY
            while flow_pushed:
                flow_pushed = self.find_blocking_flow(source_node, sink_node, INFINITE_CAPACITY)
                total_flow += flow_pushed
        return total_flow

import sys
sys.setrecursionlimit(10 ** 7)
read_input = sys.stdin.readline

number_of_elements = int(read_input())
element_values = list(map(int, read_input().split()))

total_positive_score = 0
INFINITE_EDGE_CAPACITY = float('inf')
number_of_nodes_in_flow_network = number_of_elements + 2
flow_network = DinicAlgorithm(number_of_nodes_in_flow_network)

source_node_id = 0
sink_node_id = number_of_nodes_in_flow_network - 1

for element_index in range(number_of_elements):
    element_value = element_values[element_index]
    node_id = element_index + 1
    if element_value > 0:
        flow_network.add_directed_edge(node_id, sink_node_id, element_value)
        total_positive_score += element_value
    elif element_value < 0:
        flow_network.add_directed_edge(source_node_id, node_id, -element_value)

for divisor_node in range(1, number_of_elements // 2 + 1):
    for multiple_node in range(2 * divisor_node, number_of_elements + 1, divisor_node):
        flow_network.add_directed_edge(divisor_node, multiple_node, INFINITE_EDGE_CAPACITY)

maximum_flow_from_source_to_sink = flow_network.compute_maximum_flow(source_node_id, sink_node_id)
max_scorable_sum = total_positive_score - maximum_flow_from_source_to_sink
print(max_scorable_sum)