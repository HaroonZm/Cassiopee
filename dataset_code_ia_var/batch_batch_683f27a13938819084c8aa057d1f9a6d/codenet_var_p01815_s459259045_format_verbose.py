import sys

input = sys.stdin.readline

number_of_nodes, number_of_edges = map(int, input().split())

node_weights = [0] + list(map(int, input().split()))

edge_list = [tuple(map(int, input().split())) for _ in range(number_of_edges)]

root_node = 1

adjacency_list = [[] for _ in range(number_of_nodes + 1)]

degree_of_nodes = [0] * (number_of_nodes + 1)

for node_a, node_b in edge_list:
    adjacency_list[node_a].append(node_b)
    adjacency_list[node_b].append(node_a)
    degree_of_nodes[node_a] += 1
    degree_of_nodes[node_b] += 1

from collections import deque

processing_queue = deque()
visited_nodes = [0] * (number_of_nodes + 1)

for node_index in range(1, number_of_nodes + 1):
    if degree_of_nodes[node_index] == 1 and node_index != root_node:
        visited_nodes[node_index] = 1
        processing_queue.append(node_index)

degree_of_nodes[root_node] += 1 << 50
visited_nodes[root_node] = 1

while processing_queue:
    current_node = processing_queue.pop()
    degree_of_nodes[current_node] -= 1

    for neighbor_node in adjacency_list[current_node]:
        if visited_nodes[neighbor_node] == 1:
            continue
        degree_of_nodes[neighbor_node] -= 1

        if degree_of_nodes[neighbor_node] == 1 and visited_nodes[neighbor_node] == 0:
            processing_queue.append(neighbor_node)
            visited_nodes[neighbor_node] = 1

cycle_nodes = []
cycle_total_weight = 0

for node_index in range(1, number_of_nodes + 1):
    if degree_of_nodes[node_index] != 0:
        cycle_total_weight += node_weights[node_index]
        cycle_nodes.append(node_index)

maximum_weight_from_cycle = [0] * (number_of_nodes + 1)
visited_for_scoring = [0] * (number_of_nodes + 1)

for cycle_node in cycle_nodes:
    maximum_weight_from_cycle[cycle_node] = cycle_total_weight
    visited_for_scoring[cycle_node] = 1

processing_queue = deque(cycle_nodes)

while processing_queue:
    current_node = processing_queue.pop()
    for neighbor_node in adjacency_list[current_node]:
        if visited_for_scoring[neighbor_node] == 1:
            continue
        maximum_weight_from_cycle[neighbor_node] = node_weights[neighbor_node] + maximum_weight_from_cycle[current_node]
        processing_queue.append(neighbor_node)
        visited_for_scoring[neighbor_node] = 1

print(max(maximum_weight_from_cycle))