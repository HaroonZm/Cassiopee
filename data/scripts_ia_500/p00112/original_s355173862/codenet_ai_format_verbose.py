while True:
    
    number_of_elements = int(raw_input())
    
    if number_of_elements == 0:
        break
    
    elements = []
    total_weighted_sum = 0
    
    for index in range(number_of_elements):
        element_value = int(raw_input())
        elements.append(element_value)
    
    elements.sort()
    
    for reverse_index in range(number_of_elements - 1, 0, -1):
        weighted_index = number_of_elements - reverse_index - 1
        total_weighted_sum += reverse_index * elements[weighted_index]
    
    print total_weighted_sum