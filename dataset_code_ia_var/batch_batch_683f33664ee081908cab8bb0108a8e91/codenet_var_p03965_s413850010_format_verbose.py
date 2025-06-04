user_input_string = input()
input_string_length = len(user_input_string)

total_game_points = 0

for character_index in range(1, input_string_length):
    
    is_odd_position = character_index % 2 != 0

    if is_odd_position:
        if user_input_string[character_index] == 'g':
            total_game_points += 1
    else:
        if user_input_string[character_index] == 'p':
            total_game_points -= 1

print(total_game_points)