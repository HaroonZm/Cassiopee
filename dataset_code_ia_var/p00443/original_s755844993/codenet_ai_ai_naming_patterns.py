def calc_gcd(value_a, value_b):
    while value_b > 0:
        value_a, value_b = value_b, value_a % value_b
    return value_a

while True:
    num_nodes = int(input())
    if not num_nodes:
        break

    node_specs_list = [list(map(int, input().split())) for _ in range(num_nodes)]

    all_node_ids = set(range(1, num_nodes + 1))
    referenced_node_ids = set(node_id for node_info in node_specs_list for node_id in node_info[2:])
    root_node_id = (all_node_ids - referenced_node_ids).pop()

    def compute_total_weight(ratio_right, ratio_left, left_child_idx, right_child_idx):
        current_gcd = calc_gcd(ratio_right, ratio_left)
        norm_ratio_right = ratio_right // current_gcd
        norm_ratio_left = ratio_left // current_gcd

        left_subtree_weight = compute_total_weight(*node_specs_list[left_child_idx - 1]) if left_child_idx else 0
        right_subtree_weight = compute_total_weight(*node_specs_list[right_child_idx - 1]) if right_child_idx else 0

        if left_subtree_weight == 0 and right_subtree_weight == 0:
            left_subtree_weight, right_subtree_weight = norm_ratio_left, norm_ratio_right
        elif left_subtree_weight == 0:
            target_right_weight = (right_subtree_weight * norm_ratio_right) // calc_gcd(right_subtree_weight, norm_ratio_right)
            left_subtree_weight = norm_ratio_left * (target_right_weight // norm_ratio_right)
            right_subtree_weight = target_right_weight
        elif right_subtree_weight == 0:
            target_left_weight = (left_subtree_weight * norm_ratio_left) // calc_gcd(left_subtree_weight, norm_ratio_left)
            right_subtree_weight = norm_ratio_right * (target_left_weight // norm_ratio_left)
            left_subtree_weight = target_left_weight
        else:
            alt_right = left_subtree_weight * norm_ratio_right
            alt_left = right_subtree_weight * norm_ratio_left
            alt_gcd = calc_gcd(alt_left, alt_right)
            right_subtree_weight = right_subtree_weight * (alt_right // alt_gcd)
            left_subtree_weight = left_subtree_weight * (alt_left // alt_gcd)

        return left_subtree_weight + right_subtree_weight

    print(compute_total_weight(*node_specs_list[root_node_id - 1]))