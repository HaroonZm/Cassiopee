import sys

input_stream = sys.stdin.readline
output_stream = sys.stdout.write

def calculate_line_segments_intersection(point_a_start, point_a_end, point_b_start, point_b_end):
    ax_start, ay_start = point_a_start
    ax_end, ay_end = point_a_end
    bx_start, by_start = point_b_start
    bx_end, by_end = point_b_end

    direction_a_x = ax_end - ax_start
    direction_a_y = ay_end - ay_start
    direction_b_x = bx_end - bx_start
    direction_b_y = by_end - by_start

    numerator = (ay_start - by_start) * direction_b_x - (ax_start - bx_start) * direction_b_y
    denominator = direction_a_x * direction_b_y - direction_a_y * direction_b_x

    if denominator == 0:
        return None

    intersection_x = ax_start + numerator * direction_a_x / denominator
    intersection_y = ay_start + numerator * direction_a_y / denominator

    return (intersection_x, intersection_y)

def solve_problem_instance():
    rectangle_width, rectangle_height, num_segments, obstacle_radius = map(int, input_stream().split())
    if rectangle_width == 0 and rectangle_height == 0:
        return False

    segments_list = [
        tuple(map(int, input_stream().split()))
        for _ in range(num_segments)
    ]

    # Add rectangle boundaries as segments, mark with type indicator as 0
    segments_list.extend([
        (0, 0, rectangle_width, 0, 0),
        (0, 0, 0, rectangle_height, 0),
        (0, rectangle_height, rectangle_width, rectangle_height, 0),
        (rectangle_width, 0, rectangle_width, rectangle_height, 0),
    ])

    floating_point_epsilon = 1e-9
    iteration_sign_pairs = ((1, 1), (1, -1), (-1, 1), (-1, -1))

    total_segments = num_segments + 4

    for current_index in range(total_segments):
        start_x_1, start_y_1, end_x_1, end_y_1, thickness_1 = segments_list[current_index]
        segment_1_start = (start_x_1, start_y_1)
        segment_1_end = (end_x_1, end_y_1)
        segment_1_dx = end_x_1 - start_x_1
        segment_1_dy = end_y_1 - start_y_1
        segment_1_length = (segment_1_dx ** 2 + segment_1_dy ** 2) ** 0.5

        for previous_index in range(current_index):
            start_x_2, start_y_2, end_x_2, end_y_2, thickness_2 = segments_list[previous_index]
            segment_2_start = (start_x_2, start_y_2)
            segment_2_end = (end_x_2, end_y_2)
            segment_2_dx = end_x_2 - start_x_2
            segment_2_dy = end_y_2 - start_y_2
            segment_2_length = (segment_2_dx ** 2 + segment_2_dy ** 2) ** 0.5

            intersection_point = calculate_line_segments_intersection(
                segment_1_start, segment_1_end,
                segment_2_start, segment_2_end
            )

            if intersection_point is None:
                continue

            intersection_x, intersection_y = intersection_point
            cross_vector_magnitude = abs(segment_1_dx * segment_2_dy - segment_2_dx * segment_1_dy)

            for sign_p, sign_q in iteration_sign_pairs:
                shift_distance_a = sign_p * segment_2_length * (thickness_2 + obstacle_radius)
                shift_distance_b = sign_q * segment_1_length * (thickness_1 + obstacle_radius)

                candidate_x = intersection_x + (
                    shift_distance_a * segment_1_dx + shift_distance_b * segment_2_dx
                ) / cross_vector_magnitude

                candidate_y = intersection_y + (
                    shift_distance_a * segment_1_dy + shift_distance_b * segment_2_dy
                ) / cross_vector_magnitude

                if not (obstacle_radius - floating_point_epsilon < candidate_x < rectangle_width - obstacle_radius + floating_point_epsilon):
                    continue
                if not (obstacle_radius - floating_point_epsilon < candidate_y < rectangle_height - obstacle_radius + floating_point_epsilon):
                    continue

                placement_valid = True
                for obstacle_index in range(num_segments):
                    obs_x_1, obs_y_1, obs_x_2, obs_y_2, obs_thickness = segments_list[obstacle_index]
                    obstacle_dx = obs_x_2 - obs_x_1
                    obstacle_dy = obs_y_2 - obs_y_1
                    candidate_to_obs_dx = candidate_x - obs_x_1
                    candidate_to_obs_dy = candidate_y - obs_y_1
                    obstacle_length = (obstacle_dx ** 2 + obstacle_dy ** 2) ** 0.5

                    cross_product_magnitude = abs(obstacle_dx * candidate_to_obs_dy - candidate_to_obs_dx * obstacle_dy)
                    required_minimum_distance = (obstacle_radius + obs_thickness) * obstacle_length - floating_point_epsilon

                    if cross_product_magnitude < required_minimum_distance:
                        placement_valid = False
                        break

                if placement_valid:
                    output_stream("Yes\n")
                    return True

    output_stream("No\n")
    return True

while solve_problem_instance():
    pass