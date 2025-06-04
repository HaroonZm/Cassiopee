if __name__ == '__main__':

    user_input_numbers_as_strings = input().split()
    
    user_input_numbers_as_integers = map(int, user_input_numbers_as_strings)
    
    sorted_numbers_descending = sorted(user_input_numbers_as_integers, reverse=True)
    
    largest_number = sorted_numbers_descending[0]
    second_largest_number = sorted_numbers_descending[1]
    smallest_number = sorted_numbers_descending[2]
    
    computed_result = (largest_number * 10) + second_largest_number + smallest_number
    
    print(str(computed_result))