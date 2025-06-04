def parse_movement_sequence(movement_sequence):
    current_coordinates = [0, 0, 0]  # x, y, z
    marker_to_coordinates = {}
    line_segment_list = []

    for movement_token in movement_sequence:
        if movement_token.isdecimal():
            if movement_token in marker_to_coordinates:
                current_coordinates = marker_to_coordinates[movement_token]
            else:
                marker_to_coordinates[movement_token] = current_coordinates
        else:
            movement_direction_sign = 1 if movement_token[0] == "+" else -1

            if movement_token[1] == "x":
                start_position = current_coordinates.copy()
                end_position = [current_coordinates[0] + movement_direction_sign, current_coordinates[1], current_coordinates[2]]
                line_segment_list.append([start_position, end_position])
                current_coordinates = end_position

            elif movement_token[1] == "y":
                start_position = current_coordinates.copy()
                end_position = [current_coordinates[0], current_coordinates[1] + movement_direction_sign, current_coordinates[2]]
                line_segment_list.append([start_position, end_position])
                current_coordinates = end_position

            elif movement_token[1] == "z":
                start_position = current_coordinates.copy()
                end_position = [current_coordinates[0], current_coordinates[1], current_coordinates[2] + movement_direction_sign]
                line_segment_list.append([start_position, end_position])
                current_coordinates = end_position

    return line_segment_list

def rotate_around_x_axis(line_segments):
    minimum_y_coordinate = float("inf")
    minimum_z_coordinate = float("inf")
    
    for segment_index in range(len(line_segments)):
        for endpoint_index in range(2):
            y_before_rotation = line_segments[segment_index][endpoint_index][1]
            z_before_rotation = line_segments[segment_index][endpoint_index][2]
            
            line_segments[segment_index][endpoint_index][1] = -z_before_rotation
            line_segments[segment_index][endpoint_index][2] = y_before_rotation
            
            y_after_rotation = line_segments[segment_index][endpoint_index][1]
            z_after_rotation = line_segments[segment_index][endpoint_index][2]

            if y_after_rotation < minimum_y_coordinate:
                minimum_y_coordinate = y_after_rotation
            if z_after_rotation < minimum_z_coordinate:
                minimum_z_coordinate = z_after_rotation

    for segment_index in range(len(line_segments)):
        for endpoint_index in range(2):
            line_segments[segment_index][endpoint_index][1] -= minimum_y_coordinate
            line_segments[segment_index][endpoint_index][2] -= minimum_z_coordinate
        line_segments[segment_index].sort()
    return line_segments

def rotate_around_y_axis(line_segments):
    minimum_x_coordinate = float("inf")
    minimum_z_coordinate = float("inf")

    for segment_index in range(len(line_segments)):
        for endpoint_index in range(2):
            x_before_rotation = line_segments[segment_index][endpoint_index][0]
            z_before_rotation = line_segments[segment_index][endpoint_index][2]
            
            line_segments[segment_index][endpoint_index][0] = -z_before_rotation
            line_segments[segment_index][endpoint_index][2] = x_before_rotation

            x_after_rotation = line_segments[segment_index][endpoint_index][0]
            z_after_rotation = line_segments[segment_index][endpoint_index][2]

            if x_after_rotation < minimum_x_coordinate:
                minimum_x_coordinate = x_after_rotation
            if z_after_rotation < minimum_z_coordinate:
                minimum_z_coordinate = z_after_rotation

    for segment_index in range(len(line_segments)):
        for endpoint_index in range(2):
            line_segments[segment_index][endpoint_index][0] -= minimum_x_coordinate
            line_segments[segment_index][endpoint_index][2] -= minimum_z_coordinate
        line_segments[segment_index].sort()
    return line_segments

