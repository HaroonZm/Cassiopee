number_of_elements = int(input())

input_numbers_list = list(map(int, input().split()))

final_result = 0

cumulative_sum_coefficients = [0] * number_of_elements

running_total = 0

for current_index in range(number_of_elements):
    
    cumulative_sum_coefficients[current_index] += running_total
    
    running_total += input_numbers_list[current_index]


for current_index in range(number_of_elements):
    
    final_result += input_numbers_list[current_index] * cumulative_sum_coefficients[current_index]


modulo = 1000000000 + 7

print(final_result % modulo)