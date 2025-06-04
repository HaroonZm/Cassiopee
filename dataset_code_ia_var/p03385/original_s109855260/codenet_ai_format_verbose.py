user_input_characters_list = list(input())

found_character_a = 0
found_character_b = 0
found_character_c = 0

for character_index in range(3):
    
    if user_input_characters_list[character_index] == "a":
        found_character_a = 1
        
    if user_input_characters_list[character_index] == "b":
        found_character_b = 1
        
    if user_input_characters_list[character_index] == "c":
        found_character_c = 1

if found_character_a * found_character_b * found_character_c == 1:
    print("Yes")
else:
    print("No")