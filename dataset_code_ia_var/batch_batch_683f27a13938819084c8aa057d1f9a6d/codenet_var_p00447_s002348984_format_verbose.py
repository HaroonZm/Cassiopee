import operator

for user_input_square_count in iter(input, '0'):
    
    reference_shape_coordinates = [
        [*map(int, input().split())]
        for _ in [0] * int(user_input_square_count)
    ]
    
    min_coordinate_x, min_coordinate_y = min(reference_shape_coordinates)
    
    normalized_reference_shape = {
        (x - min_coordinate_x, y - min_coordinate_y) 
        for x, y in reference_shape_coordinates
    }
    
    reference_shape_max_x = max(coordinate[0] for coordinate in normalized_reference_shape)
    
    target_shape_square_count = int(input())
    target_shape_coordinates = {
        tuple(map(int, input().split()))
        for _ in [0] * target_shape_square_count
    }
    
    max_target_shape_x = max(operator.itemgetter(0)(coordinates) for coordinates in target_shape_coordinates)
    max_offset_x = max_target_shape_x - reference_shape_max_x
    
    for candidate_origin_x, candidate_origin_y in target_shape_coordinates:
        if candidate_origin_x > max_offset_x:
            continue
        for delta_x, delta_y in normalized_reference_shape:
            if (candidate_origin_x + delta_x, candidate_origin_y + delta_y) not in target_shape_coordinates:
                break
        else:
            print(candidate_origin_x - min_coordinate_x, candidate_origin_y - min_coordinate_y)
            break