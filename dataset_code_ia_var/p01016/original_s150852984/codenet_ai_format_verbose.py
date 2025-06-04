first_input_string = input()
second_input_string = input()

length_of_first_string = len(first_input_string)
length_of_second_string = len(second_input_string)

for start_index in range(length_of_first_string - length_of_second_string + 1):
    
    is_match_found = True

    for offset in range(length_of_second_string):

        current_character_in_first = first_input_string[start_index + offset]
        current_character_in_second = second_input_string[offset]

        if current_character_in_first == current_character_in_second:
            continue
        else:
            if current_character_in_second == '_':
                continue
            else:
                is_match_found = False
                break

    if is_match_found:
        print('Yes')
        exit()

print('No')