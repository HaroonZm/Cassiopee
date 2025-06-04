number_of_additional_inputs = input()

first_value, additional_value = map(int, raw_input().split())

initial_sum = input()

maximum_ratio = float(initial_sum) / first_value

additional_inputs_list = [input() for index in range(number_of_additional_inputs)]

current_sum_of_values = first_value
current_total_sum = initial_sum

for additional_input in reversed(sorted(additional_inputs_list)):
    
    current_sum_of_values += additional_value
    current_total_sum += additional_input

    current_ratio = float(current_total_sum) / current_sum_of_values
    
    if maximum_ratio <= current_ratio:
        maximum_ratio = current_ratio
    else:
        break

print maximum_ratio