while True:
    
    try:
        
        input_numbers = raw_input()
        
        number_list = list(map(int, input_numbers.split()))
        
        first_number, second_number = sorted(number_list)
        
        while first_number != 0:
            
            temporary_value = first_number
            
            first_number = second_number % first_number
            
            second_number = temporary_value
        
        print second_number
    
    except EOFError:
        
        break