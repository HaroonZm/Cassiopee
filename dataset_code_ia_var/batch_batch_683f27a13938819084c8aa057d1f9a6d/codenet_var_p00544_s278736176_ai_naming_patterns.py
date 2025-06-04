row_count, col_count = map(int, input().split())

matrix_flag = []
for row_index in range(row_count):
    input_row = list(input())
    matrix_flag.append(input_row)

min_change_count = 10**9
for white_row_count in range(1, row_count-1):
    for blue_row_count in range(1, row_count-1):
        red_row_count = row_count - white_row_count - blue_row_count
        if red_row_count <= 0:
            continue

        modification_count = 0

        # Count changes for white rows
        for white_row_index in range(white_row_count):
            for col_index in range(col_count):
                if matrix_flag[white_row_index][col_index] != "W":
                    modification_count += 1

        # Count changes for blue rows
        for blue_row_index in range(blue_row_count):
            for col_index in range(col_count):
                if matrix_flag[white_row_count + blue_row_index][col_index] != "B":
                    modification_count += 1

        # Count changes for red rows
        for red_row_index in range(red_row_count):
            for col_index in range(col_count):
                if matrix_flag[white_row_count + blue_row_count + red_row_index][col_index] != "R":
                    modification_count += 1

        if min_change_count > modification_count:
            min_change_count = modification_count

print(min_change_count)