user_input_numbers_as_strings = input().split()

user_input_numbers_as_integers = list(map(int, user_input_numbers_as_strings))

unique_numbers_set = set(user_input_numbers_as_integers)

unique_numbers_list = list(unique_numbers_set)

count_of_unique_numbers = len(unique_numbers_list)

print(count_of_unique_numbers)