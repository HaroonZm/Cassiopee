number_of_input_parameters_and_minimum_fruits_to_select = list(map(int, input().split()))

fruit_prices_list = list(map(int, input().split()))

fruit_prices_list.sort()

total_minimum_fruit_cost = 0

for fruit_index in range(number_of_input_parameters_and_minimum_fruits_to_select[1]):
    
    total_minimum_fruit_cost += fruit_prices_list[fruit_index]

print(total_minimum_fruit_cost)