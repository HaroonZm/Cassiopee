alphabet_characters = 'qwertyuiopasdfghjklzxcvbnm'

user_input_string = input()

result_is_valid = 'yes'


for character_in_input in user_input_string:
    
    if character_in_input in alphabet_characters:
        
        alphabet_characters = alphabet_characters.replace(character_in_input, '')
        
    else:
        
        result_is_valid = 'no'
        
        break


print(result_is_valid)