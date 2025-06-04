import sys

standard_input = sys.stdin.readline

read_string = lambda: standard_input().strip()
read_integer = lambda: int(standard_input())
read_integer_list = lambda: list(map(int, standard_input().split()))

modulo = 10 ** 9 + 7

grid_height, grid_width = read_integer_list()
grid = []

for row_index in range(grid_height):
    row_string = read_string()
    grid.append(row_string)

import collections

def get_longest_path_from(start_row, start_column):
    visited_positions = {}
    breadth_first_queue = collections.deque()
    breadth_first_queue.append((start_row, start_column, 0))
    current_maximum_distance = 0

    while breadth_first_queue:
        current_row, current_column, current_distance = breadth_first_queue.popleft()
        if (current_row, current_column) in visited_positions:
            continue

        current_maximum_distance = max(current_maximum_distance, current_distance)
        visited_positions[(current_row, current_column)] = True

        for row_delta, column_delta in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_row = current_row + row_delta
            next_column = current_column + column_delta

            if (
                0 <= next_row < grid_height and
                0 <= next_column < grid_width and
                grid[next_row][next_column] != '#'
            ):
                breadth_first_queue.append((next_row, next_column, current_distance + 1))

    return current_maximum_distance

maximum_path_length = 0

for row_index in range(grid_height):
    for column_index in range(grid_width):
        if grid[row_index][column_index] == '#':
            continue
        longest_path = get_longest_path_from(row_index, column_index)
        maximum_path_length = max(maximum_path_length, longest_path)

print(maximum_path_length)