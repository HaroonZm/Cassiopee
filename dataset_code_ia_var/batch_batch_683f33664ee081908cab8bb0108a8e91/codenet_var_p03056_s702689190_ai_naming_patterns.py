num_rows, num_cols = map(int, input().split())
cell_values = [[1 if cell_char == "#" else 0 for cell_char in input()] for _ in range(num_rows)]
x_transition = [[[-2] * (num_rows + 2) for _ in range(num_cols + 2)] for _ in range(num_rows + 2)]
y_transition = [[[-2] * (num_cols + 2) for _ in range(num_cols + 2)] for _ in range(num_rows + 2)]

for row_idx in range(num_rows):
    for col_idx in range(num_cols):
        x_transition[row_idx][col_idx][row_idx] = col_idx
        y_transition[row_idx][col_idx][col_idx] = row_idx
for row_idx in range(num_rows):
    for col_idx in range(num_cols-1)[::-1]:
        if cell_values[row_idx][col_idx] == cell_values[row_idx][col_idx+1]:
            x_transition[row_idx][col_idx][row_idx] = x_transition[row_idx][col_idx+1][row_idx]
for row_idx in range(num_rows-1)[::-1]:
    for col_idx in range(num_cols):
        if cell_values[row_idx][col_idx] == cell_values[row_idx+1][col_idx]:
            y_transition[row_idx][col_idx][col_idx] = y_transition[row_idx+1][col_idx][col_idx]

for row_idx in range(num_rows):
    for col_idx in range(num_cols):
        for bottom_row in range(row_idx+1, num_rows):
            if cell_values[bottom_row][col_idx] != cell_values[row_idx][col_idx]:
                break
            x_transition[row_idx][col_idx][bottom_row] = min(x_transition[row_idx][col_idx][bottom_row-1], x_transition[bottom_row][col_idx][bottom_row])
for row_idx in range(num_rows):
    for col_idx in range(num_cols):
        for right_col in range(col_idx+1, num_cols):
            if cell_values[row_idx][right_col] != cell_values[row_idx][col_idx]:
                break
            y_transition[row_idx][col_idx][right_col] = min(y_transition[row_idx][col_idx][right_col-1], y_transition[row_idx][right_col][right_col])

for step_idx in range(16):
    if x_transition[0][0][num_rows-1] == num_cols-1:
        print(step_idx)
        break
    elif step_idx == 15:
        print(16)
        break
    for row_idx in range(num_rows):
        row_x_transition = x_transition[row_idx]
        row_y_transition = y_transition[row_idx]
        for col_idx in range(num_cols):
            col_x_transition = row_x_transition[col_idx]
            col_y_transition = row_y_transition[col_idx]
            for bottom_row in range(row_idx, num_rows):
                current_x = col_x_transition[bottom_row]
                if current_x >= 0 and x_transition[row_idx][current_x + 1][bottom_row] >= 0:
                    col_x_transition[bottom_row] = x_transition[row_idx][current_x + 1][bottom_row]
            for right_col in range(col_idx, num_cols):
                current_y = col_y_transition[right_col]
                if current_y >= 0 and y_transition[current_y + 1][col_idx][right_col] >= 0:
                    col_y_transition[right_col] = y_transition[current_y + 1][col_idx][right_col]
            
            max_right_col = num_cols - 1
            for bottom_row in range(row_idx, num_rows):
                while max_right_col >= col_idx and col_y_transition[max_right_col] < bottom_row:
                    max_right_col -= 1
                if max_right_col >= col_idx:
                    col_x_transition[bottom_row] = max(col_x_transition[bottom_row], max_right_col)
            
            max_bottom_row = num_rows - 1
            for right_col in range(col_idx, num_cols):
                while max_bottom_row >= row_idx and col_x_transition[max_bottom_row] < right_col:
                    max_bottom_row -= 1
                if max_bottom_row >= row_idx:
                    col_y_transition[right_col] = max(col_y_transition[right_col], max_bottom_row)