from copy import deepcopy

def rotate_points(point_list):
    return [[y, -x] for x, y in point_list]

def generate_moved_variants(reference_points, target_points):
    for target_x, target_y in target_points:
        delta_x = target_x - reference_points[0][0]
        delta_y = target_y - reference_points[0][1]
        translated_points = [[mx - delta_x, my - delta_y] for mx, my in target_points]
        yield translated_points
        yield list(reversed(translated_points))

def are_points_equal(points_a, points_b):
    return points_a == points_b

def check_all_movements_match(reference_points, target_points):
    for shifted_points in generate_moved_variants(reference_points, target_points):
        if are_points_equal(reference_points, shifted_points):
            return True
    return False

input_point_sequence = lambda: map(int, raw_input().split())

while True:
    num_targets = input()
    if num_targets == 0:
        break
    reference_shape = [input_point_sequence() for _ in range(input())]
    target_shapes_collection = [[input_point_sequence() for _ in range(input())] for _ in range(num_targets)]
    matching_indices = []
    for target_index, candidate_shape in enumerate(target_shapes_collection):
        rotated_candidate = deepcopy(candidate_shape)
        for rotation_attempt in range(4):
            if check_all_movements_match(reference_shape, rotated_candidate):
                matching_indices.append(target_index + 1)
                break
            rotated_candidate = rotate_points(rotated_candidate)
    for result_index in matching_indices:
        print result_index
    print '+++++'