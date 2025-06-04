DIVISOR_MODULO = 100000

while True:
    
    total_number_of_variables, maximum_value_per_variable, target_sum = map(int, raw_input().split())
    
    if total_number_of_variables == 0:
        break

    dp_table = [
        [0] * (target_sum + 1)
        for _ in range(total_number_of_variables * total_number_of_variables + 1)
    ]

    dp_table[0][0] = 1

    for current_number_of_variables in range(1, total_number_of_variables * total_number_of_variables + 1):
        for current_sum in range(target_sum + 1):

            if current_sum - current_number_of_variables >= 0:
                dp_table[current_number_of_variables][current_sum] = (
                    dp_table[current_number_of_variables][current_sum]
                    + dp_table[current_number_of_variables - 1][current_sum - current_number_of_variables]
                    + dp_table[current_number_of_variables][current_sum - current_number_of_variables]
                ) % DIVISOR_MODULO

            if current_sum - maximum_value_per_variable - 1 >= 0:
                dp_table[current_number_of_variables][current_sum] = (
                    dp_table[current_number_of_variables][current_sum]
                    - dp_table[current_number_of_variables - 1][current_sum - maximum_value_per_variable - 1]
                    + DIVISOR_MODULO
                ) % DIVISOR_MODULO

    print dp_table[total_number_of_variables * total_number_of_variables][target_sum]