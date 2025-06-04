directional_moves = [
    {'F': lambda row, col, step: (row, min(col_count, col + step)), 'B': lambda row, col, step: (row, max(1, col - step))},
    {'F': lambda row, col, step: (min(row_count, row + step), col), 'B': lambda row, col, step: (max(1, row - step), col)},
    {'F': lambda row, col, step: (row, max(1, col - step)), 'B': lambda row, col, step: (row, min(col_count, col + step))},
    {'F': lambda row, col, step: (max(1, row - step), col), 'B': lambda row, col, step: (min(row_count, row + step), col)}
]
direction_rotation = {'R': lambda idx: (idx + 1) % 4, 'L': lambda idx: (idx - 1) % 4}

while True:
    row_count, col_count = map(int, input().split())
    if row_count == 0:
        break
    position_row, position_col = 1, 1
    direction_index = 0
    while True:
        command_str = input()
        command_type = command_str[0]
        if command_type in ('F', 'B'):
            _, amount = command_str.split()
            position_row, position_col = directional_moves[direction_index][command_type](position_row, position_col, int(amount))
        elif command_type in ('R', 'L'):
            direction_index = direction_rotation[command_type](direction_index)
        else:
            print(position_row, position_col)
            break