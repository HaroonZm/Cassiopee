from collections import deque

def generate_children_list(parent_list):
    child_set_list = [set() for _ in range(tree_size)]
    for child_index, parent_index in enumerate(parent_list):
        child_set_list[parent_index].add(child_index + 1)
    return child_set_list

def build_level_structures(children_structure):
    level_nodes_list = []
    node_level_map = {}
    bfs_queue = deque([(0, 0)])
    while bfs_queue:
        node_id, level = bfs_queue.popleft()
        if node_fixed_list[node_id]:
            continue
        if len(level_nodes_list) <= level:
            level_nodes_list.append(set())
        level_nodes_list[level].add(node_id)
        node_level_map[node_id] = level
        bfs_queue.extend((child_id, level + 1) for child_id in children_structure[node_id])
    return level_nodes_list, node_level_map

def create_position_map(arranged_list):
    position_lookup_list = [0] * tree_size
    for pos, val in enumerate(arranged_list):
        position_lookup_list[val] = pos
    return position_lookup_list

def find_tree_leaves(level_list):
    leaves_map = {}
    child_result_list = [-1] * tree_size
    for curr_level, nodes_in_level in reversed(list(enumerate(level_list))):
        for node in nodes_in_level:
            curr_result = child_result_list[node]
            parent_index = parent_list[node - 1]
            if curr_result == -2:
                child_result_list[parent_index] = -2
                continue
            if curr_result == -1:
                if current_arrangement[node] == node:
                    node_fixed_list[node] = True
                    continue
                leaves_map[node] = node
                curr_result = node
            else:
                leaves_map[node] = curr_result
            if child_result_list[parent_index] == -1:
                child_result_list[parent_index] = curr_result
            else:
                child_result_list[parent_index] = -2
    return leaves_map

def perform_move(target_idx, val):
    operation_buffer.append(target_idx)
    position_map[val] = target_idx
    val, current_arrangement[target_idx] = current_arrangement[target_idx], val
    while target_idx:
        parent_idx = parent_list[target_idx - 1]
        position_map[val] = parent_idx
        val, current_arrangement[parent_idx] = current_arrangement[parent_idx], val
        target_idx = parent_idx

def resolve_tree():
    child_structure = generate_children_list(parent_list)
    level_list, level_map = build_level_structures(child_structure)
    while not node_fixed_list[0]:
        leaves_nodes = find_tree_leaves(level_list)
        while leaves_nodes:
            root_value = current_arrangement[0]
            if root_value in leaves_nodes:
                grandchild_index = leaves_nodes[root_value]
                while True:
                    val_to_check = current_arrangement[grandchild_index]
                    if not node_fixed_list[val_to_check] or val_to_check < root_value:
                        perform_move(grandchild_index, root_value)
                        node_fixed_list[root_value] = True
                        break
                    grandchild_index = parent_list[grandchild_index - 1]
                del leaves_nodes[root_value]
            else:
                max_level, max_index = max((level_map[position_map[node]], position_map[node]) for node in leaves_nodes)
                perform_move(max_index, root_value)

tree_size = int(input())
parent_list = list(map(int, input().split()))
current_arrangement = list(map(int, input().split()))
position_map = create_position_map(current_arrangement)
node_fixed_list = [False] * tree_size
operation_buffer = []
resolve_tree()
print(len(operation_buffer))
print('\n'.join(map(str, operation_buffer)))