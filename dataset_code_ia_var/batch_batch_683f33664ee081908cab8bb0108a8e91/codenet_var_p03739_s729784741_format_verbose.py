import sys
from itertools import accumulate

read_entire_input = sys.stdin.read
read_line = sys.stdin.readline
read_all_lines = sys.stdin.readlines

sys.setrecursionlimit(10 ** 9)

INFINITY = 1 << 60
MODULO = 1000000007

def calculate_minimum_operations(array_of_integers):
    minimum_operations_required = 0
    cumulative_sum = array_of_integers[0]

    for next_integer in array_of_integers[1:]:
        previous_sum = cumulative_sum
        cumulative_sum = cumulative_sum + next_integer

        if previous_sum > 0 and cumulative_sum >= 0:
            minimum_operations_required += cumulative_sum + 1
            cumulative_sum = -1

        if previous_sum < 0 and cumulative_sum <= 0:
            minimum_operations_required += -cumulative_sum + 1
            cumulative_sum = 1

    return minimum_operations_required

def main():
    input_numbers = list(map(int, read_entire_input().split()))
    total_number_of_elements = input_numbers[0]
    array_elements = input_numbers[1:]

    original_first_element = array_elements[0]

    minimum_operations_starting_positive = 0

    if array_elements[0] <= 0:
        minimum_operations_starting_positive = -array_elements[0] + 1
        array_elements[0] = 1

    minimum_operations_starting_positive += calculate_minimum_operations(array_elements)

    array_elements[0] = original_first_element

    minimum_operations_starting_negative = 0

    if array_elements[0] >= 0:
        minimum_operations_starting_negative = array_elements[0] + 1
        array_elements[0] = -1

    minimum_operations_starting_negative += calculate_minimum_operations(array_elements)

    smallest_operation_count = min(
        minimum_operations_starting_positive,
        minimum_operations_starting_negative
    )

    print(smallest_operation_count)

    return

if __name__ == '__main__':
    main()