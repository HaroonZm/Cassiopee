import sys
input_reader = sys.stdin.readline

def get_parent_order(adj_list, root_node):
    node_count = len(adj_list)
    parent_list = [0] * node_count
    parent_list[root_node] = -1
    node_stack = [root_node]
    traversal_order = []
    visited_nodes = set([root_node])
    push_to_stack = node_stack.append
    push_to_order = traversal_order.append
    while node_stack:
        current_node = node_stack.pop()
        push_to_order(current_node)
        for neighbor_node in adj_list[current_node]:
            if neighbor_node in visited_nodes:
                continue
            visited_nodes.add(neighbor_node)
            parent_list[neighbor_node] = current_node
            push_to_stack(neighbor_node)
    return parent_list, traversal_order

def get_children_list(parent_list):
    children_list = [[] for _ in range(len(parent_list))]
    for node_idx, parent_val in enumerate(parent_list[1:], 1):
        children_list[parent_val].append(node_idx)
    return children_list

def calc_distance_from_sources(source_nodes, node_count, adj_list):
    distance = [0] * node_count
    temp_stack = source_nodes[:]
    visited_flag = [False] * node_count
    for source_node in source_nodes:
        visited_flag[source_node] = True
    while temp_stack:
        current_node = temp_stack.pop()
        for neighbor in adj_list[current_node]:
            if not visited_flag[neighbor]:
                visited_flag[neighbor] = True
                distance[neighbor] = 1 + distance[current_node]
                temp_stack.append(neighbor)
    return distance

node_count = int(input_reader())
adjacency_list = [[] for _ in range(node_count)]
for _ in range(node_count - 1):
    node_a, node_b = map(int, input_reader().split())
    node_a -= 1
    node_b -= 1
    adjacency_list[node_a].append(node_b)
    adjacency_list[node_b].append(node_a)

distance_from_0 = calc_distance_from_sources([0], node_count, adjacency_list)
farthest_from_0 = distance_from_0.index(max(distance_from_0))
distance_from_far = calc_distance_from_sources([farthest_from_0], node_count, adjacency_list)
farthest_end = distance_from_far.index(max(distance_from_far))
distance_from_end = calc_distance_from_sources([farthest_end], node_count, adjacency_list)

diameter_length = distance_from_far[farthest_end]
diameter_path_nodes = []
for node_idx in range(node_count):
    if distance_from_far[node_idx] + distance_from_end[node_idx] == diameter_length:
        diameter_path_nodes.append(node_idx)

if max(calc_distance_from_sources(diameter_path_nodes, node_count, adjacency_list)) > 1:
    print(-1)
else:
    diameter_path_nodes.sort(key=lambda x: distance_from_far[x])

    permute_list_1 = [None] * node_count
    current_count = 1
    external_count = 0
    node_index_seq = 0
    path_nodes_set = set(diameter_path_nodes)
    for path_idx in range(diameter_length + 1):
        curr_node = diameter_path_nodes[path_idx]
        external_count = 0
        for adj_node in adjacency_list[curr_node]:
            if adj_node in path_nodes_set:
                continue
            external_count += 1
            permute_list_1[node_index_seq] = current_count + external_count
            node_index_seq += 1
        permute_list_1[node_index_seq] = current_count
        node_index_seq += 1
        current_count = current_count + external_count + 1

    permute_list_2 = [None] * node_count
    current_count = 1
    external_count = 0
    node_index_seq = 0
    for path_idx in range(diameter_length + 1):
        curr_node = diameter_path_nodes[diameter_length - path_idx]
        external_count = 0
        for adj_node in adjacency_list[curr_node]:
            if adj_node in path_nodes_set:
                continue
            external_count += 1
            permute_list_2[node_index_seq] = current_count + external_count
            node_index_seq += 1
        permute_list_2[node_index_seq] = current_count
        node_index_seq += 1
        current_count = current_count + external_count + 1

    print(*min(permute_list_1, permute_list_2))