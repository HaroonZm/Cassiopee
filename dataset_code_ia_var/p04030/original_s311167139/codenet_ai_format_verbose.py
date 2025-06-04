user_input_string = input()

resulting_string = ''

for current_character_index in range(len(user_input_string)):
    
    current_character = user_input_string[current_character_index]
    
    if resulting_string == '' and current_character == "B":
        # Do nothing if the result is empty and character is 'B'
        pass
    
    elif resulting_string == '' and current_character != "B":
        resulting_string = current_character
    
    elif current_character == "B":
        resulting_string = resulting_string[:-1]
    
    else:
        resulting_string += current_character

print(resulting_string)