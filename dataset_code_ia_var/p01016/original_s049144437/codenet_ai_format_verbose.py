first_input_string = input()
second_input_string = input()

length_of_first_input = len(first_input_string)
length_of_second_input = len(second_input_string)

def does_pattern_match_with_wildcard():
    
    for start_index in range(length_of_first_input - length_of_second_input + 1):
        
        for current_pattern_index in range(length_of_second_input):
            
            current_pattern_character = second_input_string[current_pattern_index]
            current_target_character = first_input_string[start_index + current_pattern_index]
            
            if current_pattern_character == "_" or current_target_character == current_pattern_character:
                continue
            else:
                break
        
        else:
            print("Yes")
            return
    
    print("No")
    return

does_pattern_match_with_wildcard()