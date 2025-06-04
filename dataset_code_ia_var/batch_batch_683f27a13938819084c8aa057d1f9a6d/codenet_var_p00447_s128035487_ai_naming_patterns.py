while True:
    num_points_p = input()
    if num_points_p == 0:
        break
    set_points_p = set([tuple(map(int, raw_input().split())) for _ in range(num_points_p)])
    num_points_q = input()
    set_points_q = set([tuple(map(int, raw_input().split())) for _ in xrange(num_points_q)])
    is_found = False
    for point_p_x, point_p_y in set_points_p:
        if is_found:
            break
        for point_q_x, point_q_y in set_points_q:
            if is_found:
                break
            shift_x = point_q_x - point_p_x
            shift_y = point_q_y - point_p_y
            for point_check_x, point_check_y in set_points_p:
                mapped_x = point_check_x + shift_x
                mapped_y = point_check_y + shift_y
                if (mapped_x, mapped_y) not in set_points_q:
                    break
            else:
                print shift_x, shift_y
                is_found = True