number_of_strings = int(input())
target_name = input()
target_name_length = len(target_name)
list_of_strings = [list(input()) for _ in range(number_of_strings)]

count_matches = 0
for string_index in range(number_of_strings):
    current_string = list_of_strings[string_index]
    match_found_flag = False
    current_string_length = len(current_string)
    
    for step in range(1, 101):
        if match_found_flag:
            break
        for start_pos in range(current_string_length):
            constructed_substring = ""
            position = start_pos
            for _ in range(target_name_length):
                if position < current_string_length:
                    constructed_substring += current_string[position]
                else:
                    break
                position += step
            if constructed_substring == target_name:
                match_found_flag = True
                break
    if match_found_flag:
        count_matches += 1

print(count_matches)