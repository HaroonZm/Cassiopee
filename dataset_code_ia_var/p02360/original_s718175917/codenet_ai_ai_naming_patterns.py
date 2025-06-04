import sys
input_stream = sys.stdin.readline

num_rectangles = int(input_stream())

grid_size = 1001
coverage_grid = [[0 for col_idx in range(grid_size)] for row_idx in range(grid_size)]

for rect_idx in range(num_rectangles):
    rect_x1, rect_y1, rect_x2, rect_y2 = map(int, input_stream().split())
    coverage_grid[rect_x1][rect_y1] += 1
    coverage_grid[rect_x2][rect_y2] += 1
    coverage_grid[rect_x2][rect_y1] -= 1
    coverage_grid[rect_x1][rect_y2] -= 1

for row_idx in range(grid_size):
    for col_idx in range(grid_size - 1):
        coverage_grid[row_idx][col_idx + 1] += coverage_grid[row_idx][col_idx]

for col_idx in range(grid_size):
    for row_idx in range(grid_size - 1):
        coverage_grid[row_idx + 1][col_idx] += coverage_grid[row_idx][col_idx]

max_coverage = 0

for row_idx in range(grid_size):
    max_coverage = max(max_coverage, max(coverage_grid[row_idx]))

print(max_coverage)