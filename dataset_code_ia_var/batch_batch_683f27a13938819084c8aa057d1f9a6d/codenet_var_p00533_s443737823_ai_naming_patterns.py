row_count, col_count = map(int, input().split())
cloud_grid = [list(input()) for _ in range(row_count)]

for row_index in range(row_count):
    has_cloud = False
    cloud_distance = 0
    for col_index in range(col_count):
        current_cell = cloud_grid[row_index][col_index]
        is_last_col = (col_index == col_count - 1)

        if current_cell == 'c':
            print(0, end='' if is_last_col else ' ')
            has_cloud = True
            cloud_distance = 0
        elif has_cloud:
            cloud_distance += 1
            print(cloud_distance, end='' if is_last_col else ' ')
        else:
            print(-1, end='' if is_last_col else ' ')
    print()