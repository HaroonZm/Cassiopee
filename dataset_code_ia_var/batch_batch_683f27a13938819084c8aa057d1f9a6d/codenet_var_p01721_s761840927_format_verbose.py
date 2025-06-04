def calculate_number_of_paths_to_reach_target():
    rectangle_width, rectangle_height, movement_speed, elapsed_time, target_x, target_y, starting_x, starting_y = map(int, input().split())

    def count_possible_paths(mirrored_starting_x, mirrored_starting_y):
        path_count = 0
        maximum_distance = movement_speed * elapsed_time

        vertical_reflection_index = 0
        while True:
            mirrored_y = mirrored_starting_y + 2 * rectangle_height * vertical_reflection_index
            distance_squared = maximum_distance ** 2 - (mirrored_y - target_y) ** 2
            if distance_squared < 0:
                break

            distance = distance_squared ** 0.5 + 1e-7
            lower_bound_horizontal_index = int((target_x - mirrored_starting_x - distance) // (2 * rectangle_width))
            upper_bound_horizontal_index = int((target_x - mirrored_starting_x + distance) // (2 * rectangle_width))
            number_of_solutions_at_current_vertical = max(upper_bound_horizontal_index - lower_bound_horizontal_index, 0)
            path_count += number_of_solutions_at_current_vertical

            vertical_reflection_index += 1

        vertical_reflection_index = -1
        while True:
            mirrored_y = mirrored_starting_y + 2 * rectangle_height * vertical_reflection_index
            distance_squared = maximum_distance ** 2 - (mirrored_y - target_y) ** 2
            if distance_squared < 0:
                break

            distance = distance_squared ** 0.5 + 1e-7
            lower_bound_horizontal_index = int((target_x - mirrored_starting_x - distance) // (2 * rectangle_width))
            upper_bound_horizontal_index = int((target_x - mirrored_starting_x + distance) // (2 * rectangle_width))
            number_of_solutions_at_current_vertical = max(upper_bound_horizontal_index - lower_bound_horizontal_index, 0)
            path_count += number_of_solutions_at_current_vertical

            vertical_reflection_index -= 1

        return path_count

    total_number_of_paths = 0
    for possible_start_x in [starting_x, 2 * rectangle_width - starting_x]:
        for possible_start_y in [starting_y, 2 * rectangle_height - starting_y]:
            total_number_of_paths += count_possible_paths(possible_start_x, possible_start_y)

    print(total_number_of_paths)

calculate_number_of_paths_to_reach_target()