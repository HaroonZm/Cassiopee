user_input_integer = int(input())

balanced_ternary_representation = ''
balanced_ternary_characters = '0+-'
current_power = 0

while user_input_integer > (3 ** current_power - 1) // 2:
    
    character_index = (user_input_integer + (3 ** current_power - 1) // 2) // (3 ** current_power) % 3
    
    balanced_ternary_representation += balanced_ternary_characters[character_index]
    
    current_power += 1

print(balanced_ternary_representation[::-1])