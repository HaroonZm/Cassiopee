max_possible_value = 1 << 28

while True:
    number_of_points = int(raw_input())
    if number_of_points == 0:
        break

    point_time_pairs = [map(int, raw_input().split()) for _ in xrange(number_of_points)]

    position_list = [0] + [point_time_pair[0] for point_time_pair in point_time_pairs]
    time_list = [0] + [point_time_pair[1] for point_time_pair in point_time_pairs]

    minimum_cost_dp = [
        [max_possible_value] * 4
        for _ in xrange(number_of_points + 1)
    ]
    minimum_cost_dp[0][0] = 0

    for current_index in xrange(1, number_of_points + 1):
        for previous_jump in xrange(1, 4):
            required_time_for_double_jump = (previous_jump + 1) * position_list[current_index - 1] + position_list[current_index]
            available_time = time_list[current_index] - time_list[current_index - 1]
            if required_time_for_double_jump <= available_time:
                minimum_cost_dp[current_index][1] = min(
                    minimum_cost_dp[current_index][1],
                    minimum_cost_dp[current_index - 1][previous_jump] + position_list[current_index - 1] + position_list[current_index]
                )
            required_time_for_single_jump = abs(position_list[current_index - 1] - position_list[current_index]) * previous_jump
            if required_time_for_single_jump <= available_time:
                minimum_cost_dp[current_index][previous_jump] = min(
                    minimum_cost_dp[current_index][previous_jump],
                    minimum_cost_dp[current_index - 1][previous_jump - 1] + abs(position_list[current_index - 1] - position_list[current_index])
                )
        if min(minimum_cost_dp[current_index]) == max_possible_value:
            print "NG", current_index
            break

    else:
        for jump_type in xrange(1, 4):
            minimum_cost_dp[-1][jump_type] += position_list[-1]
        print "OK", min(minimum_cost_dp[number_of_points])