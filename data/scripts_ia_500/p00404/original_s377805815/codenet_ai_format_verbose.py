def find_region_containing_point(target_x, target_y):
    
    x_min_boundary = 0
    y_min_boundary = 0
    x_max_boundary = 0
    y_max_boundary = 0
    
    fibonacci_current = 0
    fibonacci_previous_1 = 1
    fibonacci_previous_2 = 0
    
    step_count = 0

    while True:
        
        if (x_min_boundary <= target_x <= x_max_boundary and
            y_min_boundary <= target_y <= y_max_boundary):
            return (step_count % 3) + 1
        
        fibonacci_current = fibonacci_previous_1 + fibonacci_previous_2
        
        direction_index = step_count % 4
        
        if direction_index == 0:            # move east: increase max x boundary
            x_max_boundary += fibonacci_current
        
        elif direction_index == 1:          # move north: increase max y boundary
            y_max_boundary += fibonacci_current
        
        elif direction_index == 2:          # move west: decrease min x boundary
            x_min_boundary -= fibonacci_current
        
        else:                              # move south: decrease min y boundary
            y_min_boundary -= fibonacci_current
        
        fibonacci_previous_2 = fibonacci_previous_1
        fibonacci_previous_1 = fibonacci_current
        
        step_count += 1


input_x, input_y = map(int, input().split())

print(find_region_containing_point(input_x, input_y))