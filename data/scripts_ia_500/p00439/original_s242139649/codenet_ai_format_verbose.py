array_values, sum_values = [0] * 100003, [0] * 100003

while True:
    
    number_of_elements, window_size = map(int, input().split())
    
    if number_of_elements == 0:
        break
    
    array_values[0] = int(input())
    sum_values[0] = array_values[0]
    
    for current_index in range(1, number_of_elements):
        
        array_values[current_index] = int(input())
        
        sum_values[current_index] = sum_values[current_index - 1] + array_values[current_index]
        
        if current_index >= window_size:
            sum_values[current_index] -= array_values[current_index - window_size]
    
    maximum_window_sum = 0
    
    for current_index in range(window_size, number_of_elements):
        
        if sum_values[current_index] > maximum_window_sum:
            maximum_window_sum = sum_values[current_index]
    
    print(maximum_window_sum)