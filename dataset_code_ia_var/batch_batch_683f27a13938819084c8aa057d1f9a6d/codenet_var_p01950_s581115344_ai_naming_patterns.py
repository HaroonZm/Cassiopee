import sys
from collections import deque

def input_readline():
    return sys.stdin.readline()

def output_write(data):
    sys.stdout.write(data)

def main_solve():
    node_count, edge_count = map(int, input_readline().split())
    adjacency_list = [[] for _ in range(node_count)]
    for edge_index in range(edge_count):
        node_u, node_v = map(int, input_readline().split())
        adjacency_list[node_u - 1].append(node_v - 1)
        adjacency_list[node_v - 1].append(node_u - 1)
    layer_node_counts = [1, 0]
    distance_layers = [[-1] * node_count for _ in range(2)]
    distance_layers[0][0] = 0
    bfs_queue = deque([(0, 0)])
    while bfs_queue:
        current_node, current_layer = bfs_queue.popleft()
        next_layer = current_layer ^ 1
        next_layer_distance = distance_layers[next_layer]
        new_distance = distance_layers[current_layer][current_node] + 1
        for neighbor_node in adjacency_list[current_node]:
            if next_layer_distance[neighbor_node] != -1:
                continue
            next_layer_distance[neighbor_node] = new_distance
            bfs_queue.append((neighbor_node, next_layer))
            layer_node_counts[next_layer] += 1
            if layer_node_counts[next_layer] == node_count:
                output_write(f"{new_distance}\n")
                break
        else:
            continue
        break
    else:
        output_write("-1\n")

main_solve()