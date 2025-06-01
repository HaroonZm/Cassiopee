array_values, prefix_sums = [0] * 100003, [0] * 100003

while True:
    
    number_of_elements, subarray_length = map(int, input().split())
    if number_of_elements == 0:
        break
    
    first_value = int(input())
    array_values[0] = first_value
    prefix_sums[0] = first_value
    
    for index in range(1, number_of_elements):
        current_value = int(input())
        array_values[index] = current_value
        prefix_sums[index] = prefix_sums[index - 1] + current_value
        
        if index >= subarray_length:
            prefix_sums[index] -= array_values[index - subarray_length]
    
    maximum_sum = prefix_sums[subarray_length - 1]
    
    for index in range(subarray_length, number_of_elements):
        if prefix_sums[index] > maximum_sum:
            maximum_sum = prefix_sums[index]
    
    print(maximum_sum)