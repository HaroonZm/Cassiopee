while True:
    input_height, input_width = map(int, input().split())
    if input_height == 0:
        break
    grid_height = input_height - 1
    grid_width = input_width - 1
    path_dp = {
        (0, 2, 'U_U'): 1,
        (2, 0, 'R_R'): 1,
        (1, 1, 'U_R'): 1,
        (1, 1, 'R_U'): 1
    }
    for row in range(grid_height + 1):
        for col in range(grid_width + 1):
            if row + col <= 2:
                continue
            path_dp[(row, col, 'U_U')] = 0
            if (row, col - 1, 'U_U') in path_dp:
                path_dp[(row, col, 'U_U')] += path_dp[(row, col - 1, 'U_U')]
            if (row, col - 1, 'R_U') in path_dp:
                path_dp[(row, col, 'U_U')] += path_dp[(row, col - 1, 'R_U')]
            path_dp[(row, col, 'R_R')] = 0
            if (row - 1, col, 'R_R') in path_dp:
                path_dp[(row, col, 'R_R')] += path_dp[(row - 1, col, 'R_R')]
            if (row - 1, col, 'U_R') in path_dp:
                path_dp[(row, col, 'R_R')] += path_dp[(row - 1, col, 'U_R')]
            path_dp[(row, col, 'U_R')] = 0
            if (row - 1, col, 'U_U') in path_dp:
                path_dp[(row, col, 'U_R')] += path_dp[(row - 1, col, 'U_U')]
            path_dp[(row, col, 'R_U')] = 0
            if (row, col - 1, 'R_R') in path_dp:
                path_dp[(row, col, 'R_U')] += path_dp[(row, col - 1, 'R_R')]
    result_total_paths = (
        path_dp.get((grid_height, grid_width, 'U_U'), 0) +
        path_dp.get((grid_height, grid_width, 'U_R'), 0) +
        path_dp.get((grid_height, grid_width, 'R_U'), 0) +
        path_dp.get((grid_height, grid_width, 'R_R'), 0)
    )
    print(result_total_paths % 100000)