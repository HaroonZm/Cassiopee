input_height, input_width = map(int, input().split())
for row_index in range(input_height):
    row_string = input()
    column_results = []
    for column_index in range(len(row_string)):
        if row_string[column_index] == 'c':
            column_results.append(0)
        elif column_index == 0:
            column_results.append(-1)
        else:
            found_flag = False
            for offset in range(1, column_index + 1):
                if row_string[column_index - offset] == 'c':
                    column_results.append(offset)
                    found_flag = True
                    break
            if not found_flag:
                column_results.append(-1)
    print(' '.join(map(str, column_results)))