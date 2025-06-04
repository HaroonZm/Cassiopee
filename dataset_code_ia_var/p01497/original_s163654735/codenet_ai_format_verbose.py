from functools import reduce
import operator

def solve():
    number_of_rows = 4
    number_of_columns = 5  # Not actually used, kept for context

    initial_grid = [list(map(int, input().split())) for _ in range(number_of_rows)]

    memoization_dict = { (0,) * (number_of_rows ** 2): 0 }

    direction_vectors = ((-1, 0), (0, -1), (1, 0), (0, 1))

    unreachable_value = 10

    def minimum_moves(remaining_moves, current_grid_state):
        flattened_state = reduce(operator.add, map(tuple, current_grid_state))
        if flattened_state in memoization_dict:
            return memoization_dict[flattened_state]

        if remaining_moves == 0:
            return unreachable_value

        minimal_steps = unreachable_value

        for row_index in range(number_of_rows):
            for column_index in range(number_of_rows):
                current_cell_value = current_grid_state[row_index][column_index]

                grid_copy = [row[:] for row in current_grid_state]

                if grid_copy[row_index][column_index] < 4:
                    grid_copy[row_index][column_index] += 1
                    minimal_steps = min(minimal_steps, minimum_moves(remaining_moves - 1, grid_copy) + 1)
                    continue

                grid_copy[row_index][column_index] = 0

                cell_stack = [ (column_index, row_index, direction_index) for direction_index in range(4) ]
                increment_count = 1

                while cell_stack:
                    next_stack = []

                    for x_pos, y_pos, direction in cell_stack:
                        dx, dy = direction_vectors[direction]
                        next_x = x_pos + dx
                        next_y = y_pos + dy

                        if not (0 <= next_x < number_of_rows and 0 <= next_y < number_of_rows):
                            continue

                        if grid_copy[next_y][next_x]:
                            grid_copy[next_y][next_x] += 1
                        else:
                            next_stack.append((next_x, next_y, direction))

                    for search_row in range(number_of_rows):
                        for search_col in range(number_of_rows):
                            if grid_copy[search_row][search_col] >= 5:
                                grid_copy[search_row][search_col] = 0
                                increment_count += 1
                                next_stack.extend( (search_col, search_row, dir_idx) for dir_idx in range(4) )

                    cell_stack = next_stack

                minimal_steps = min(minimal_steps, minimum_moves(remaining_moves - 1, grid_copy) + 1)

        memoization_dict[flattened_state] = minimal_steps
        return minimal_steps

    result = minimum_moves(5, initial_grid)

    if result < unreachable_value:
        print(result)
    else:
        print(-1)

solve()