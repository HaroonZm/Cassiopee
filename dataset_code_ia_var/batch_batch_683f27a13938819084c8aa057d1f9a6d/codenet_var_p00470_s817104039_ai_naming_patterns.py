while True:
    grid_width, grid_height = map(int, raw_input().split())
    if (grid_width | grid_height) == 0:
        break
    paths_dp = [[[0 for col in xrange(grid_width + 1)] for row in xrange(grid_height + 1)] for dir_idx in xrange(4)]
    # 0:up->up, 1:up->right, 2:right->up, 3:right->right
    paths_dp[0][1][0] = 1
    paths_dp[3][0][1] = 1
    for row_idx in xrange(grid_height):
        for col_idx in xrange(grid_width):
            paths_dp[0][row_idx + 1][col_idx] += paths_dp[0][row_idx][col_idx] + paths_dp[2][row_idx][col_idx]
            paths_dp[1][row_idx][col_idx + 1] += paths_dp[0][row_idx][col_idx]
            paths_dp[2][row_idx + 1][col_idx] += paths_dp[3][row_idx][col_idx]
            paths_dp[3][row_idx][col_idx + 1] += paths_dp[1][row_idx][col_idx] + paths_dp[3][row_idx][col_idx]
    print sum(paths_dp[dir_idx][grid_height - 1][grid_width - 1] for dir_idx in xrange(4)) % 100000