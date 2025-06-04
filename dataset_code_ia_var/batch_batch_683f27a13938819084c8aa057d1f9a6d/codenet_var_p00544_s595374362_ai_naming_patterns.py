def calculate_repaint_count(row_string, target_color):
    return len(row_string) - row_string.count(target_color)

num_rows, num_columns = map(int, input().split())
middle_rows = []
initial_repaint_count = 0
for row_index in range(num_rows):
    current_row = input().strip()
    if row_index == 0:
        initial_repaint_count += calculate_repaint_count(current_row, 'W')
    elif row_index == num_rows - 1:
        initial_repaint_count += calculate_repaint_count(current_row, 'R')
    else:
        middle_rows.append(current_row)

row_color_combinations = []
for white_row_count in range(0, num_rows - 1):
    for blue_row_count in range(1, num_rows - white_row_count):
        red_row_count = num_rows - 2 - white_row_count - blue_row_count
        if red_row_count >= 0:
            row_color_combinations.append([white_row_count, blue_row_count, red_row_count])

minimum_total_repaint = 2500
current_combination_repaint = 0
for combination in row_color_combinations:
    for middle_row_index in range(len(middle_rows)):
        if middle_row_index < combination[0]:
            current_combination_repaint += calculate_repaint_count(middle_rows[middle_row_index], 'W')
        elif combination[0] <= middle_row_index < (combination[0] + combination[1]):
            current_combination_repaint += calculate_repaint_count(middle_rows[middle_row_index], 'B')
        elif (combination[0] + combination[1]) <= middle_row_index < (combination[0] + combination[1] + combination[2]):
            current_combination_repaint += calculate_repaint_count(middle_rows[middle_row_index], 'R')
    if current_combination_repaint < minimum_total_repaint:
        minimum_total_repaint = current_combination_repaint
    current_combination_repaint = 0

print(initial_repaint_count + minimum_total_repaint)