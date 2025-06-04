first_input_number, second_input_number = map(int, input().split())

maximum_input_number = max(first_input_number, second_input_number)

threshold_value = 8

if maximum_input_number > threshold_value:
    print(':(')
else:
    print('Yay!')