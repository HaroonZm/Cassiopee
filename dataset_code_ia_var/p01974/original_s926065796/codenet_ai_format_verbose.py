def find_and_print_pair_with_difference_multiple_of_n_minus_one():
    
    total_numbers = int(input())
    
    integer_list = [int(number_string) for number_string in input().split()]
    
    for first_index in range(total_numbers):
        
        for second_index in range(first_index + 1, total_numbers):
            
            absolute_difference = abs(integer_list[first_index] - integer_list[second_index])
            
            if absolute_difference % (total_numbers - 1) == 0:
                
                print(str(integer_list[first_index]) + " " + str(integer_list[second_index]))
                
                return

find_and_print_pair_with_difference_multiple_of_n_minus_one()