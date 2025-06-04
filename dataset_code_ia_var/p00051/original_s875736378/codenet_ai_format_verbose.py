def calculate_difference_between_max_and_min_number_from_digits(digit_list):
    
    digits_sorted_descending = sorted(digit_list, reverse=True)
    
    digits_sorted_ascending = sorted(digit_list)
    
    number_from_ascending_digits = 0
    number_from_descending_digits = 0
    
    total_digits = len(digit_list)
    
    for digit_index in range(total_digits):
        
        number_from_ascending_digits += digits_sorted_ascending[digit_index] * (10 ** digit_index)
        
        number_from_descending_digits += digits_sorted_descending[digit_index] * (10 ** digit_index)
    
    return number_from_ascending_digits - number_from_descending_digits


number_of_test_cases = int(input())

for test_case_index in range(number_of_test_cases):
    
    input_digits_as_characters = input()
    
    digits_as_integer_list = list(map(int, input_digits_as_characters))
    
    difference = calculate_difference_between_max_and_min_number_from_digits(digits_as_integer_list)
    
    print(difference)