from collections import deque
import itertools as itertools_module
import sys

sys.setrecursionlimit(1000000)

while True:
    number_of_rows, candidate_value = map(int, raw_input().split())

    if number_of_rows == 0:
        break

    triangle_grid = []

    for row_index in range(number_of_rows):
        row_values = map(int, raw_input().split())
        triangle_grid.append(row_values)

    visited_positions = {}

    def flood_fill(column, row, target_value):
        if column < 0 or column > row or row >= number_of_rows:
            return []

        if (column, row) in visited_positions:
            return []

        visited_positions[(column, row)] = True

        if triangle_grid[row][column] == 0:
            return [(column, row)]

        if triangle_grid[row][column] != target_value:
            return []

        connected_positions = []

        neighbor_offsets = [
            [column - 1, row],
            [column + 1, row],
            [column - 1, row - 1],
            [column, row - 1],
            [column, row + 1],
            [column + 1, row + 1]
        ]

        for neighbor in neighbor_offsets:
            neighbor_with_value = neighbor + [target_value]
            result = flood_fill(*neighbor_with_value)
            if result:
                connected_positions += result

        return connected_positions

    highest_score = -10000

    for current_row in range(number_of_rows):
        for current_column in range(current_row + 1):
            if triangle_grid[current_row][current_column] == 0:

                original_value = triangle_grid[current_row][current_column]
                triangle_grid[current_row][current_column] = candidate_value

                orphaned_numbers = []

                for row_iter in range(number_of_rows):
                    for column_iter in range(row_iter + 1):
                        if triangle_grid[row_iter][column_iter] != 0:
                            visited_positions = {}
                            if len(flood_fill(column_iter, row_iter, triangle_grid[row_iter][column_iter])) == 0:
                                orphaned_numbers.append(triangle_grid[row_iter][column_iter])

                triangle_grid[current_row][current_column] = original_value

                current_score = 0
                for orphaned_value in orphaned_numbers:
                    if orphaned_value == candidate_value:
                        current_score -= 1
                    else:
                        current_score += 1

                highest_score = max(highest_score, current_score)

    print highest_score