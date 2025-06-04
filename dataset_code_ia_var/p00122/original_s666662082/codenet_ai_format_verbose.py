def is_path_exist_through_grid_with_constraints(grid_layers, current_x, current_y, current_depth, total_layers):

    if current_depth == total_layers:
        return True

    if current_x < 0 or current_x >= 10 or current_y < 0 or current_y >= 10:
        return False

    if current_depth >= 0 and grid_layers[current_x][current_y][current_depth] == 0:
        return False

    next_depth = current_depth + 1

    # Explore all direction
    if is_path_exist_through_grid_with_constraints(grid_layers, current_x-2, current_y-1, next_depth, total_layers):
        return True

    if is_path_exist_through_grid_with_constraints(grid_layers, current_x-2, current_y, next_depth, total_layers):
        return True

    if is_path_exist_through_grid_with_constraints(grid_layers, current_x-2, current_y+1, next_depth, total_layers):
        return True

    if is_path_exist_through_grid_with_constraints(grid_layers, current_x-1, current_y-2, next_depth, total_layers):
        return True

    if is_path_exist_through_grid_with_constraints(grid_layers, current_x, current_y-2, next_depth, total_layers):
        return True

    if is_path_exist_through_grid_with_constraints(grid_layers, current_x+1, current_y-2, next_depth, total_layers):
        return True

    if is_path_exist_through_grid_with_constraints(grid_layers, current_x+2, current_y-1, next_depth, total_layers):
        return True

    if is_path_exist_through_grid_with_constraints(grid_layers, current_x+2, current_y, next_depth, total_layers):
        return True

    if is_path_exist_through_grid_with_constraints(grid_layers, current_x+2, current_y+1, next_depth, total_layers):
        return True

    if is_path_exist_through_grid_with_constraints(grid_layers, current_x-1, current_y+2, next_depth, total_layers):
        return True

    if is_path_exist_through_grid_with_constraints(grid_layers, current_x, current_y+2, next_depth, total_layers):
        return True

    if is_path_exist_through_grid_with_constraints(grid_layers, current_x+1, current_y+2, next_depth, total_layers):
        return True

    return False


while True:

    starting_position_input = [int(value) for value in input().split()]
    starting_x, starting_y = starting_position_input

    if starting_x == 0 and starting_y == 0:
        break

    grid_layers = [
        [
            [0 for depth_index in range(10)]
            for column_index in range(10)
        ]
        for row_index in range(10)
    ]

    number_of_layers = int(input())
    trap_coordinates_flat_list = [int(value) for value in input().split()]

    for trap_index in range(0, len(trap_coordinates_flat_list), 2):

        trap_x = trap_coordinates_flat_list[trap_index]
        trap_y = trap_coordinates_flat_list[trap_index + 1]

        trap_x_min = max(trap_x - 1, 0)
        trap_y_min = max(trap_y - 1, 0)
        trap_x_max = min(trap_x + 1, 9)
        trap_y_max = min(trap_y + 1, 9)

        layer_number = trap_index // 2

        grid_layers[trap_x_min][trap_y_min][layer_number] = 1
        grid_layers[trap_x_min][trap_y][layer_number] = 1
        grid_layers[trap_x_min][trap_y_max][layer_number] = 1
        grid_layers[trap_x][trap_y_min][layer_number] = 1
        grid_layers[trap_x][trap_y][layer_number] = 1
        grid_layers[trap_x][trap_y_max][layer_number] = 1
        grid_layers[trap_x_max][trap_y_min][layer_number] = 1
        grid_layers[trap_x_max][trap_y][layer_number] = 1
        grid_layers[trap_x_max][trap_y_max][layer_number] = 1

    if is_path_exist_through_grid_with_constraints(grid_layers, starting_x, starting_y, -1, number_of_layers):
        print("OK")
    else:
        print("NA")