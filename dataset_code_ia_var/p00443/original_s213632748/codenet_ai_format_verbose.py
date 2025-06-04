def compute_least_common_multiple(value_a, value_b):
    return value_a // compute_greatest_common_divisor(value_a, value_b) * value_b

def compute_greatest_common_divisor(value_a, value_b):
    while value_b != 0:
        remainder = value_a % value_b
        value_a, value_b = value_b, remainder
    return value_a

def compute_total_weight(node_index):
    if node_structure_list[node_index][2] > 0:
        right_branch_weight = compute_total_weight(node_structure_list[node_index][2])
    else:
        right_branch_weight = 1

    if node_structure_list[node_index][3] > 0:
        left_branch_weight = compute_total_weight(node_structure_list[node_index][3])
    else:
        left_branch_weight = 1

    combined_weight = compute_least_common_multiple(
        node_structure_list[node_index][0] * right_branch_weight,
        node_structure_list[node_index][1] * left_branch_weight
    )

    return combined_weight // node_structure_list[node_index][0] + combined_weight // node_structure_list[node_index][1]

while True:
    number_of_nodes = int(input())
    if number_of_nodes == 0:
        break

    parent_index_list = [0] * (number_of_nodes + 1)
    node_structure_list = [(0, 0, 0, 0)]

    for current_node_index in range(1, number_of_nodes + 1):
        right_distance, left_distance, right_child_index, left_child_index = map(int, input().split())
        node_structure_list.append(
            (right_distance, left_distance, right_child_index, left_child_index)
        )
        if right_child_index > 0:
            parent_index_list[right_child_index] = current_node_index
        if left_child_index > 0:
            parent_index_list[left_child_index] = current_node_index

    for possible_root_index in range(1, number_of_nodes + 1):
        if parent_index_list[possible_root_index] == 0:
            break

    print(compute_total_weight(possible_root_index))