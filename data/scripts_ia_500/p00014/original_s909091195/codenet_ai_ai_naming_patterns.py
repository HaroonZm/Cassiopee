for iteration_index in range(20):
    try:
        input_value_as_int = int(input())
        accumulated_size = 0
        
        max_inner_iterations = (600 // input_value_as_int) - 1
        for inner_index in range(max_inner_iterations):
            current_index = inner_index + 1
            accumulated_size += ((current_index * input_value_as_int) ** 2) * input_value_as_int
            
        print(int(accumulated_size))
        
    except:
        break