def rotate_around_z_axis(line_segments):
    minimum_x_coordinate = float("inf")
    minimum_y_coordinate = float("inf")

    for segment_index in range(len(line_segments)):
        for endpoint_index in range(2):
            x_before_rotation = line_segments[segment_index][endpoint_index][0]
            y_before_rotation = line_segments[segment_index][endpoint_index][1]
            
            line_segments[segment_index][endpoint_index][0] = -y_before_rotation
            line_segments[segment_index][endpoint_index][1] = x_before_rotation

            x_after_rotation = line_segments[segment_index][endpoint_index][0]
            y_after_rotation = line_segments[segment_index][endpoint_index][1]

            if x_after_rotation < minimum_x_coordinate:
                minimum_x_coordinate = x_after_rotation
            if y_after_rotation < minimum_y_coordinate:
                minimum_y_coordinate = y_after_rotation

    for segment_index in range(len(line_segments)):
        for endpoint_index in range(2):
            line_segments[segment_index][endpoint_index][0] -= minimum_x_coordinate
            line_segments[segment_index][endpoint_index][1] -= minimum_y_coordinate
        line_segments[segment_index].sort()
    return line_segments

def normalize_line_segments(line_segments):
    minimum_x_coordinate = float("inf")
    minimum_y_coordinate = float("inf")
    minimum_z_coordinate = float("inf")
    
    for segment in line_segments:
        for endpoint in segment:
            if endpoint[0] < minimum_x_coordinate:
                minimum_x_coordinate = endpoint[0]
            if endpoint[1] < minimum_y_coordinate:
                minimum_y_coordinate = endpoint[1]
            if endpoint[2] < minimum_z_coordinate:
                minimum_z_coordinate = endpoint[2]
    
    for segment_index in range(len(line_segments)):
        for endpoint_index in range(2):
            line_segments[segment_index][endpoint_index][0] -= minimum_x_coordinate
            line_segments[segment_index][endpoint_index][1] -= minimum_y_coordinate
            line_segments[segment_index][endpoint_index][2] -= minimum_z_coordinate
        line_segments[segment_index].sort()
    return line_segments

def are_polycubes_identical(line_segments_A, line_segments_B):
    if len(line_segments_A) != len(line_segments_B):
        return False

    line_segments_A.sort()
    line_segments_B.sort()
    for segment_index in range(len(line_segments_A)):
        if line_segments_A[segment_index][0] not in line_segments_B[segment_index] or line_segments_A[segment_index][1] not in line_segments_B[segment_index]:
            return False
    return True

while True:
    input_line = input()
    if input_line != "":
        first_polycube_raw = input_line.split()
        number_of_movements_polycube_1 = int(first_polycube_raw[0])
        movement_sequence_polycube_1 = first_polycube_raw[1:]
    else:
        continue

    if number_of_movements_polycube_1 == 0:
        break

    while len(movement_sequence_polycube_1) < number_of_movements_polycube_1:
        movement_sequence_polycube_1 += input().split()
    
    normalized_line_segments_polycube_1 = normalize_line_segments(parse_movement_sequence(movement_sequence_polycube_1))

    second_polycube_input = input().split()
    number_of_movements_polycube_2 = int(second_polycube_input[0])
    movement_sequence_polycube_2 = second_polycube_input[1:]

    while len(movement_sequence_polycube_2) < number_of_movements_polycube_2:
        movement_sequence_polycube_2 += input().split()

    normalized_line_segments_polycube_2 = normalize_line_segments(parse_movement_sequence(movement_sequence_polycube_2))

    polycubes_are_identical = False

    for rotation_around_z in range(4):
        for rotation_around_y in range(4):
            for rotation_around_x in range(4):
                if are_polycubes_identical(normalized_line_segments_polycube_1, normalized_line_segments_polycube_2):
                    polycubes_are_identical = True
                    break
                normalized_line_segments_polycube_2 = rotate_around_x_axis(normalized_line_segments_polycube_2)
            if polycubes_are_identical:
                break
            normalized_line_segments_polycube_2 = rotate_around_y_axis(normalized_line_segments_polycube_2)
        if polycubes_are_identical:
            break
        normalized_line_segments_polycube_2 = rotate_around_z_axis(normalized_line_segments_polycube_2)

    if polycubes_are_identical:
        print("SAME")
    else:
        print("DIFFERENT")