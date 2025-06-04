number_of_iterations = int(input())

for iteration_index in range(number_of_iterations):

    largest_number_string = ""
    smallest_number_string = ""

    input_number_string = str(input())
    digit_list = list(map(str, input_number_string))

    smallest_digit_list_sorted = sorted(digit_list)
    largest_digit_list_sorted = sorted(digit_list, reverse=True)

    for digit_position in range(8):
        largest_number_string = largest_number_string + largest_digit_list_sorted[digit_position]
        smallest_number_string = smallest_number_string + smallest_digit_list_sorted[digit_position]

    difference_between_largest_and_smallest = int(largest_number_string) - int(smallest_number_string)

    print(difference_between_largest_and_smallest)