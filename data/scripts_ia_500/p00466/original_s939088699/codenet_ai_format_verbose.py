while True:
    
    input_line = input()
    
    if not input_line:
        break
    
    for iteration_index in range(9):
        input_line -= input()
    
    print(input_line)