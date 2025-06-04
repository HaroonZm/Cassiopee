import array

def is_valid_check_digit(input_digit_sequence):
    
    compute_weight_for_position = lambda position: (position + 1) if 1 <= position <= 6 else (position - 5)
    
    sum_of_weighted_digits = 0
    
    for digit_position in range(1, 12):
        digit_value = input_digit_sequence[digit_position]
        weight = compute_weight_for_position(digit_position)
        sum_of_weighted_digits += digit_value * weight
    
    modulus_eleven_remainder = sum_of_weighted_digits % 11
    
    expected_check_digit = 0 if modulus_eleven_remainder <= 1 else (11 - modulus_eleven_remainder)
    
    return input_digit_sequence[0] == expected_check_digit

def convert_string_to_digit_array(input_string):
    
    digit_list = list(map(int, input_string[::-1]))
    digit_byte_array = array.array("B", digit_list)
    
    return digit_byte_array

def find_unique_replacement_digit(identifier_string_with_unknown):
    
    possible_candidate_digits = set()
    
    for replacement_digit in range(0, 10):
        
        identifier_string_filled = identifier_string_with_unknown.replace("?", str(replacement_digit))
        
        digit_sequence = convert_string_to_digit_array(identifier_string_filled)
        
        if is_valid_check_digit(digit_sequence):
            possible_candidate_digits.add(replacement_digit)
    
    if len(possible_candidate_digits) == 1:
        return possible_candidate_digits.pop()
    else:
        return -1

def main():
    
    identifier_string_with_missing_digit = input()
    
    resulting_digit = find_unique_replacement_digit(identifier_string_with_missing_digit)
    
    if resulting_digit == -1:
        print("MULTIPLE")
    else:
        print(resulting_digit)

if __name__ == '__main__':
    main()