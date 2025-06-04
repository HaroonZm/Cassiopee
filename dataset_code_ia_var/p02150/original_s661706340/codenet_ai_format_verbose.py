minimum_value, step_subtract, initial_value = [int(input_value) for input_value in input().split()]

if initial_value >= minimum_value:
    
    number_of_full_steps = (initial_value - step_subtract) // (minimum_value - step_subtract)
    
    cumulative_result = number_of_full_steps * step_subtract + initial_value

else:
    
    cumulative_result = initial_value

print(cumulative_result % 1000000007)