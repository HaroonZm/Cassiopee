import sys
from collections import deque

def input_readline():
    return sys.stdin.readline()

def output_write(value):
    sys.stdout.write(value)

def graph_connected_components_count():
    node_count, edge_count = map(int, input_readline().split())
    adjacency_list = [[] for node_index in range(node_count)]
    for edge_index in range(edge_count):
        source_node, target_node = map(int, input_readline().split())
        adjacency_list[source_node - 1].append(target_node - 1)
    node_visited = [False] * node_count
    answer_total = 0
    for start_node in range(node_count):
        if node_visited[start_node]:
            continue
        breadth_queue = deque([start_node])
        node_visited[start_node] = True
        while breadth_queue:
            current_node = breadth_queue.popleft()
            answer_total += len(adjacency_list[current_node]) - 1
            for neighbor_node in adjacency_list[current_node]:
                if node_visited[neighbor_node]:
                    continue
                node_visited[neighbor_node] = True
                breadth_queue.append(neighbor_node)
        answer_total += 1
    output_write(f"{answer_total}\n")

graph_connected_components_count()