while True:

    grid_width, grid_height = map(int, raw_input().split())

    if grid_width == 0 and grid_height == 0:
        break

    movement_directions = (
        (0, 1),   # Up/North
        (1, 0),   # Right/East
        (0, -1),  # Down/South
        (-1, 0),  # Left/West
    )

    current_direction_index = 0  # 0:North, 1:East, 2:South, 3:West
    current_x_position = 1
    current_y_position = 1

    while True:

        user_command = raw_input()

        if user_command == "STOP":
            break

        if user_command[-1].isdigit():

            movement_type, movement_length = user_command.split()
            movement_length = int(movement_length)

            if movement_type == "FORWARD":
                current_x_position += movement_directions[current_direction_index][0] * movement_length
                current_y_position += movement_directions[current_direction_index][1] * movement_length

            elif movement_type == "BACKWARD":
                current_x_position -= movement_directions[current_direction_index][0] * movement_length
                current_y_position -= movement_directions[current_direction_index][1] * movement_length

            if current_x_position > grid_width:
                current_x_position = grid_width
            if current_x_position < 1:
                current_x_position = 1

            if current_y_position > grid_height:
                current_y_position = grid_height
            if current_y_position < 1:
                current_y_position = 1

        else:

            if user_command == "LEFT":
                if current_direction_index != 0:
                    current_direction_index -= 1
                else:
                    current_direction_index = 3

            elif user_command == "RIGHT":
                current_direction_index = (current_direction_index + 1) % 4

    print current_x_position, current_y_position