while True:
    
    number_of_elements, step_size = map(int, input().split())
    
    if number_of_elements == 0:
        break
    
    elements_list = [element for element in range(1, number_of_elements + 1)]
    
    current_index = number_of_elements - 1
    
    while len(elements_list) > 1:
        
        current_index = (current_index + step_size) % len(elements_list)
        
        elements_list.pop(current_index)
        
        current_index -= 1
    
    print(elements_list[0])