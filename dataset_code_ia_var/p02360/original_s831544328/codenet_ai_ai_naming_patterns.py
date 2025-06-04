import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
read_input = sys.stdin.buffer.readline

rectangle_count = int(read_input())
size_limit = 1002

field_grid = [[0] * size_limit for _ in range(size_limit)]

for _ in range(rectangle_count):
    left_x, top_y, right_x, bottom_y = map(int, read_input().split())
    field_grid[left_x][top_y] += 1
    field_grid[left_x][bottom_y] -= 1
    field_grid[right_x][top_y] -= 1
    field_grid[right_x][bottom_y] += 1

for row_index in range(size_limit):
    field_grid[row_index] = list(accumulate(field_grid[row_index]))

for row_index in range(size_limit - 1):
    for col_index in range(size_limit):
        field_grid[row_index + 1][col_index] += field_grid[row_index][col_index]

max_overlap = 0
for row in field_grid:
    max_overlap = max(max_overlap, max(row))

print(max_overlap)