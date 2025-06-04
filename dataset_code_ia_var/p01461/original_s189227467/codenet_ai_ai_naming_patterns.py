import collections
import sys

input_stream = sys.stdin.readline
output_stream = sys.stdout.write

def main_solution():
    node_count = int(input_stream())
    edge_start = [0] * node_count
    edge_end = [0] * node_count

    for edge_index in range(node_count - 1):
        node_u, node_v = map(int, input_stream().split())
        if node_u > node_v:
            node_u, node_v = node_v, node_u
        edge_start[edge_index] = node_u - 1
        edge_end[edge_index] = node_v - 1

    traversal_queue = collections.deque([0])
    traversal_order = []
    node_distance = [0] * node_count

    while traversal_queue:
        current_node = traversal_queue.popleft()
        traversal_order.append(current_node)
        current_distance = node_distance[current_node]
        if edge_start[current_node] != node_count - 1:
            adjacent_node = edge_start[current_node]
            traversal_queue.append(adjacent_node)
            node_distance[adjacent_node] = current_distance + 1
        if edge_end[current_node] != node_count - 1:
            adjacent_node = edge_end[current_node]
            traversal_queue.append(adjacent_node)
            node_distance[adjacent_node] = current_distance + 1

    subtree_size = [0] * node_count
    dp_table = [[0, 0] for _ in range(node_count)]
    traversal_order.reverse()

    for node in traversal_order:
        node_a = edge_start[node]
        node_b = edge_end[node]
        if node_a == node_count - 1:
            dp_table[node][0] = 2
            dp_table[node][1] = node_distance[node] + 2
            subtree_size[node] = 2
        elif node_b == node_count - 1:
            dp_table[node][0] = dp_table[node_a][0] + subtree_size[node_a] + 1
            dp_table[node][1] = dp_table[node_a][1] + 1
            subtree_size[node] = subtree_size[node_a] + 1
        else:
            dp_table[node][0] = dp_table[node_a][0] + dp_table[node_b][0] + subtree_size[node_a] + subtree_size[node_b]
            dp_table[node][1] = min(
                dp_table[node_a][0] + dp_table[node_b][1] + subtree_size[node_a],
                dp_table[node_a][1] + dp_table[node_b][0] + subtree_size[node_b],
                dp_table[node_a][1] + dp_table[node_b][1]
            )
            subtree_size[node] = subtree_size[node_a] + subtree_size[node_b]

    output_stream(f"{dp_table[0][1]}\n")

main_solution()