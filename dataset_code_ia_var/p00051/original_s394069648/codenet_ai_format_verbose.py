import sys

input_stream_readline = sys.stdin.readline
output_stream_write = sys.stdout.write

def compute_max_difference_between_permutations():
    input_number_as_string = input_stream_readline().strip()

    digits_sorted_descending = "".join(sorted(input_number_as_string, reverse=True))
    digits_sorted_ascending = "".join(sorted(input_number_as_string))

    integer_descending = int(digits_sorted_descending)
    integer_ascending = int(digits_sorted_ascending)

    difference_between_permutations = integer_descending - integer_ascending

    output_stream_write(f"{difference_between_permutations}\n")

number_of_test_cases = int(input_stream_readline())

for test_case_index in range(number_of_test_cases):
    compute_max_difference_between_permutations()