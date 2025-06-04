user_input_string = input()

is_length_three = len(user_input_string) == 3
contains_a = 'a' in user_input_string
contains_b = 'b' in user_input_string
contains_c = 'c' in user_input_string

if is_length_three and contains_a and contains_b and contains_c:
    print('Yes')
else:
    print('No')