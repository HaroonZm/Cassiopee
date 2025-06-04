def main():
    while True:
        number_of_rows, upper_sum_limit, target_sum = map(int, input().split())
        
        if max(number_of_rows, upper_sum_limit, target_sum) == 0:
            break
        
        calculated_answer = compute_number_of_partitions(number_of_rows, upper_sum_limit, target_sum)
        
        print(calculated_answer)

def compute_number_of_partitions(number_of_rows, upper_sum_limit, target_sum):
    MODULO_CONSTANT = 10 ** 5
    
    total_cell_count = number_of_rows * number_of_rows
    
    max_additional_value_per_cell = upper_sum_limit - total_cell_count
    
    minimum_possible_sum = (total_cell_count * (total_cell_count + 1)) // 2
    
    required_additional_sum = target_sum - minimum_possible_sum
    
    dp_table = [[0 for additional_sum in range(required_additional_sum + 1)] for cell_index in range(total_cell_count + 1)]
    
    dp_table[0][0] = 1
    
    for current_cell in range(1, total_cell_count + 1):
        for current_additional_sum in range(required_additional_sum + 1):
            dp_table[current_cell][current_additional_sum] = dp_table[current_cell - 1][current_additional_sum]
            
            if current_additional_sum - current_cell >= 0:
                dp_table[current_cell][current_additional_sum] += dp_table[current_cell][current_additional_sum - current_cell]
            
            if current_additional_sum - current_cell - max_additional_value_per_cell >= 0:
                dp_table[current_cell][current_additional_sum] -= dp_table[current_cell - 1][current_additional_sum - current_cell - max_additional_value_per_cell]
            
            dp_table[current_cell][current_additional_sum] %= MODULO_CONSTANT
    
    number_of_valid_partitions = dp_table[total_cell_count][required_additional_sum]
    
    return number_of_valid_partitions

main()