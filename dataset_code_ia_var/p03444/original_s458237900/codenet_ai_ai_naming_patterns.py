from collections import deque

def generate_child_map(parent_list):
    child_map = [set() for _ in range(node_count)]
    for node_index, parent_index in enumerate(parent_list):
        child_map[parent_index].add(node_index + 1)
    return child_map

def generate_level_map(child_map):
    level_map = []
    node_queue = deque([(0, 0)])
    while node_queue:
        current_node, current_level = node_queue.popleft()
        if node_fixed_state[current_node]:
            continue
        if len(level_map) <= current_level:
            level_map.append(set())
        level_map[current_level].add(current_node)
        node_queue.extend((child, current_level + 1) for child in child_map[current_node])
    return level_map

def generate_node_position_map():
    node_position_map = [0] * node_count
    for position, node_value in enumerate(node_array):
        node_position_map[node_value] = position
    return node_position_map

def generate_leaf_map(level_map):
    leaf_map = {}
    child_state = [-1] * node_count
    for level_index, current_level_nodes in reversed(list(enumerate(level_map))):
        for node in current_level_nodes:
            child_value = child_state[node]
            parent_index = parent_list[node - 1]
            if child_value == -1:
                if node_array[node] == node:
                    node_fixed_state[node] = True
                    continue
                else:
                    leaf_map[node] = node
                if child_state[parent_index] == -1:
                    child_state[parent_index] = node
                else:
                    child_state[parent_index] = -2
            elif child_value == -2:
                child_state[parent_index] = -2
            else:
                leaf_map[node] = child_value
                if child_state[parent_index] == -1:
                    child_state[parent_index] = child_value
                else:
                    child_state[parent_index] = -2
    return leaf_map

def assign_node(node_idx, target_value, position_map):
    result_order.append(node_idx)
    position_map[target_value] = node_idx
    temp_value, node_array[node_idx] = node_array[node_idx], target_value
    while node_idx:
        parent_idx = parent_list[node_idx - 1]
        position_map[temp_value] = parent_idx
        temp_value, node_array[parent_idx] = node_array[parent_idx], temp_value
        node_idx = parent_idx

def process_solution():
    child_map = generate_child_map(parent_list)
    while not node_fixed_state[0]:
        level_map = generate_level_map(child_map)
        leaf_map = generate_leaf_map(level_map)
        position_map = generate_node_position_map()
        while leaf_map:
            root_value = node_array[0]
            if root_value in leaf_map:
                current_index = leaf_map[root_value]
                while True:
                    current_value = node_array[current_index]
                    if not node_fixed_state[current_value] or current_value < root_value:
                        assign_node(current_index, root_value, position_map)
                        node_fixed_state[root_value] = True
                        break
                    current_index = parent_list[current_index - 1]
                del leaf_map[root_value]
            else:
                max_index = max(position_map[i] for i in leaf_map if not node_fixed_state[i])
                assign_node(max_index, root_value, position_map)

node_count = int(input())
parent_list = list(map(int, input().split()))
node_array = list(map(int, input().split()))
node_fixed_state = [False] * node_count
result_order = []
process_solution()
print(len(result_order))
print('\n'.join(map(str, result_order)))