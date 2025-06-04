import bisect
import os
import sys

# Constants for system configuration and modular arithmetic
CONST_INPUT_RECURSION_LIMIT = 10 ** 9
CONST_INF_FLOAT = float("inf")
CONST_INF_INT = 10 ** 18
CONST_MODULO = 10 ** 9 + 7
# CONST_ALT_MODULO = 998244353

# Input configuration for local/remote environments
if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(CONST_INPUT_RECURSION_LIMIT)

# Input parsing with systematic variable naming
var_num_nodes, var_num_ranges = map(int, sys.stdin.buffer.readline().split())
list_pair_node_states = [list(map(int, sys.stdin.buffer.readline().split())) for _ in range(var_num_nodes)]
list_pair_range_edges = [list(map(int, sys.stdin.buffer.readline().split())) for _ in range(var_num_ranges)]

# Preprocessing input data
list_pair_node_states.sort()
var_node_index_odd = 0  # unused
list_tuple_nodes_extended = [(0, 0)] + list_pair_node_states + [(CONST_INF_FLOAT, 0)]
list_val_a = [val_a for val_a, val_b in list_tuple_nodes_extended]
list_val_b = [val_b for val_a, val_b in list_tuple_nodes_extended]

var_nodes_total = len(list_tuple_nodes_extended)
list_adjacent_graph = [[] for _ in range(var_nodes_total)]
for idx_edge, (var_left, var_right) in enumerate(list_pair_range_edges, start=1):
    idx_left = bisect.bisect_left(list_val_a, var_left) - 1
    idx_right = bisect.bisect_right(list_val_a, var_right) - 1
    list_adjacent_graph[idx_left].append((idx_right, idx_edge))
    list_adjacent_graph[idx_right].append((idx_left, idx_edge))

list_node_parity = [0] * var_nodes_total
for idx_node, (val_b_prev, val_b_next) in enumerate(zip(list_val_b, list_val_b[1:])):
    if val_b_prev == 0 and val_b_next == 1:
        list_node_parity[idx_node] = 1
    if val_b_prev == 1 and val_b_next == 0:
        list_node_parity[idx_node] = 1

list_node_visited = [False] * var_nodes_total
list_all_trees_edges = []

for idx_tree_root in range(var_nodes_total):
    if list_node_visited[idx_tree_root] or not list_adjacent_graph[idx_tree_root]:
        continue
    list_stack_edges = []
    list_node_visited[idx_tree_root] = True
    list_dfs_stack = [idx_tree_root]
    while list_dfs_stack:
        idx_current_node = list_dfs_stack.pop()
        for idx_neighbor, idx_graph_edge in list_adjacent_graph[idx_current_node]:
            if list_node_visited[idx_neighbor]:
                continue
            list_node_visited[idx_neighbor] = True
            list_dfs_stack.append(idx_neighbor)
            list_stack_edges.append((idx_current_node, idx_neighbor, idx_graph_edge))
    if not list_stack_edges and list_node_parity[idx_tree_root] == 1:
        print(-1)
        exit()
    list_all_trees_edges.append(list_stack_edges)

list_adjacent_graph = [[] for _ in range(var_nodes_total)]
list_node_degrees = [0] * var_nodes_total
for list_edges_tree in list_all_trees_edges:
    for idx_from, idx_to, idx_edge_id in list_edges_tree:
        list_adjacent_graph[idx_from].append((idx_to, idx_edge_id))
        list_adjacent_graph[idx_to].append((idx_from, idx_edge_id))
        list_node_degrees[idx_from] += 1
        list_node_degrees[idx_to] += 1

list_result_edges = []
list_node_used = [False] * var_nodes_total
list_leaf_stack = [idx_node for idx_node, deg in enumerate(list_node_degrees) if deg == 1]
while list_leaf_stack:
    idx_leaf = list_leaf_stack.pop()
    if list_node_degrees[idx_leaf] == 0:
        continue
    assert list_node_degrees[idx_leaf] == 1
    if list_node_used[idx_leaf]:
        continue
    list_node_used[idx_leaf] = True
    list_node_degrees[idx_leaf] = 0
    for idx_neighbor, idx_edge_label in list_adjacent_graph[idx_leaf]:
        if list_node_used[idx_neighbor]:
            continue
        if list_node_parity[idx_leaf] == list_node_parity[idx_neighbor] == 1:
            list_node_parity[idx_leaf] = 0
            list_node_parity[idx_neighbor] = 0
            list_result_edges.append(idx_edge_label)
        elif list_node_parity[idx_leaf] == 1 and list_node_parity[idx_neighbor] == 0:
            list_node_parity[idx_leaf] = 0
            list_node_parity[idx_neighbor] = 1
            list_result_edges.append(idx_edge_label)
        list_node_degrees[idx_neighbor] -= 1
        if list_node_degrees[idx_neighbor] == 1:
            list_leaf_stack.append(idx_neighbor)

if 1 in list_node_parity:
    print(-1)
else:
    print(len(list_result_edges))
    print(*sorted(list_result_edges))