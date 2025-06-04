import sys
def calculate_max_distance():
    total_length, num_trees = map(int, input().split())
    input_lines = sys.stdin.readlines()

    tree_positions_ccw = [None] * num_trees
    for index in range(num_trees):
        tree_positions_ccw[index] = int(input_lines[index])

    tree_positions_cw = [total_length - tree_positions_ccw[-(index + 1)] for index in range(num_trees)]
    prefix_sum_ccw = [0] + [None] * num_trees
    prefix_sum_cw = [0] + [None] * num_trees
    for index in range(num_trees):
        prefix_sum_ccw[index + 1] = prefix_sum_ccw[index] + tree_positions_ccw[index]
        prefix_sum_cw[index + 1] = prefix_sum_cw[index] + tree_positions_cw[index]

    max_distance = 0

    for offset in range(1, num_trees + 1):
        trees_on_left = offset
        num_ccw = trees_on_left + (num_trees - trees_on_left) // 2
        num_cw = num_trees - num_ccw

        distance_case_1 = 2 * (prefix_sum_ccw[num_ccw] - prefix_sum_ccw[offset - 1]) + 2 * prefix_sum_cw[num_cw]
        distance_case_2 = 2 * (prefix_sum_cw[num_ccw] - prefix_sum_cw[offset - 1]) + 2 * prefix_sum_ccw[num_cw]

        if (num_trees - trees_on_left) % 2 == 0:
            distance_case_1 -= tree_positions_ccw[num_ccw - 1]
            distance_case_2 -= tree_positions_cw[num_ccw - 1]
        else:
            distance_case_1 -= tree_positions_cw[num_cw - 1]
            distance_case_2 -= tree_positions_ccw[num_cw - 1]

        if max_distance < distance_case_1:
            max_distance = distance_case_1

        if max_distance < distance_case_2:
            max_distance = distance_case_2

    print(max_distance)
    return

calculate_max_distance()