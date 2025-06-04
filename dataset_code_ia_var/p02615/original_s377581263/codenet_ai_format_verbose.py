number_of_elements = int(input())

list_of_integers = [int(element) for element in input().split()]

list_of_integers.sort(reverse=True)

maximum_total_sum = list_of_integers[0]

remaining_positions_to_fill = number_of_elements - 2

current_index = 0

while remaining_positions_to_fill > 0:
    
    next_largest_value = list_of_integers[current_index + 1]
    
    if remaining_positions_to_fill >= 2:
        maximum_total_sum += next_largest_value * 2
        remaining_positions_to_fill -= 2
    else:
        maximum_total_sum += next_largest_value
        remaining_positions_to_fill -= 1
    
    current_index += 1

print(maximum_total_sum)