def read_input_lines():
    while True:
        try:
            yield ''.join(input())
        except EOFError:
            break


def flood_fill_connected_cells(grid_boolean, grid_labels, current_x, current_y):
    if grid_boolean[current_x - 1][current_y] and grid_labels[current_x - 1][current_y] == 0:
        grid_labels[current_x - 1][current_y] = grid_labels[current_x][current_y]
        flood_fill_connected_cells(grid_boolean, grid_labels, current_x - 1, current_y)

    if grid_boolean[current_x + 1][current_y] and grid_labels[current_x + 1][current_y] == 0:
        grid_labels[current_x + 1][current_y] = grid_labels[current_x][current_y]
        flood_fill_connected_cells(grid_boolean, grid_labels, current_x + 1, current_y)

    if grid_boolean[current_x][current_y - 1] and grid_labels[current_x][current_y - 1] == 0:
        grid_labels[current_x][current_y - 1] = grid_labels[current_x][current_y]
        flood_fill_connected_cells(grid_boolean, grid_labels, current_x, current_y - 1)

    if grid_boolean[current_x][current_y + 1] and grid_labels[current_x][current_y + 1] == 0:
        grid_labels[current_x][current_y + 1] = grid_labels[current_x][current_y]
        flood_fill_connected_cells(grid_boolean, grid_labels, current_x, current_y + 1)

    return


all_input_lines = list(read_input_lines())

for batch_start_index in range(0, len(all_input_lines), 13):

    boolean_grid = [[False for column in range(14)] for row in range(14)]

    for row_index in range(12):
        for column_index in range(12):
            if int(all_input_lines[batch_start_index + row_index][column_index]) == 1:
                boolean_grid[row_index + 1][column_index + 1] = True

    label_grid = [[0 for column in range(14)] for row in range(14)]

    connected_component_count = 0

    for row_index in range(1, 13):
        for column_index in range(1, 13):
            if boolean_grid[row_index][column_index] and label_grid[row_index][column_index] == 0:
                connected_component_count += 1
                label_grid[row_index][column_index] = connected_component_count
                flood_fill_connected_cells(boolean_grid, label_grid, row_index, column_index)

    print(connected_component_count)