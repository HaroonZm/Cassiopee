#!/opt/local/bin/python

while True:

    user_input_numbers = map(int, raw_input().split())
    number_of_rows = user_input_numbers[0]
    number_of_columns = user_input_numbers[1]

    if number_of_rows == 0 and number_of_columns == 0:
        break

    for current_row_index in range(number_of_rows):

        print "#" * number_of_columns

    else:

        print