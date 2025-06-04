matrix_rows = [
    [int(cell_value) for cell_value in input().split()]
    for current_row_index in range(3)
]

set_of_first_minus_second = {row[0] - row[1] for row in matrix_rows}
set_of_first_minus_third = {row[0] - row[2] for row in matrix_rows}

has_same_difference_between_first_and_second = len(set_of_first_minus_second) == 1
has_same_difference_between_first_and_third = len(set_of_first_minus_third) == 1

if has_same_difference_between_first_and_second and has_same_difference_between_first_and_third:
    print('Yes')
else:
    print('No')