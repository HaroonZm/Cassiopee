import math

def compute_angle_between_points(start_point, end_point):
    start_x, start_y = start_point
    end_x, end_y = end_point
    return math.atan2(end_y - start_y, end_x - start_x)

def compute_distance_between_points(start_point, end_point):
    start_x, start_y = start_point
    end_x, end_y = end_point
    return math.sqrt((end_x - start_x) ** 2 + (end_y - start_y) ** 2)

while True:
    number_of_points = int(raw_input())
    if number_of_points == 0:
        break
    else:
        remaining_points = []
        for point_index in range(number_of_points):
            current_point = [int(coordinate) for coordinate in raw_input().split()]
            remaining_points.append(current_point)

        current_position = [0, 0]
        current_angle_in_radians = math.pi / 2
        total_path_length = 0

        for iteration_index in range(number_of_points):
            best_candidate_angle = None
            best_candidate_distance = None
            best_candidate_index = None

            for candidate_index, candidate_point in enumerate(remaining_points):
                angle_to_candidate = compute_angle_between_points(current_position, candidate_point)
                angle_difference = -angle_to_candidate + current_angle_in_radians

                if angle_difference < 0:
                    angle_difference += 2 * math.pi

                distance_to_candidate = compute_distance_between_points(current_position, candidate_point)

                if (best_candidate_angle is None or
                    angle_difference < best_candidate_angle or
                    (angle_difference == best_candidate_angle and distance_to_candidate < best_candidate_distance)):
                    best_candidate_angle = angle_difference
                    best_candidate_distance = distance_to_candidate
                    best_candidate_index = candidate_index

            next_point = remaining_points.pop(best_candidate_index)
            total_path_length += compute_distance_between_points(current_position, next_point)
            current_angle_in_radians = compute_angle_between_points(current_position, next_point)
            current_position = next_point

        print round(total_path_length, 1)