debug_enabled = False

def debug_print(debug_message, additional_info=None):
    
    if debug_enabled:
        print(debug_message, additional_info)

def has_exact_sum(word_length_list, target_sum):
    
    running_sum = 0
    
    for index in range(len(word_length_list)):
        
        running_sum += word_length_list[index]
        
        if running_sum == target_sum:
            debug_print((True, index), word_length_list)
            return (True, index + 1)
        
        if running_sum > target_sum:
            debug_print((False, None), word_length_list)
            return (False, None)
            
    debug_print((False, None), word_length_list)
    return (False, None)

while True:
    
    number_of_lines = int(input())
    
    if number_of_lines == 0:
        break

    total_character_count = 0
    
    word_lengths = [0 for _ in range(number_of_lines)]
    
    for line_index in range(number_of_lines):
        
        line_length = len(input())
        
        word_lengths[line_index] = line_length
        
        total_character_count += line_length

    start_index = 0
    
    while start_index < total_character_count:
        
        check_first = has_exact_sum(word_lengths[start_index:], 5)
        
        if not check_first[0]:
            start_index += 1
            continue
        
        check_second = has_exact_sum(word_lengths[start_index + check_first[1]:], 7)
        
        if not check_second[0]:
            start_index += 1
            continue
        
        check_third = has_exact_sum(word_lengths[start_index + check_first[1] + check_second[1]:], 5)
        
        if not check_third[0]:
            start_index += 1
            continue
        
        check_fourth = has_exact_sum(word_lengths[start_index + check_first[1] + check_second[1] + check_third[1]:], 7)
        
        if not check_fourth[0]:
            start_index += 1
            continue
        
        check_fifth = has_exact_sum(word_lengths[start_index + check_first[1] + check_second[1] + check_third[1] + check_fourth[1]:], 7)
        
        if not check_fifth[0]:
            start_index += 1
            continue
        
        break

    print(start_index + 1)