user_input_numbers_as_strings = input().split()

user_input_numbers_as_integers = list(map(int, user_input_numbers_as_strings))

sorted_numbers_in_ascending_order = sorted(user_input_numbers_as_integers)

all_but_largest_numbers = sorted_numbers_in_ascending_order[:-1]

sum_of_all_but_largest_numbers = sum(all_but_largest_numbers)

print(sum_of_all_but_largest_numbers)