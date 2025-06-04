matrix_of_integers = [list(map(int, input().split())) for row_index in range(3)]

total_sum_of_all_elements = 0
sum_of_main_diagonal_elements_times_three = 0

for row_index in range(3):

    total_sum_of_all_elements += sum(matrix_of_integers[row_index])

    sum_of_main_diagonal_elements_times_three += matrix_of_integers[row_index][row_index] * 3

if total_sum_of_all_elements == sum_of_main_diagonal_elements_times_three:

    print('Yes')

else:

    print('No')