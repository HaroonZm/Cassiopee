from collections import deque

node_count, query_count = map(int, input().split())

adjacency_list = [[] for _ in range(node_count + 1)]
for edge_index in range(node_count - 1):
    node_a, node_b = map(int, input().split())
    adjacency_list[node_a].append(node_b)
    adjacency_list[node_b].append(node_a)

value_list = [0 for _ in range(node_count + 1)]
for query_index in range(query_count):
    update_node, update_value = map(int, input().split())
    value_list[update_node] += update_value

traversal_stack = deque()
traversal_stack.append(1)
visited_nodes = set()
while traversal_stack:
    current_node = traversal_stack.pop()
    visited_nodes.add(current_node)
    for adjacent_node in adjacency_list[current_node]:
        if adjacent_node not in visited_nodes:
            traversal_stack.append(adjacent_node)
            value_list[adjacent_node] += value_list[current_node]

print(*value_list[1:])