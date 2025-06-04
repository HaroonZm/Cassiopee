from collections import deque
from functools import reduce
from itertools import zip_longest
from operator import mul

def find_longest_path(tree_adjacency_lists):
    initial_queue = deque([(adjacent_node, 0) for adjacent_node in tree_adjacency_lists[0]])
    last_node_visited = 0
    
    while initial_queue:
        current_node, parent_node = initial_queue.popleft()
        last_node_visited = current_node
        for neighbor in tree_adjacency_lists[current_node]:
            if neighbor != parent_node:
                initial_queue.append((neighbor, current_node))

    parent_of_node = [-1] * len(tree_adjacency_lists)
    reconstruct_queue = deque([(neighbor, last_node_visited) for neighbor in tree_adjacency_lists[last_node_visited]])
    path_start_node, _ = 0, 0

    while reconstruct_queue:
        current_node, parent = reconstruct_queue.popleft()
        parent_of_node[current_node] = parent
        for neighbor in tree_adjacency_lists[current_node]:
            if neighbor != parent:
                reconstruct_queue.append((neighbor, current_node))
    
    path_from_last_to_first = [path_start_node]
    ancestor_pointer = path_start_node
    while ancestor_pointer != last_node_visited:
        ancestor_pointer = parent_of_node[ancestor_pointer]
        path_from_last_to_first.append(ancestor_pointer)
    
    return path_from_last_to_first

def compute_max_branching(tree_adjacency_lists, current_root, except_parent, required_depth):
    max_children_per_level = [1] * required_depth
    exploration_queue = deque([
        (adjacent_node, current_root, 1)
        for adjacent_node in tree_adjacency_lists[current_root]
        if adjacent_node != except_parent
    ])
    
    max_children_per_level[0] = len(exploration_queue)
    
    while exploration_queue:
        node, parent, level = exploration_queue.popleft()
        max_children_per_level[level] = max(
            max_children_per_level[level], 
            len(tree_adjacency_lists[node]) - 1
        )
        for neighbor in tree_adjacency_lists[node]:
            if neighbor != parent:
                exploration_queue.append((neighbor, node, level + 1))
    return max_children_per_level

def solve_tree_properties(number_of_nodes, tree_adjacency_lists):
    if number_of_nodes == 2:
        return 1, 2

    path_between_leaves = find_longest_path(tree_adjacency_lists)
    path_length = len(path_between_leaves)
    half_path_length = (path_length + 1) // 2

    if path_length % 2 == 0:
        mid_left_node = path_between_leaves[path_length // 2 - 1]
        mid_right_node = path_between_leaves[path_length // 2]
        left_branching = compute_max_branching(tree_adjacency_lists, mid_left_node, mid_right_node, half_path_length)
        right_branching = compute_max_branching(tree_adjacency_lists, mid_right_node, mid_left_node, half_path_length)
        
        total_leaf_count = 1
        for left_count, right_count in zip(left_branching, right_branching):
            total_leaf_count *= max(left_count, right_count)
        return len(left_branching), total_leaf_count * 2

    central_node = path_between_leaves[path_length // 2]
    central_branching = compute_max_branching(tree_adjacency_lists, central_node, None, half_path_length)
    minimal_leaf_count = reduce(mul, central_branching, 1)
    for neighbor in tree_adjacency_lists[central_node]:
        neighbor_to_central = compute_max_branching(tree_adjacency_lists, neighbor, central_node, half_path_length)
        central_to_neighbor = compute_max_branching(tree_adjacency_lists, central_node, neighbor, half_path_length)
        branching_product = 1
        for nb_count, cn_count in zip_longest(neighbor_to_central, central_to_neighbor):
            branching_product *= max(nb_count, cn_count)
        minimal_leaf_count = min(minimal_leaf_count, branching_product * 2)
    return len(central_branching), minimal_leaf_count

number_of_nodes = int(input())
tree_adjacency_lists = [set() for _ in range(number_of_nodes)]
for _ in range(number_of_nodes - 1):
    node_a, node_b = map(int, input().split())
    node_a -= 1
    node_b -= 1
    tree_adjacency_lists[node_a].add(node_b)
    tree_adjacency_lists[node_b].add(node_a)

result_depth, result_leaves = solve_tree_properties(number_of_nodes, tree_adjacency_lists)
print(result_depth, result_leaves)