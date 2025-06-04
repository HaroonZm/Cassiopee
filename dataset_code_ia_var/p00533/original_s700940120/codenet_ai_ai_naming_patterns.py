height, width = map(int, input().split())
grid = [list(input()) for _ in range(height)]
result = [[0] * width for _ in range(height)]

for row_idx in range(height):
    for col_idx in range(width):
        if grid[row_idx][col_idx] == '.':
            has_cloud_left = False
            for check_col_idx in range(col_idx):
                if grid[row_idx][check_col_idx] == 'c':
                    has_cloud_left = True
                    break
            if not has_cloud_left:
                result[row_idx][col_idx] = -1
            else:
                for offset in range(1, col_idx + 1):
                    if grid[row_idx][col_idx - offset] == 'c':
                        result[row_idx][col_idx] = offset
                        break
for result_row in result:
    print(*result_row)