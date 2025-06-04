import itertools

input_rectangle_count = int(input())
grid_size = 1001
grid = [[0] * grid_size for _ in range(grid_size)]

for rectangle in (map(int, input().split()) for _ in range(input_rectangle_count)):
    x_start, y_start, x_end, y_end = rectangle
    grid[x_start][y_start] += 1
    grid[x_start][y_end] -= 1
    grid[x_end][y_start] -= 1
    grid[x_end][y_end] += 1

row_prefix_sums = [list(itertools.accumulate(row)) for row in grid]
column_prefix_sums = [list(itertools.accumulate(column)) for column in zip(*row_prefix_sums)]
maximum_overlap = max(max(row) for row in column_prefix_sums)
print(maximum_overlap)