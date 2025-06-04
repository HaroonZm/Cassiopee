while True:

    grid_width, grid_height = map(int, input().split())

    if grid_width == 0 and grid_height == 0:
        break

    num_blocked_cells = int(input())

    num_paths_to_cell = [[1] * (grid_width + 1) for _ in range(grid_height + 1)]

    # Set first row to 0 except for origin
    num_paths_to_cell[0] = [0] * (grid_width + 1)

    # Set first column entries to 0 except for origin
    for row_index in range(2, grid_height + 1):
        num_paths_to_cell[row_index][0] = 0

    # Block specified cells
    for _ in range(num_blocked_cells):
        blocked_x, blocked_y = map(int, input().split())
        num_paths_to_cell[blocked_y][blocked_x] = 0

    # Dynamic programming to count paths
    for current_x in range(1, grid_width + 1):
        for current_y in range(1, grid_height + 1):

            if num_paths_to_cell[current_y][current_x] == 0:
                continue

            num_paths_to_cell[current_y][current_x] = (
                num_paths_to_cell[current_y - 1][current_x] +
                num_paths_to_cell[current_y][current_x - 1]
            )

    print(num_paths_to_cell[grid_height][grid_width])