first_input_string = input()
second_input_string = input()

number_of_rows = len(second_input_string)
number_of_columns = len(first_input_string)

subsequence_count_table = [
    [0 for column_index in range(number_of_columns)]
    for row_index in range(number_of_rows)
]

if len(first_input_string) > len(second_input_string):

    if first_input_string[0] == second_input_string[0]:
        subsequence_count_table[0][0] = 1

    for column_index in range(1, number_of_columns):
        if first_input_string[column_index] == second_input_string[0]:
            subsequence_count_table[0][column_index] = (
                subsequence_count_table[0][column_index - 1] + 1
            )
        else:
            subsequence_count_table[0][column_index] = subsequence_count_table[0][column_index - 1]

    for row_index in range(1, number_of_rows):

        if second_input_string[row_index] == first_input_string[row_index]:
            subsequence_count_table[row_index][row_index] = subsequence_count_table[row_index - 1][row_index - 1]

        for column_index in range(row_index + 1, number_of_columns):
            if second_input_string[row_index] == first_input_string[column_index]:
                subsequence_count_table[row_index][column_index] = (
                    subsequence_count_table[row_index - 1][column_index - 1] +
                    subsequence_count_table[row_index][column_index - 1]
                )
            else:
                subsequence_count_table[row_index][column_index] = subsequence_count_table[row_index][column_index - 1]

    print(subsequence_count_table[number_of_rows - 1][number_of_columns - 1] % 1000000007)

elif len(first_input_string) == len(second_input_string):
    if first_input_string == second_input_string:
        print(1)
    else:
        print(0)

else:
    print(0)