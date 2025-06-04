user_input_string = input()

count_letter_K = user_input_string.count('K')
count_letter_U = user_input_string.count('U')
count_letter_P = user_input_string.count('P')
count_letter_C = user_input_string.count('C')

letter_counts_list = [count_letter_K, count_letter_U, count_letter_P, count_letter_C]

minimum_letter_count = min(letter_counts_list)

print(minimum_letter_count)