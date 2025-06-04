def are_keys_equivalent(reference_key_positions, comparison_key_positions):
    normalized_comparison_positions = normalize_key(comparison_key_positions)
    
    for x_rotation_count in range(4):
        reference_key_positions = rotate_key_along_x_axis(reference_key_positions)
        
        for y_rotation_count in range(4):
            reference_key_positions = rotate_key_along_y_axis(reference_key_positions)
            
            for z_rotation_count in range(4):
                reference_key_positions = rotate_key_along_z_axis(reference_key_positions)
                
                is_match = True
                
                for position_pair_in_comparison in normalized_comparison_positions:
                    if (
                        position_pair_in_comparison not in reference_key_positions and
                        [position_pair_in_comparison[1], position_pair_in_comparison[0]] not in reference_key_positions
                    ):
                        is_match = False
                
                if is_match:
                    return True
    return False

def rotate_key_along_x_axis(key_position_list):
    rotated_key_positions = []
    
    for position_pair in key_position_list:
        rotated_position_pair = []
        
        for coordinate in position_pair:
            rotated_coordinate = [
                coordinate[0], 
                coordinate[2], 
                -coordinate[1]
            ]
            rotated_position_pair.append(rotated_coordinate)
        
        rotated_key_positions.append(rotated_position_pair)
    
    return normalize_key(rotated_key_positions)

def rotate_key_along_y_axis(key_position_list):
    rotated_key_positions = []
    
    for position_pair in key_position_list:
        rotated_position_pair = []
        
        for coordinate in position_pair:
            rotated_coordinate = [
                -coordinate[2], 
                coordinate[1], 
                coordinate[0]
            ]
            rotated_position_pair.append(rotated_coordinate)
        
        rotated_key_positions.append(rotated_position_pair)
    
    return normalize_key(rotated_key_positions)

def rotate_key_along_z_axis(key_position_list):
    rotated_key_positions = []
    
    for position_pair in key_position_list:
        rotated_position_pair = []
        
        for coordinate in position_pair:
            rotated_coordinate = [
                coordinate[1], 
                -coordinate[0], 
                coordinate[2]
            ]
            rotated_position_pair.append(rotated_coordinate)
        
        rotated_key_positions.append(rotated_position_pair)
    
    return normalize_key(rotated_key_positions)

def direction_string_to_vector(direction_string):
    if direction_string[0] == '+':
        if direction_string[1] == 'x':
            return [1, 0, 0]
        elif direction_string[1] == 'y':
            return [0, 1, 0]
        else:
            return [0, 0, 1]
    else:
        if direction_string[1] == 'x':
            return [-1, 0, 0]
        elif direction_string[1] == 'y':
            return [0, -1, 0]
        else:
            return [0, 0, -1]

def vector_addition(vector1, vector2):
    summed_vector = []
    for coordinate_index in range(len(vector1)):
        summed_vector.append(vector1[coordinate_index] + vector2[coordinate_index])
    return summed_vector

def normalize_key(key_position_list):
    minimal_x = float('inf')
    minimal_y = float('inf')
    minimal_z = float('inf')
    
    for position_pair in key_position_list:
        for coordinate in position_pair:
            minimal_x = min(minimal_x, coordinate[0])
            minimal_y = min(minimal_y, coordinate[1])
            minimal_z = min(minimal_z, coordinate[2])
    
    normalized_key_positions = []
    
    for position_pair in key_position_list:
        normalized_position_pair = []
        
        for coordinate in position_pair:
            normalized_coordinate = [
                coordinate[0] - minimal_x,
                coordinate[1] - minimal_y,
                coordinate[2] - minimal_z
            ]
            normalized_position_pair.append(normalized_coordinate)
        
        normalized_key_positions.append(normalized_position_pair)
    
    return normalized_key_positions

previous_key_positions = []
current_key_positions = []

while True:
    is_input_needed = True
    
    if not previous_key_positions:
        previous_key_positions, current_key_positions, main_input_counter = current_key_positions, [], 0
    else:
        previous_key_positions, current_key_positions, main_input_counter = [], [], 0
    
    generated_key_label_to_position = {'0': (0, 0, 0)}
    current_position_coordinates = [0, 0, 0]
    raw_input_line = False
    
    while not raw_input_line:
        raw_input_line = input()
    
    if not raw_input_line.isdecimal():
        raw_key_count, *input_tokens = raw_input_line.split()
        is_input_needed = False
    else:
        raw_key_count = raw_input_line
    
    key_pair_count = int(raw_key_count)
    if not key_pair_count:
        break
    
    while main_input_counter < key_pair_count:
        if is_input_needed:
            input_tokens = input().split()
        
        for token_index in range(len(input_tokens)):
            current_token = input_tokens[token_index]
            
            if current_token.isdecimal():
                if current_token not in generated_key_label_to_position:
                    generated_key_label_to_position[current_token] = current_position_coordinates
                else:
                    current_position_coordinates = generated_key_label_to_position[current_token]
            else:
                current_key_positions.append([current_position_coordinates])
                current_position_coordinates = vector_addition(
                    direction_string_to_vector(current_token), 
                    current_position_coordinates
                )
                current_key_positions[-1].append(current_position_coordinates)
            
            main_input_counter += 1
    
    if previous_key_positions:
        if are_keys_equivalent(current_key_positions, previous_key_positions):
            print('SAME')
        else:
            print('DIFFERENT')