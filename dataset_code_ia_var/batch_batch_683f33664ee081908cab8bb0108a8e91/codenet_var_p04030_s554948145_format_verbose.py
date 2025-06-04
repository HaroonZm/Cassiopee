user_input_string = input()

resulting_character_list = []

for current_character in user_input_string:
    
    if current_character == '0':
        resulting_character_list.append('0')
        
    elif current_character == '1':
        resulting_character_list.append('1')
        
    elif len(resulting_character_list) > 0:
        resulting_character_list.pop(-1)

final_output_string = ''.join(resulting_character_list)

print(final_output_string)