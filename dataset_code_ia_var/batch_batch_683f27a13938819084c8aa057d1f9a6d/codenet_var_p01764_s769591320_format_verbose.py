from collections import defaultdict
import sys

def calculate_minimal_merge_cost(
    left_index, 
    middle_index, 
    right_index, 
    cumulative_values_matrix, 
    minimal_cost_matrix
):
    left_sum = cumulative_values_matrix[left_index][middle_index]
    right_sum = cumulative_values_matrix[middle_index][right_index]
    temporary_result = minimal_cost_matrix[left_index][middle_index] + minimal_cost_matrix[middle_index][right_index]
    carry_over = 0

    while left_sum or right_sum or carry_over:
        current_left_digit = left_sum % 10
        current_right_digit = right_sum % 10
        temporary_result += current_left_digit * current_right_digit + carry_over

        if temporary_result >= minimal_cost_matrix[left_index][right_index]:
            return minimal_cost_matrix[left_index][right_index]

        carry_over = 1 if current_left_digit + current_right_digit + carry_over >= 10 else 0
        left_sum //= 10
        right_sum //= 10

    return temporary_result

def solve():
    number_of_elements = int(sys.stdin.readline())
    sequence_of_numbers = [int(x) for x in sys.stdin.readline().split()]

    minimal_cost_matrix = [
        [float("inf")] * (number_of_elements + 1) 
        for _ in range(number_of_elements)
    ]

    for prefix_index in range(number_of_elements - 1):
        sequence_of_numbers[prefix_index + 1] += sequence_of_numbers[prefix_index]

    sequence_of_numbers.insert(0, 0)

    cumulative_values_matrix = [
        [0] * (number_of_elements + 1) 
        for _ in range(number_of_elements)
    ]

    for left_index in range(number_of_elements):
        minimal_cost_matrix[left_index][left_index + 1] = 0
        for right_index in range(left_index + 1, number_of_elements + 1):
            cumulative_values_matrix[left_index][right_index] = (
                sequence_of_numbers[right_index] - sequence_of_numbers[left_index]
            )

    for current_length in range(2, number_of_elements + 1):
        for left_index in range(number_of_elements - current_length + 1):
            right_index = left_index + current_length
            for middle_index in range(left_index + 1, right_index):
                minimal_cost_matrix[left_index][right_index] = calculate_minimal_merge_cost(
                    left_index, 
                    middle_index, 
                    right_index, 
                    cumulative_values_matrix, 
                    minimal_cost_matrix
                )

    print(minimal_cost_matrix[0][number_of_elements])

if __name__ == "__main__":
    solve()