for line_input in iter(input, '0 0'):
    width, height = map(int, line_input.split())
    dp_table = [[[1, 0, 1, 0] for _ in range(height)] for _ in range(width)]
    for x in range(1, width):
        for y in range(1, height):
            prev_left_first, prev_left_second = dp_table[x-1][y][0], dp_table[x-1][y][1]
            prev_top_third, prev_top_fourth = dp_table[x][y-1][2], dp_table[x][y-1][3]
            dp_table[x][y] = [prev_top_fourth, prev_left_first + prev_left_second, prev_left_second, prev_top_third + prev_top_fourth]
    final_result = (sum(dp_table[width-2][height-1][:2]) + sum(dp_table[width-1][height-2][2:])) % 100000
    print(final_result)