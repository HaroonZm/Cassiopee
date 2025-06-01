import sys

input_coordinates = list(map(int, input().split()))

if input_coordinates[0] == 0 and input_coordinates[1] == 0:
    
    print("1")
    sys.exit()

fibonacci_sequence = [0, 1, 1]

maximum_coordinate_bounds = [0, 0]
minimum_coordinate_bounds = [0, 0]

iteration_index = 2

while True:
    
    if iteration_index % 4 == 2 or iteration_index % 4 == 3:
        maximum_coordinate_bounds[iteration_index % 2] += fibonacci_sequence[2]
    else:
        minimum_coordinate_bounds[iteration_index % 2] -= fibonacci_sequence[2]
        
    if (minimum_coordinate_bounds[0] <= input_coordinates[0] <= maximum_coordinate_bounds[0] and
        minimum_coordinate_bounds[1] <= input_coordinates[1] <= maximum_coordinate_bounds[1]):
        
        print(((iteration_index - 1) % 3) + 1)
        break
        
    fibonacci_sequence[0] = fibonacci_sequence[1]
    fibonacci_sequence[1] = fibonacci_sequence[2]
    fibonacci_sequence[2] = fibonacci_sequence[0] + fibonacci_sequence[1]
    
    iteration_index += 1