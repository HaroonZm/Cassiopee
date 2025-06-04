while True:
    input_height, input_width = map(int, raw_input().split())
    if input_height == 0 and input_width == 0:
        break
    grid_data = [list(raw_input()) for grid_row_index in range(input_height)]
    cursor_x, cursor_y = 0, 0
    while True:
        current_tile = grid_data[cursor_y][cursor_x]
        grid_data[cursor_y][cursor_x] = '*'
        if current_tile == '>':
            cursor_x += 1
        elif current_tile == '<':
            cursor_x -= 1
        elif current_tile == 'v':
            cursor_y += 1
        elif current_tile == '^':
            cursor_y -= 1
        elif current_tile == '.':
            print cursor_x, cursor_y
            break
        else:
            print 'LOOP'
            break