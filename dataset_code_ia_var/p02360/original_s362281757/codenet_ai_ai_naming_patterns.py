rect_count = int(input())
grid_width = 1001
grid_height = 1001

grid_mark = [[0] * grid_width for _ in range(grid_height)]
grid_row_prefix = [[0] * grid_width for _ in range(grid_height)]
grid_sum = [[0] * grid_width for _ in range(grid_height)]

for _ in range(rect_count):
    x_start, y_start, x_end, y_end = map(int, input().split())
    grid_mark[y_start][x_start] += 1
    grid_mark[y_start][x_end] -= 1
    grid_mark[y_end][x_start] -= 1
    grid_mark[y_end][x_end] += 1

for row_idx in range(grid_height):
    grid_row_prefix[row_idx][0] = grid_mark[row_idx][0]
    for col_idx in range(1, grid_width):
        grid_row_prefix[row_idx][col_idx] = grid_mark[row_idx][col_idx] + grid_row_prefix[row_idx][col_idx - 1]

for col_idx in range(grid_width):
    grid_sum[0][col_idx] = grid_row_prefix[0][col_idx]
    for row_idx in range(1, grid_height):
        grid_sum[row_idx][col_idx] = grid_row_prefix[row_idx][col_idx] + grid_sum[row_idx - 1][col_idx]

max_cover = 0
for row_idx in range(grid_height):
    row_max = max(grid_sum[row_idx])
    if row_max > max_cover:
        max_cover = row_max

print(max_cover)