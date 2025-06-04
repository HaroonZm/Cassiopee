first_input_char_list = list(str(input()))
second_input_char_list = list(str(input()))

are_inputs_circularly_equal = 'No'

for rotation_start_index in range(len(first_input_char_list)):
    
    rotated_first_input = (
        first_input_char_list[rotation_start_index:] +
        first_input_char_list[:rotation_start_index]
    )
    
    if rotated_first_input == second_input_char_list:
        are_inputs_circularly_equal = 'Yes'
        break

print(are_inputs_circularly_equal)