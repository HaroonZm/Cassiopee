number_of_elements, extra_parameter = map(int, input().split())

sequence_of_numbers = list(map(int, input().split()))

current_min_value = sequence_of_numbers[0]

maximum_difference = 0

number_of_maximum_differences = 0

for index in range(1, number_of_elements):

    current_min_value = min(current_min_value, sequence_of_numbers[index - 1])

    difference_with_min = sequence_of_numbers[index] - current_min_value

    if maximum_difference < difference_with_min:

        maximum_difference = difference_with_min

        number_of_maximum_differences = 1

    elif maximum_difference == difference_with_min:

        number_of_maximum_differences += 1

print(number_of_maximum_differences)