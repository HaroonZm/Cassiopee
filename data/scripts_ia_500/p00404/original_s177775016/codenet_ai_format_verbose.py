import sys

input_x, input_y = map(int, input().split())

iteration_count = 1
bottom_left_corner = [0, 0]
top_right_corner = [1, 1]

if bottom_left_corner[0] <= input_x < top_right_corner[0] and bottom_left_corner[1] <= input_y < top_right_corner[1]:
    
    print(iteration_count)
    sys.exit(0)

while True:
    
    if iteration_count % 4 == 1:
        top_right_corner[0] += top_right_corner[1] - bottom_left_corner[1]
        
    elif iteration_count % 4 == 2:
        top_right_corner[1] += top_right_corner[0] - bottom_left_corner[0]
        
    elif iteration_count % 4 == 3:
        bottom_left_corner[0] -= top_right_corner[1] - bottom_left_corner[1]
        
    elif iteration_count % 4 == 0:
        bottom_left_corner[1] -= top_right_corner[0] - bottom_left_corner[0]
        
    if bottom_left_corner[0] <= input_x < top_right_corner[0] and bottom_left_corner[1] <= input_y < top_right_corner[1]:
        print((iteration_count % 3) + 1)
        break
        
    iteration_count += 1