number_of_rows, number_of_columns = map(int, input().split())

first_matrix_rows = [input() for _ in range(number_of_rows)]

second_matrix_rows = [input() for _ in range(number_of_rows)]

difference_count = 0

for first_row, second_row in zip(first_matrix_rows, second_matrix_rows):

    for first_element, second_element in zip(first_row, second_row):

        if first_element != second_element:

            difference_count += 1

print(difference_count)