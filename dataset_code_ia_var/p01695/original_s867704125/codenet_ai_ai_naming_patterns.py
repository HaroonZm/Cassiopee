def count_leading_dot(sequence):
    dot_count = 0
    for element in sequence:
        if element != '.':
            return dot_count
        dot_count += 1
    return dot_count

def process_grid(row_count):
    grid_rows = []
    leading_dot_counts = []
    for row_index in range(row_count):
        current_row = [character for character in input()]
        grid_rows.append(current_row)
        leading_dot_counts.append(count_leading_dot(current_row))

    for row_index in range(row_count):
        for col_index in range(len(grid_rows[row_index])):
            if grid_rows[row_index][col_index] == '.':
                grid_rows[row_index][col_index] = ' '

    for row_index in range(1, row_count):
        insert_col_index = leading_dot_counts[row_index] - 1
        grid_rows[row_index][insert_col_index] = '+'
        step = 1
        while True:
            prev_row_index = row_index - step
            if grid_rows[prev_row_index][insert_col_index] == ' ':
                grid_rows[prev_row_index][insert_col_index] = '|'
                step += 1
            else:
                break

    for row_index in range(row_count):
        for character in grid_rows[row_index]:
            print(character, end='')
        print()

while True:
    num_rows = int(input())
    if num_rows == 0:
        break
    process_grid(num_rows)