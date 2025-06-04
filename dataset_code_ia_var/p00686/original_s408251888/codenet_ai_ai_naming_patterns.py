while True:
    grid_width, grid_height = map(int, raw_input().split())
    if grid_width == 0 and grid_height == 0:
        break
    direction_vectors = ((0,1), (1,0), (0,-1), (-1,0))
    direction_index = 0
    position_x = 1
    position_y = 1
    while True:
        command_input = raw_input()
        if command_input == "STOP":
            break
        if command_input[-1].isdigit():
            movement_type, movement_length = command_input.split()
            movement_length_int = int(movement_length)
            if movement_type == "FORWARD":
                position_x += direction_vectors[direction_index][0] * movement_length_int
                position_y += direction_vectors[direction_index][1] * movement_length_int
            elif movement_type == "BACKWARD":
                position_x -= direction_vectors[direction_index][0] * movement_length_int
                position_y -= direction_vectors[direction_index][1] * movement_length_int
            position_x = min(max(position_x, 1), grid_width)
            position_y = min(max(position_y, 1), grid_height)
        else:
            if command_input == "LEFT":
                direction_index = (direction_index - 1) % 4
            elif command_input == "RIGHT":
                direction_index = (direction_index + 1) % 4
    print position_x, position_y