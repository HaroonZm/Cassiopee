user_input = input()

first_number_str, second_number_str = user_input.split(" ")

first_number_int = int(first_number_str)
second_number_int = int(second_number_str)

is_first_number_contains_zero = "0" in first_number_str
is_second_number_contains_zero = "0" in second_number_str
is_first_number_greater_than_nine = first_number_int > 9
is_second_number_greater_than_nine = second_number_int > 9

if (
    is_first_number_contains_zero or
    is_second_number_contains_zero or
    is_first_number_greater_than_nine or
    is_second_number_greater_than_nine
):
    print(-1)
else:
    print(first_number_int * second_number_int)