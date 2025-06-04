current_height = 0
current_width = 0
number_of_obstacles = 0

while True:
    current_height, current_width = map(int, input().split())

    if current_height == 0 and current_width == 0:
        break

    max_row_index = current_height - 1
    max_col_index = current_width - 1

    obstacle_grid = [[1] * (max_col_index + 1) for _ in range(max_row_index + 1)]

    number_of_obstacles = int(input())
    for _ in range(number_of_obstacles):
        obstacle_row, obstacle_col = map(int, input().split())
        obstacle_grid[obstacle_row - 1][obstacle_col - 1] = 0

    path_count_grid = [[0] * (max_col_index + 2) for _ in range(max_row_index + 2)]
    path_count_grid[0][0] = obstacle_grid[0][0]

    for row_index in range(max_row_index + 1):
        for col_index in range(max_col_index + 1):
            if obstacle_grid[row_index][col_index]:
                path_count_grid[row_index + 1][col_index] += path_count_grid[row_index][col_index]
                path_count_grid[row_index][col_index + 1] += path_count_grid[row_index][col_index]

    if obstacle_grid[max_row_index][max_col_index]:
        print(path_count_grid[max_row_index][max_col_index])
    else:
        print(0)