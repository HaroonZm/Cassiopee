import math as math_module

input_character_list = list(input())

change_of_character_indexes = [0]

for character_index in range(1, len(input_character_list)):
    if input_character_list[character_index] != input_character_list[character_index - 1]:
        change_of_character_indexes.append(character_index)

change_of_character_indexes.append(len(input_character_list))

resultant_counts_list = [0] * len(input_character_list)

for segment_index in range(1, len(change_of_character_indexes), 2):
    current_change_index = change_of_character_indexes[segment_index]
    consecutive_same_left = change_of_character_indexes[segment_index] - change_of_character_indexes[segment_index - 1]
    consecutive_same_right = change_of_character_indexes[segment_index + 1] - change_of_character_indexes[segment_index]
    
    resultant_counts_list[current_change_index - 1] = (
        math_module.ceil(consecutive_same_left / 2) + math_module.floor(consecutive_same_right / 2)
    )
    
    resultant_counts_list[current_change_index] = (
        math_module.floor(consecutive_same_left / 2) + math_module.ceil(consecutive_same_right / 2)
    )

print(*resultant_counts_list)