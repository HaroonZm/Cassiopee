user_inputs_as_strings = input().split()

user_inputs_as_integers = list(map(int, user_inputs_as_strings))

first_input_value = user_inputs_as_integers[0]
second_input_value = user_inputs_as_integers[1]
third_input_value = user_inputs_as_integers[2]

if first_input_value == second_input_value == third_input_value:
    
    print(1)

elif (
    first_input_value != second_input_value
    and first_input_value != third_input_value
    and second_input_value != third_input_value
):
    
    print(3)

else:
    
    print(2)