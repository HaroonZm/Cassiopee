import sys

from collections import deque

read_input_line = sys.stdin.readline

sys.setrecursionlimit(10**6)

number_of_nodes, number_of_edges = map(int, read_input_line().split())

if number_of_edges % 2 == 1:
    print(-1)
    exit()

edge_list = [ [int(vertex) for vertex in read_input_line().split()] for _ in range(number_of_edges) ]

adjacency_list = [[] for _ in range(number_of_nodes + 1)]

for node_a, node_b in edge_list:
    adjacency_list[node_a].append(node_b)
    adjacency_list[node_b].append(node_a)

spanning_tree_edges = [ set() for _ in range(number_of_nodes + 1) ]
visited_nodes = [False] * (number_of_nodes + 1)
visited_nodes[1] = True

bfs_queue = deque([1])

while bfs_queue:
    current_node = bfs_queue.popleft()
    for neighbor_node in adjacency_list[current_node]:
        if visited_nodes[neighbor_node]:
            continue
        visited_nodes[neighbor_node] = True
        spanning_tree_edges[current_node].add(neighbor_node)
        spanning_tree_edges[neighbor_node].add(current_node)
        bfs_queue.append(neighbor_node)

node_out_degrees = [0] * (number_of_nodes + 1)
edge_orientations = []

for node_a, node_b in edge_list:
    if node_b in spanning_tree_edges[node_a]:
        continue
    edge_orientations.append('{} {}'.format(node_a, node_b))
    node_out_degrees[node_a] += 1

def assign_edge_directions(current_node = 1, parent_node = None):
    for adjacent_node in spanning_tree_edges[current_node]:
        if adjacent_node == parent_node:
            continue
        assign_edge_directions(adjacent_node, current_node)
        if node_out_degrees[adjacent_node] % 2 == 0:
            edge_orientations.append('{} {}'.format(current_node, adjacent_node))
            node_out_degrees[current_node] += 1
        else:
            edge_orientations.append('{} {}'.format(adjacent_node, current_node))
            node_out_degrees[adjacent_node] += 1

assign_edge_directions()

print('\n'.join(edge_orientations))