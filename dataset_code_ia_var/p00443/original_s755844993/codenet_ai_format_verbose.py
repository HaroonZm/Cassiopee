def compute_greatest_common_divisor(first_number, second_number):
    while second_number > 0:
        first_number, second_number = second_number, first_number % second_number
    return first_number


while True:
    number_of_nodes = int(input())

    if not number_of_nodes:
        break

    node_data_list = [list(map(int, input().split())) for _ in range(number_of_nodes)]

    all_node_indices = set(range(1, number_of_nodes + 1))
    child_node_indices = set(child_index for node_data in node_data_list for child_index in node_data[2:])
    root_node_index = (all_node_indices - child_node_indices).pop()

    def compute_minimal_total_weight(ratio_right, ratio_left, left_child_index, right_child_index):
        greatest_common_divisor = compute_greatest_common_divisor(ratio_right, ratio_left)
        ratio_right //= greatest_common_divisor
        ratio_left //= greatest_common_divisor

        left_subtree_weight = compute_minimal_total_weight(*node_data_list[left_child_index - 1]) if left_child_index else 0
        right_subtree_weight = compute_minimal_total_weight(*node_data_list[right_child_index - 1]) if right_child_index else 0

        if left_subtree_weight == 0 and right_subtree_weight == 0:
            left_subtree_weight, right_subtree_weight = ratio_left, ratio_right
        elif left_subtree_weight == 0:
            right_subtree_weight = (right_subtree_weight * ratio_right) // compute_greatest_common_divisor(right_subtree_weight, ratio_right)
            left_subtree_weight = ratio_left * (right_subtree_weight // ratio_right)
        elif right_subtree_weight == 0:
            left_subtree_weight = (left_subtree_weight * ratio_left) // compute_greatest_common_divisor(left_subtree_weight, ratio_left)
            right_subtree_weight = ratio_right * (left_subtree_weight // ratio_left)
        else:
            left_product = left_subtree_weight * ratio_right
            right_product = right_subtree_weight * ratio_left
            divisor = compute_greatest_common_divisor(left_product, right_product)
            right_subtree_weight = right_subtree_weight * (left_product // divisor)
            left_subtree_weight = left_subtree_weight * (right_product // divisor)

        return right_subtree_weight + left_subtree_weight

    print(compute_minimal_total_weight(*node_data_list[root_node_index - 1]))