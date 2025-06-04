def get_leading_dot_count(row_list):
    leading_dot_count = 0
    for char in row_list:
        if char != '.':
            return leading_dot_count
        leading_dot_count += 1

def process_grid(num_rows):
    grid_rows = []
    leading_dots_per_row = []
    for row_index in range(num_rows):
        row_chars = [ch for ch in input()]
        grid_rows.append(row_chars)
        leading_dots_per_row.append(get_leading_dot_count(row_chars))
    for row_index in range(num_rows):
        for col_index in range(len(grid_rows[row_index])):
            if grid_rows[row_index][col_index] == '.':
                grid_rows[row_index][col_index] = ' '
    for row_index in range(1, num_rows):
        grid_rows[row_index][leading_dots_per_row[row_index] - 1] = '+'
        vertical_offset = 1
        while True:
            prev_row = row_index - vertical_offset
            col_for_pipe = leading_dots_per_row[row_index] - 1
            if grid_rows[prev_row][col_for_pipe] == ' ':
                grid_rows[prev_row][col_for_pipe] = '|'
                vertical_offset += 1
            else:
                break
    for row_index in range(num_rows):
        for char in grid_rows[row_index]:
            print(char, end='')
        print()

while True:
    input_row_count = int(input())
    if input_row_count == 0:
        break
    process_grid(input_row_count)