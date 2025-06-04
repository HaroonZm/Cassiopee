def find_first_zero_position(grid_data):
    for row_index, row in enumerate(grid_data):
        try:
            column_index = row.index(0)
            return column_index, row_index
        except ValueError:
            pass

def depth_first_fill(number_to_place, grid_data):
    if number_to_place == 9:
        return 1

    total_solutions = 0
    column, row = find_first_zero_position(grid_data)
    grid_data[row][column] = number_to_place

    for offset_x, offset_y in movement_directions:
        neighbor_column = column + offset_x
        neighbor_row = row + offset_y
        if not (0 <= neighbor_column < 4 and 0 <= neighbor_row < 4):
            continue
        if grid_data[neighbor_row][neighbor_column] != 0:
            continue
        grid_data[neighbor_row][neighbor_column] = number_to_place
        total_solutions += depth_first_fill(number_to_place + 1, grid_data)
        grid_data[neighbor_row][neighbor_column] = 0

    grid_data[row][column] = 0
    return total_solutions

while True:
    user_input_numbers = list(map(int, input().split()))
    if len(user_input_numbers) == 1:
        break
    movement_directions = list(zip(*[iter(user_input_numbers)] * 2))
    empty_4_by_4_grid = [[0 for _ in range(4)] for _ in range(4)]
    print(depth_first_fill(1, empty_4_by_4_grid))