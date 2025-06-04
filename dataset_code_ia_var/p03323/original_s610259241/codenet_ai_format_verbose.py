first_input_number, second_input_number = map(int, input().split())

maximum_allowed_value = 8

if first_input_number <= maximum_allowed_value and second_input_number <= maximum_allowed_value:
    print('Yay!')
else:
    print(':(')