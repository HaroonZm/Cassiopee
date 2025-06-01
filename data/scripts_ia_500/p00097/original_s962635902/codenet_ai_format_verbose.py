max_index = 1001

index_range = range(9)

dynamic_table = [[0] * max_index for _ in index_range]

for current_row in range(101):
    
    for current_index in index_range[::-1]:
        
        if current_index == 0:
            
            dynamic_table[current_index][current_row] = 1
        
        else:
            
            for offset in range(max_index - current_row):
                
                dynamic_table[current_index][offset + current_row] += dynamic_table[current_index - 1][offset]

while True:
    
    input_n, input_s = map(int, raw_input().split())
    
    if input_n == 0 and input_s == 0:
        
        break
    
    print(dynamic_table[input_n - 1][input_s])