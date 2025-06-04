def calculate_fizz_buzz_start_position(limit_number):
    
    sequence_position_count = -1
    digit_length = 1
    
    while 10 ** digit_length < limit_number:
        
        lower_bound = 10 ** (digit_length - 1)
        upper_bound = 10 ** digit_length
        
        total_numbers_in_range = upper_bound - lower_bound
        
        sequence_position_count += digit_length * total_numbers_in_range
        
        fizz_buzz_both_count = ( (upper_bound - 1) // 15 ) - ( (lower_bound - 1) // 15 )
        fizz_count = ( (upper_bound - 1) // 3 ) - ( (lower_bound - 1) // 3 )
        buzz_count = ( (upper_bound - 1) // 5 ) - ( (lower_bound - 1) // 5 )
        
        non_number_entry_count = (fizz_count + buzz_count) * 4 - (fizz_count + buzz_count - fizz_buzz_both_count) * digit_length
        
        sequence_position_count += non_number_entry_count
        
        digit_length += 1
    
    lower_bound = 10 ** (digit_length - 1)
    total_numbers_remaining = limit_number - lower_bound
    
    sequence_position_count += digit_length * total_numbers_remaining
    
    fizz_buzz_both_count = ( (limit_number - 1) // 15 ) - ( (lower_bound - 1) // 15 )
    fizz_count = ( (limit_number - 1) // 3 ) - ( (lower_bound - 1) // 3 )
    buzz_count = ( (limit_number - 1) // 5 ) - ( (lower_bound - 1) // 5 )
    
    non_number_entry_count = (fizz_count + buzz_count) * 4 - (fizz_count + buzz_count - fizz_buzz_both_count) * digit_length
    
    sequence_position_count += non_number_entry_count
    
    return sequence_position_count + 1

total_sequence_index_target = int(input()) - 1

binary_search_left = 1
binary_search_right = 10 ** 18

while binary_search_left + 1 < binary_search_right:
    
    binary_search_mid = (binary_search_left + binary_search_right) // 2
    calculated_start_position = calculate_fizz_buzz_start_position(binary_search_mid)
    
    if calculated_start_position <= total_sequence_index_target:
        binary_search_left = binary_search_mid
    else:
        binary_search_right = binary_search_mid

fizz_buzz_output_sequence = ''

for current_number in range(binary_search_left, binary_search_left + 30):
    
    current_fizz_buzz_string = ''
    
    if current_number % 3 == 0:
        current_fizz_buzz_string += "Fizz"
    if current_number % 5 == 0:
        current_fizz_buzz_string += "Buzz"
    if not current_fizz_buzz_string:
        current_fizz_buzz_string = str(current_number)
    
    fizz_buzz_output_sequence += current_fizz_buzz_string

starting_index_after_binary_search = calculate_fizz_buzz_start_position(binary_search_left)

output_substring_start = total_sequence_index_target - starting_index_after_binary_search
output_substring_end = output_substring_start + 20

print(fizz_buzz_output_sequence[output_substring_start:output_substring_end])