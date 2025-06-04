INFINITY = 10 ** 9

while True:

    number_of_segments = int(input())

    if number_of_segments == 0:
        break

    segment_positions_and_limits = [(0, 0)]
    segment_positions_and_limits.extend([
        tuple(map(int, input().split()))
        for segment_index in range(number_of_segments)
    ])

    minimum_cost_dp = [
        [INFINITY] * 4
        for segment_index in range(number_of_segments + 1)
    ]
    minimum_cost_dp[0][0] = 0

    for current_segment_index in range(number_of_segments):

        did_state_update = False

        for jump_count in range(4):

            if minimum_cost_dp[current_segment_index][jump_count] is INFINITY:
                continue

            current_position = segment_positions_and_limits[current_segment_index][0]
            next_position = segment_positions_and_limits[current_segment_index + 1][0]

            if (
                jump_count <= 2 and 
                segment_positions_and_limits[current_segment_index][1] +
                    abs(next_position - current_position) * (jump_count + 1)
                    <= segment_positions_and_limits[current_segment_index + 1][1]
                and
                minimum_cost_dp[current_segment_index + 1][jump_count + 1] >
                    minimum_cost_dp[current_segment_index][jump_count] +
                    abs(next_position - current_position)
            ):
                minimum_cost_dp[current_segment_index + 1][jump_count + 1] = (
                    minimum_cost_dp[current_segment_index][jump_count] +
                    abs(next_position - current_position)
                )
                did_state_update = True

            regular_move_cost = (
                segment_positions_and_limits[current_segment_index][1] +
                current_position * (jump_count + 1) +
                next_position
            )

            if (
                regular_move_cost <= segment_positions_and_limits[current_segment_index + 1][1]
                and
                minimum_cost_dp[current_segment_index + 1][1] >
                    minimum_cost_dp[current_segment_index][jump_count] +
                    next_position + current_position
            ):
                minimum_cost_dp[current_segment_index + 1][1] = (
                    minimum_cost_dp[current_segment_index][jump_count] +
                    next_position + current_position
                )
                did_state_update = True

        if not did_state_update:
            print('NG', current_segment_index + 1)
            break

    if did_state_update:
        print('OK', min(minimum_cost_dp[number_of_segments]) + segment_positions_and_limits[number_of_segments][0])