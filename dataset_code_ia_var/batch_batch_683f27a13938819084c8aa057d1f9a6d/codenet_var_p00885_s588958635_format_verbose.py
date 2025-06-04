INFINITY_COST = 10 ** 9

while True:
    number_of_points_input = input()
    if not number_of_points_input:
        break

    number_of_points = int(number_of_points_input)
    minimum_cost_per_visited_points = [INFINITY_COST] * 5
    minimum_cost_per_visited_points[0] = 0

    current_position = 0
    current_time = 0
    failed_point_index = -1

    positions_list = []
    times_list = []

    for point_index in range(number_of_points):
        next_position, next_time = map(int, raw_input().split())
        positions_list.append(next_position)
        times_list.append(next_time)

    for point_index in range(number_of_points):
        next_position = positions_list[point_index]
        next_time = times_list[point_index]

        position_difference = abs(next_position - current_position)
        was_step_possible = False
        minimum_recover_cost = INFINITY_COST

        for number_of_visits in range(3, -1 if point_index == 0 else 0, -1):
            minimum_cost_per_visited_points[number_of_visits + 1] = INFINITY_COST

            if minimum_cost_per_visited_points[number_of_visits] == INFINITY_COST:
                continue

            if number_of_visits < 3 and position_difference * (number_of_visits + 1) <= next_time - current_time:
                was_step_possible = True
                minimum_cost_per_visited_points[number_of_visits + 1] = minimum_cost_per_visited_points[number_of_visits] + position_difference

            if current_position * (number_of_visits + 1) + next_position <= next_time - current_time:
                minimum_recover_cost = min(minimum_recover_cost, minimum_cost_per_visited_points[number_of_visits] + current_position + next_position)
                was_step_possible = True

        minimum_cost_per_visited_points[1] = minimum_recover_cost

        if not was_step_possible:
            failed_point_index = point_index + 1
            break

        current_position = next_position
        current_time = next_time

    if failed_point_index != -1:
        print "NG", failed_point_index
    else:
        print "OK", (min(minimum_cost_per_visited_points[1:]) + next_position)