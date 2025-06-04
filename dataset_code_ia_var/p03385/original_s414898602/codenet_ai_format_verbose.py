user_input_string = input()

count_a_in_input = user_input_string.count('a')
count_b_in_input = user_input_string.count('b')
count_c_in_input = user_input_string.count('c')

if count_a_in_input == 1 and count_b_in_input == 1 and count_c_in_input == 1:
    print('Yes')
else:
    print('No')