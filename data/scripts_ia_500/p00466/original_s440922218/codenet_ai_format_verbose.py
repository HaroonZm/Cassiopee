while True:
    
    input_string = input()
    
    if input_string == "0":
        break
    
    current_value = int(input_string)
    
    for iteration_index in range(9):
        
        input_value = int(input())
        current_value -= input_value
    
    print(current_value)