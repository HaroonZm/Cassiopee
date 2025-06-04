while True:
    line_count = int(input())
    if line_count == 0:
        break
    grid_lines = [list(input()) for _ in range(line_count)]
    for row_index in range(line_count):
        for col_index in range(len(grid_lines[row_index])):
            current_cell = grid_lines[row_index][col_index]
            if current_cell == '.':
                grid_lines[row_index][col_index] = ' '
            else:
                if col_index > 0:
                    grid_lines[row_index][col_index - 1] = '+'
                    up_index = row_index - 1
                    while up_index >= 0 and grid_lines[up_index][col_index - 1] == ' ':
                        grid_lines[up_index][col_index - 1] = '|'
                        up_index -= 1
                break
    for output_row in grid_lines:
        print(''.join(output_row))