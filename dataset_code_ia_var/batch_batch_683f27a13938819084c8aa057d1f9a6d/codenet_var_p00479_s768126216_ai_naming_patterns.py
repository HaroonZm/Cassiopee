input_board_size = input()
for _ in [1] * input():
    pos_x, pos_y = map(int, raw_input().split())
    dist_left = pos_x - 1
    dist_right = input_board_size - pos_x
    dist_top = pos_y - 1
    dist_bottom = input_board_size - pos_y
    min_dist = min(dist_left, dist_right, dist_top, dist_bottom)
    result_value = min_dist % 3 + 1
    print result_value