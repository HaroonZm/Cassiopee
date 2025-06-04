while True:

    input_height, input_width = map(int, input().split())

    if input_height == 0 and input_width == 0:
        break

    for current_row_index in range(input_height):

        for current_column_index in range(input_width):

            is_border_row = current_row_index == 0 or current_row_index == input_height - 1
            is_border_column = current_column_index == 0 or current_column_index == input_width - 1

            if is_border_row or is_border_column:
                print('#', end="")
            else:
                print('.', end="")

        print('')

    print('')