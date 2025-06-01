input_x, input_y = list(map(int, input().split()))

fibonacci_sequence = [1, 1]
current_fibonacci = 0
while current_fibonacci < 10000000:
    
    current_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    
    fibonacci_sequence.append(current_fibonacci)

floor_areas = [[0, 0, 1]]

current_x, current_y = 0, 0
previous_fibonacci = 0
current_fibonacci = 1

for index in range(1, len(fibonacci_sequence)):
    
    current_fib_value = fibonacci_sequence[index]
    
    if index % 4 == 1:
        floor_areas.append([current_x + current_fibonacci, current_y + previous_fibonacci, current_fib_value])
        
    elif index % 4 == 2:
        floor_areas.append([current_x - previous_fibonacci, current_y + current_fib_value, current_fib_value])
        
    elif index % 4 == 3:
        floor_areas.append([current_x - current_fib_value, current_y, current_fib_value])
        
    elif index % 4 == 0:
        floor_areas.append([current_x, current_y - current_fibonacci, current_fib_value])
        
    previous_fibonacci = current_fibonacci
    current_fibonacci = current_fib_value
    
    current_x, current_y = floor_areas[-1][0:2]

for area_index, (area_x, area_y, area_size) in enumerate(floor_areas):
    
    if area_x <= input_x < area_x + area_size and area_y - area_size < input_y <= area_y:
        
        print(area_index % 3 + 1)
        
        break