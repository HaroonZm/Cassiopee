MAX_WIDTH = 2000
MAX_HEIGHT = 2000
coverage_grid = [[0 for col_idx in range(MAX_WIDTH)] for row_idx in range(MAX_HEIGHT)]

for _ in range(2):
    rect_x, rect_y, rect_width, rect_height = map(int, input().split())
    for x_idx in range(rect_x, rect_x + rect_width):
        for y_idx in range(rect_y, rect_y + rect_height):
            coverage_grid[y_idx][x_idx] += 1

single_coverage_count = 0
for row_idx in range(MAX_HEIGHT):
    for col_idx in range(MAX_WIDTH):
        if coverage_grid[row_idx][col_idx] == 1:
            single_coverage_count += 1

print(single_coverage_count)