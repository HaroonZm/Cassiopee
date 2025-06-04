while True:
    segment_count = int(input())
    
    x_coords = [0] * segment_count
    y_coords = [0] * segment_count
    dir_x = [-1, 0, 1, 0]
    dir_y = [0, -1, 0, 1]
    
    if segment_count == 0:
        break
    
    for segment_index in range(1, segment_count):
        prev_index, direction = map(int, input().split())
        x_coords[segment_index] = x_coords[prev_index] + dir_x[direction]
        y_coords[segment_index] = y_coords[prev_index] + dir_y[direction]
    
    width = max(x_coords) - min(x_coords) + 1
    height = max(y_coords) - min(y_coords) + 1
    print(width, height)