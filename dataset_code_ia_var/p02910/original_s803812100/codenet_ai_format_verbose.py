def is_string_valid_based_on_character_positions(input_string):
    
    for character_index in range(len(input_string)):
        
        current_character = input_string[character_index]
        
        if character_index % 2 == 0:
            allowed_characters_at_even_indices = ['R', 'U', 'D']
            if current_character not in allowed_characters_at_even_indices:
                return "No"
        else:
            allowed_characters_at_odd_indices = ['L', 'U', 'D']
            if current_character not in allowed_characters_at_odd_indices:
                return "No"
    
    return "Yes"


user_input_string = input()

print(is_string_valid_based_on_character_positions(user_input_string))