input_numbers_as_strings = input().split()
input_numbers_as_integers = list(map(int, input_numbers_as_strings))

input_numbers_as_integers.sort()

total_consecutive_differences = 0

for current_index in range(len(input_numbers_as_integers) - 1):
    next_number = input_numbers_as_integers[current_index + 1]
    current_number = input_numbers_as_integers[current_index]
    difference_between_consecutive_numbers = next_number - current_number
    total_consecutive_differences += difference_between_consecutive_numbers

print(total_consecutive_differences)