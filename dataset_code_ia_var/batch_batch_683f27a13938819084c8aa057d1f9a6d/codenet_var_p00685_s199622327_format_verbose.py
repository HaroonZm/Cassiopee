def find_first_zero_cell_index(grid_4x4):
    for row_index, row in enumerate(grid_4x4):
        try:
            column_index = row.index(0)
            return column_index, row_index
        except ValueError:
            pass

def count_recursive_placements(current_value, grid_4x4):
    if current_value == 9:
        return 1

    total_solutions = 0
    cell_x, cell_y = find_first_zero_cell_index(grid_4x4)
    grid_4x4[cell_y][cell_x] = current_value

    for delta_x, delta_y in movement_directions:
        neighbour_x = cell_x + delta_x
        neighbour_y = cell_y + delta_y

        if not (0 <= neighbour_x < 4 and 0 <= neighbour_y < 4):
            continue

        if grid_4x4[neighbour_y][neighbour_x]:
            continue

        grid_4x4[neighbour_y][neighbour_x] = current_value
        total_solutions += count_recursive_placements(current_value + 1, grid_4x4)
        grid_4x4[neighbour_y][neighbour_x] = 0

    grid_4x4[cell_y][cell_x] = 0
    return total_solutions

while True:
    user_input_numbers = list(map(int, input().split()))

    if len(user_input_numbers) == 1:
        break

    movement_directions = list(zip(*[iter(user_input_numbers)] * 2))
    empty_4x4_grid = [[0] * 4 for _ in range(4)]
    print(count_recursive_placements(1, empty_4x4_grid))