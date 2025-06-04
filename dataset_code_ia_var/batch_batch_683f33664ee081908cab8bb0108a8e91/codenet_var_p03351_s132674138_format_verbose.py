first_number, second_number, third_number, maximum_allowed_difference = map(int, input().split())

difference_first_second = abs(first_number - second_number)
difference_second_third = abs(second_number - third_number)
difference_first_third = abs(first_number - third_number)

is_first_to_second_valid = difference_first_second <= maximum_allowed_difference
is_second_to_third_valid = difference_second_third <= maximum_allowed_difference
is_first_to_third_valid = difference_first_third <= maximum_allowed_difference

if (is_first_to_second_valid and is_second_to_third_valid) or is_first_to_third_valid:
    print("Yes")
else:
    print("No")