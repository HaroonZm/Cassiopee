while True:
    width, height = map(int, input().split())
    if width == height == 0:
        break
    
    blocked_count = int(input())
    paths_grid = [[1] * (width + 1) for _ in range(height + 1)]
    paths_grid[0] = [0] * (width + 1)
    for row_index in range(2, height + 1):
        paths_grid[row_index][0] = 0

    for _ in range(blocked_count):
        blocked_x, blocked_y = map(int, input().split())
        paths_grid[blocked_y][blocked_x] = 0

    for column_index in range(1, width + 1):
        for row_index in range(1, height + 1):
            if paths_grid[row_index][column_index] == 0:
                continue
            paths_grid[row_index][column_index] = paths_grid[row_index - 1][column_index] + paths_grid[row_index][column_index - 1]
    
    print(paths_grid[height][width])