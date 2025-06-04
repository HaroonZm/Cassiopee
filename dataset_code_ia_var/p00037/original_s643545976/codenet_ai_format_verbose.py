def determine_next_move_based_on_walls_and_direction(human_state):
    
    # human_state format: (current_column, current_row, current_direction)
    # Direction encoding: 0 = east, 1 = south, 2 = west, 3 = north
    
    current_column = human_state[0]
    current_row = human_state[1]
    current_direction = human_state[2]
    
    wall_row_index = current_row * 2
    
    if current_direction == 0:  # Facing east
        wall_above_index = wall_row_index - 1
        wall_ahead_index = wall_row_index
        wall_below_index = wall_row_index + 1
        
        # Check left (wall_above_index, current_column)
        if (wall_above_index >= 0 and wall[wall_above_index][current_column] == '1'):
            return 3  # left
        # Check forward (wall_ahead_index, current_column)
        elif (current_column <= 3 and wall[wall_ahead_index][current_column] == '1'):
            return 0  # forward
        # Check right (wall_below_index, current_column)
        elif (wall_below_index <= 8 and wall[wall_below_index][current_column] == '1'):
            return 1  # right
        else:
            return 2  # backward
    
    if current_direction == 1:  # Facing south
        wall_ahead_index = wall_row_index
        wall_below_index = wall_row_index + 1
        wall_left_column = current_column - 1
        
        # Check left (wall_ahead_index, current_column)
        if (current_column <= 3 and wall[wall_ahead_index][current_column] == '1'):
            return 3
        # Check forward (wall_below_index, current_column)
        elif (wall_below_index <= 8 and wall[wall_below_index][current_column] == '1'):
            return 0
        # Check right (wall_ahead_index, wall_left_column)
        elif (wall_left_column >= 0 and wall[wall_ahead_index][wall_left_column] == '1'):
            return 1
        else:
            return 2  # backward
    
    if current_direction == 2:  # Facing west
        wall_below_index = wall_row_index + 1
        wall_ahead_index = wall_row_index
        wall_above_index = wall_row_index - 1
        wall_left_column = current_column - 1
        
        # Check left (wall_below_index, current_column)
        if (wall_below_index <= 8 and wall[wall_below_index][current_column] == '1'):
            return 3
        # Check forward (wall_ahead_index, wall_left_column)
        elif (wall_left_column >= 0 and wall[wall_ahead_index][wall_left_column] == '1'):
            return 0
        # Check right (wall_above_index, current_column)
        elif (wall_above_index >= 0 and wall[wall_above_index][current_column] == '1'):
            return 1
        else:
            return 2  # backward
    
    if current_direction == 3:  # Facing north
        wall_ahead_index = wall_row_index
        wall_left_column = current_column - 1
        wall_above_index = wall_row_index - 1
        
        # Check left (wall_ahead_index, wall_left_column)
        if (wall_left_column >= 0 and wall[wall_ahead_index][wall_left_column] == '1'):
            return 3
        # Check forward (wall_above_index, current_column)
        elif (wall_above_index >= 0 and wall[wall_above_index][current_column] == '1'):
            return 0
        # Check right (wall_ahead_index, current_column)
        elif (current_column <= 3 and wall[wall_ahead_index][current_column] == '1'):
            return 1
        else:
            return 2  # backward

walls_matrix = []

while True:
    try:
        for wall_row_counter in range(9):
            walls_matrix.append(raw_input())
    except:
        break

movement_solution_path = "R"
human_position_and_direction = (1, 0, 0)

while human_position_and_direction[0] != 0 or human_position_and_direction[1] != 0:
    
    next_turn = (human_position_and_direction[2] + determine_next_move_based_on_walls_and_direction(human_position_and_direction)) % 4
    
    current_column = human_position_and_direction[0]
    current_row = human_position_and_direction[1]
    
    if next_turn == 0:
        # Move east
        human_position_and_direction = (current_column + 1, current_row, next_turn)
        movement_solution_path += "R"
    elif next_turn == 1:
        # Move south
        human_position_and_direction = (current_column, current_row + 1, next_turn)
        movement_solution_path += "D"
    elif next_turn == 2:
        # Move west
        human_position_and_direction = (current_column - 1, current_row, next_turn)
        movement_solution_path += "L"
    else:
        # Move north
        human_position_and_direction = (current_column, current_row - 1, next_turn)
        movement_solution_path += "U"

print movement_solution_path