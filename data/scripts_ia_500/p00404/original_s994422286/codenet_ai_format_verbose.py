input_x, input_y = [int(value) for value in input().split()]

maximum_fibonacci_index = 100

fibonacci_sequence = [0 for _ in range(maximum_fibonacci_index)]
fibonacci_sequence[1] = 1
fibonacci_sequence[2] = 1

for index in range(3, maximum_fibonacci_index):
    
    fibonacci_sequence[index] = fibonacci_sequence[index - 1] + fibonacci_sequence[index - 2]
    
    
x_upper_bound = 0
y_upper_bound = 0
x_lower_bound = 0
y_lower_bound = 0

result_index = -1

if (input_x <= x_upper_bound and input_y <= y_upper_bound and input_x >= x_lower_bound and input_y >= y_lower_bound):
    
    result_index = 1
    
else:
    
    fibo_index = 2
    
    while True:
        
        x_upper_bound += fibonacci_sequence[fibo_index]
        
        if (input_x <= x_upper_bound and input_y <= y_upper_bound and input_x >= x_lower_bound and input_y >= y_lower_bound):
            
            result_index = fibo_index
            break
            
        else:
            fibo_index += 1
        
        y_upper_bound += fibonacci_sequence[fibo_index]
        
        if (input_x <= x_upper_bound and input_y <= y_upper_bound and input_x >= x_lower_bound and input_y >= y_lower_bound):
            
            result_index = fibo_index
            break
            
        else:
            fibo_index += 1
        
        x_lower_bound -= fibonacci_sequence[fibo_index]
        
        if (input_x <= x_upper_bound and input_y <= y_upper_bound and input_x >= x_lower_bound and input_y >= y_lower_bound):
            
            result_index = fibo_index
            break
            
        else:
            fibo_index += 1
        
        y_lower_bound -= fibonacci_sequence[fibo_index]
        
        if (input_x <= x_upper_bound and input_y <= y_upper_bound and input_x >= x_lower_bound and input_y >= y_lower_bound):
            
            result_index = fibo_index
            break
            
        else:
            fibo_index += 1
            
result_index = result_index % 3

if result_index == 0:
    
    result_index = 3
    
    
print(result_index)