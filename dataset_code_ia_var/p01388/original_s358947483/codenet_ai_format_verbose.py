user_input_string = input()

count_K = user_input_string.count('K')
count_U = user_input_string.count('U')
count_P = user_input_string.count('P')
count_C = user_input_string.count('C')

list_of_letter_counts = [count_K, count_U, count_P, count_C]

minimum_letter_count = min(list_of_letter_counts)

print(minimum_letter_count)