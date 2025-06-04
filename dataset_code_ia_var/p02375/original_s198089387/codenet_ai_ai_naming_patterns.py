from collections import deque

import sys
sys.setrecursionlimit(10**6)
input_reader = sys.stdin.readline
output_writer = sys.stdout.write

node_count = int(input_reader())
tree_adj = [None] * node_count
for node_idx in range(node_count):
    node_data = list(map(int, input_reader().split()))
    child_count, *child_nodes = node_data
    tree_adj[node_idx] = child_nodes

heavy_child = [0] * node_count
parent_node = [None] * node_count

def dfs_find_heavy_child(current):
    subtree_size = 1
    max_subtree = 0
    heavy = None
    for child in tree_adj[current]:
        parent_node[child] = current
        child_size = dfs_find_heavy_child(child)
        if child_size > max_subtree:
            heavy = child
            max_subtree = child_size
        subtree_size += child_size
    heavy_child[current] = heavy
    return subtree_size

dfs_find_heavy_child(0)

hld_paths = []
hld_depths = []
node_path = [0] * node_count
node_index_in_path = [0] * node_count
hld_queue = deque([(0, 0)])

while hld_queue:
    start_node, path_depth = hld_queue.popleft()
    path_nodes = []
    path_id = len(hld_paths)
    current_node = start_node
    while current_node is not None:
        node_index_in_path[current_node] = len(path_nodes)
        path_nodes.append(current_node)
        node_path[current_node] = path_id
        heavy = heavy_child[current_node]
        for adj_node in tree_adj[current_node]:
            if adj_node == heavy:
                continue
            hld_queue.append((adj_node, path_depth + 1))
        current_node = heavy
    hld_paths.append(path_nodes)
    hld_depths.append(path_depth)

path_lengths = list(map(len, hld_paths))
bit_tree_0 = [[0] * (pl + 1) for pl in path_lengths]
bit_tree_1 = [[0] * (pl + 1) for pl in path_lengths]

def bit_add(tree_size, bit_tree, tree_idx, add_val):
    while tree_idx <= tree_size:
        bit_tree[tree_idx] += add_val
        tree_idx += tree_idx & -tree_idx

def bit_query(tree_size, bit_tree, tree_idx):
    query_sum = 0
    while tree_idx:
        query_sum += bit_tree[tree_idx]
        tree_idx -= tree_idx & -tree_idx
    return query_sum

def update_path_add(target_node, add_val):
    while target_node is not None:
        path_id = node_path[target_node]
        node_idx = node_index_in_path[target_node]
        bit_add(path_lengths[path_id], bit_tree_1[path_id], node_idx + 1, -add_val)
        bit_add(path_lengths[path_id], bit_tree_1[path_id], 1, add_val)
        bit_add(path_lengths[path_id], bit_tree_0[path_id], node_idx + 1, add_val * (node_idx + 1))
        target_node = parent_node[hld_paths[path_id][0]]

def query_path_sum(target_node):
    total = - bit_query(path_lengths[0], bit_tree_1[0], 1) - bit_query(path_lengths[0], bit_tree_0[0], 1)
    while target_node is not None:
        path_id = node_path[target_node]
        node_idx = node_index_in_path[target_node]
        total += bit_query(path_lengths[path_id], bit_tree_1[path_id], node_idx + 1) * (node_idx + 1)
        total += bit_query(path_lengths[path_id], bit_tree_0[path_id], node_idx + 1)
        target_node = parent_node[hld_paths[path_id][0]]
    return total

query_count = int(input_reader())
output_list = []
for _ in range(query_count):
    query_data = list(map(int, input_reader().split()))
    query_type = query_data[0]
    if query_type:
        query_node = query_data[1]
        output_list.append(str(query_path_sum(query_node)))
    else:
        update_node, update_value = query_data[1], query_data[2]
        update_path_add(update_node, update_value)
output_writer("\n".join(output_list))
output_writer("\n")