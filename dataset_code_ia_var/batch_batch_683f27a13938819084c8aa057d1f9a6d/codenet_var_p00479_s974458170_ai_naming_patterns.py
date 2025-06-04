def input_integer():
    return int(input())

def input_integer_list():
    return list(map(int, input().split()))

def compute_cell_color(grid_size, cell_coordinates):
    row_index, col_index = cell_coordinates
    if row_index > grid_size // 2:
        row_index = grid_size - row_index + 1
    if col_index > grid_size // 2:
        col_index = grid_size - col_index + 1

    if row_index == col_index:
        cell_color = ((row_index - 1) % 3) + 1
    else:
        min_coordinate = min(row_index, col_index)
        cell_color = ((min_coordinate - 1) % 3) + 1
    return cell_color

grid_size = input_integer()
query_count = input_integer()

for query_index in range(query_count):
    cell_coordinates = input_integer_list()
    print(compute_cell_color(grid_size, cell_coordinates))