num_rows, num_cols = map(int, input().split())

def get_forward_pos(direction, row, col):
    if direction == 0 and 0 <= row - 1 < num_rows + 2 and 0 <= col < num_cols + 2:
        return (row - 1, col)
    elif direction == 1 and 0 <= row < num_rows + 2 and 0 <= col + 1 < num_cols + 2:
        return (row, col + 1)
    elif direction == 2 and 0 <= row + 1 < num_rows + 2 and 0 <= col < num_cols + 2:
        return (row + 1, col)
    elif direction == 3 and 0 <= row < num_rows + 2 and 0 <= col - 1 < num_cols + 2:
        return (row, col - 1)
    else:
        return (-1, -1)

def get_forward_diagonal_pos(direction, row, col):
    if direction == 0 and 0 <= row - 1 < num_rows + 2 and 0 <= col + 1 < num_cols + 2:
        return (row - 1, col + 1)
    elif direction == 1 and 0 <= row + 1 < num_rows + 2 and 0 <= col + 1 < num_cols + 2:
        return (row + 1, col + 1)
    elif direction == 2 and 0 <= row + 1 < num_rows + 2 and 0 <= col - 1 < num_cols + 2:
        return (row + 1, col - 1)
    elif direction == 3 and 0 <= row - 1 < num_rows + 2 and 0 <= col - 1 < num_cols + 2:
        return (row - 1, col - 1)
    else:
        return (-1, -1)

def get_right_pos(direction, row, col):
    if direction == 0 and 0 <= row < num_rows + 2 and 0 <= col + 1 < num_cols + 2:
        return (row, col + 1)
    elif direction == 1 and 0 <= row + 1 < num_rows + 2 and 0 <= col < num_cols + 2:
        return (row + 1, col)
    elif direction == 2 and 0 <= row < num_rows + 2 and 0 <= col - 1 < num_cols + 2:
        return (row, col - 1)
    elif direction == 3 and 0 <= row - 1 < num_rows + 2 and 0 <= col < num_cols + 2:
        return (row - 1, col)
    else:
        return (-1, -1)

def get_right_diagonal_pos(direction, row, col):
    if direction == 0 and 0 <= row + 1 < num_rows + 2 and 0 <= col + 1 < num_cols + 2:
        return (row + 1, col + 1)
    elif direction == 1 and 0 <= row + 1 < num_rows + 2 and 0 <= col - 1 < num_cols + 2:
        return (row + 1, col - 1)
    elif direction == 2 and 0 <= row - 1 < num_rows + 2 and 0 <= col - 1 < num_cols + 2:
        return (row - 1, col - 1)
    elif direction == 3 and 0 <= row - 1 < num_rows + 2 and 0 <= col + 1 < num_cols + 2:
        return (row - 1, col + 1)
    else:
        return (-1, -1)

visited_cells = [[False for _ in range(num_cols + 2)] for _ in range(num_rows + 2)]
grid = [['#'] + list(input()) + ['#'] for _ in range(num_rows)]
grid.insert(0, ['#' for _ in range(num_cols + 2)])
grid.append(['#' for _ in range(num_cols + 2)])

start_pos = (-1, -1)
direction_map = {'^': 0, '>': 1, 'v': 2, '<': 3}
entry_obstacle = (-1, -1)

for row_idx in range(num_rows + 2):
    for col_idx in range(num_cols + 2):
        if grid[row_idx][col_idx] in direction_map:
            current_direction = direction_map[grid[row_idx][col_idx]]
            start_pos = (row_idx, col_idx)
            forward_row, forward_col = get_forward_pos(current_direction, row_idx, col_idx)
            if (forward_row, forward_col) != (-1, -1) and grid[forward_row][forward_col] == '#':
                entry_obstacle = (forward_row, forward_col)
                break
            forward_diag_row, forward_diag_col = get_forward_diagonal_pos(current_direction, row_idx, col_idx)
            if (forward_diag_row, forward_diag_col) != (-1, -1) and grid[forward_diag_row][forward_diag_col] == '#':
                entry_obstacle = (forward_diag_row, forward_diag_col)
                break
            right_row, right_col = get_right_pos(current_direction, row_idx, col_idx)
            if (right_row, right_col) != (-1, -1) and grid[right_row][right_col] == '#':
                entry_obstacle = (right_row, right_col)
                break
            right_diag_row, right_diag_col = get_right_diagonal_pos(current_direction, row_idx, col_idx)
            if (right_diag_row, right_diag_col) != (-1, -1) and grid[right_diag_row][right_diag_col] == '#':
                entry_obstacle = (right_diag_row, right_diag_col)
                break
    else:
        continue

max_steps = 5242
current_row, current_col = start_pos
steps_counter = 0

while steps_counter < max_steps:
    next_forward_row, next_forward_col = get_forward_pos(current_direction, current_row, current_col)
    visited_cells[current_row][current_col] = True
    if grid[current_row][current_col] == 'G':
        break
    next_right_diag_row, next_right_diag_col = get_right_diagonal_pos(current_direction, current_row, current_col)
    if grid[next_forward_row][next_forward_col] != '#' and entry_obstacle != (next_right_diag_row, next_right_diag_col):
        if entry_obstacle == get_forward_diagonal_pos(current_direction, current_row, current_col) or entry_obstacle == get_right_pos(current_direction, current_row, current_col):
            current_row, current_col = get_forward_pos(current_direction, current_row, current_col)
            steps_counter += 1
            continue
        else:
            right_row, right_col = get_right_pos(current_direction, current_row, current_col)
            if grid[right_row][right_col] == '#':
                entry_obstacle = (right_row, right_col)
            steps_counter += 1
            continue
    if entry_obstacle == (next_right_diag_row, next_right_diag_col):
        right_row, right_col = get_right_pos(current_direction, current_row, current_col)
        if grid[right_row][right_col] != '#':
            current_direction = (current_direction + 1) % 4
        else:
            entry_obstacle = (right_row, right_col)
        steps_counter += 1
        continue
    right_row, right_col = get_right_pos(current_direction, current_row, current_col)
    if entry_obstacle == (right_row, right_col):
        forward_row, forward_col = get_forward_pos(current_direction, current_row, current_col)
        if grid[forward_row][forward_col] == '#':
            entry_obstacle = (forward_row, forward_col)
        steps_counter += 1
        continue
    if entry_obstacle == (next_forward_row, next_forward_col):
        current_direction = (current_direction - 1) % 4
        steps_counter += 1
        continue

if steps_counter == max_steps:
    print(-1)
else:
    visited_count = 0
    for visited_row in visited_cells:
        for visited_cell in visited_row:
            if visited_cell:
                visited_count += 1
    print(visited_count)