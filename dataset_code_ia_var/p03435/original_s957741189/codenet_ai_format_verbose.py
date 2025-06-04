first_row_of_matrix = list(map(int, input().split()))
second_row_of_matrix = list(map(int, input().split()))
third_row_of_matrix = list(map(int, input().split()))

is_valid_matrix = 1

minimum_value_in_first_row = min(first_row_of_matrix)

row_difference_vector = [
    first_row_of_matrix[0] - minimum_value_in_first_row,
    first_row_of_matrix[1] - minimum_value_in_first_row,
    first_row_of_matrix[2] - minimum_value_in_first_row
]

second_row_diff_0 = second_row_of_matrix[0] - row_difference_vector[0]
second_row_diff_1 = second_row_of_matrix[1] - row_difference_vector[1]
second_row_diff_2 = second_row_of_matrix[2] - row_difference_vector[2]

if not (second_row_diff_0 == second_row_diff_1 == second_row_diff_2):
    is_valid_matrix = 0

third_row_diff_0 = third_row_of_matrix[0] - row_difference_vector[0]
third_row_diff_1 = third_row_of_matrix[1] - row_difference_vector[1]
third_row_diff_2 = third_row_of_matrix[2] - row_difference_vector[2]

if not (third_row_diff_0 == third_row_diff_1 == third_row_diff_2):
    is_valid_matrix = 0

result_texts = ["No", "Yes"]

print(result_texts[is_valid_matrix])