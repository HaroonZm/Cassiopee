def get_next_character_and_display():
    user_input_character = input()
    
    ascii_value_of_input = ord(user_input_character)
    
    ascii_value_of_next_character = ascii_value_of_input + 1
    
    next_character = chr(ascii_value_of_next_character)
    
    print(next_character)

if __name__ == '__main__':
    get_next_character_and_display()