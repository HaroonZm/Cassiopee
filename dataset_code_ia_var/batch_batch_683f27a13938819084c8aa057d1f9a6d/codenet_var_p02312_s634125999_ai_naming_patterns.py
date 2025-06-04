import math

def circle_polygon_intersection_area(circle_params, polygon_points):
    circle_center_x, circle_center_y, circle_radius = circle_params
    total_area = 0.0
    num_points = len(polygon_points)

    for vertex_index in range(num_points):
        point_a = polygon_points[vertex_index]
        point_b = polygon_points[(vertex_index + 1) % num_points]
        intersection_points = segment_circle_intersections(circle_params, (point_a, point_b))
        all_segment_points = [point_a] + intersection_points + [point_b]
        for sub_index in range(len(all_segment_points) - 1):
            sub_point_start = all_segment_points[sub_index]
            sub_point_end = all_segment_points[sub_index + 1]

            cross_product_value = vector_cross(sub_point_start, sub_point_end)
            if cross_product_value == 0.0:
                continue

            start_distance = math.hypot(*sub_point_start)
            end_distance = math.hypot(*sub_point_end)
            if is_less_or_equal(start_distance, circle_radius) and is_less_or_equal(end_distance, circle_radius):
                total_area += cross_product_value / 2.0
            else:
                dot_product_value = vector_dot(sub_point_start, sub_point_end)
                angle = math.acos(dot_product_value / (start_distance * end_distance))
                orientation_sign = cross_product_value / abs(cross_product_value)
                total_area += orientation_sign * circle_radius * circle_radius * angle / 2.0

    return total_area

def vector_cross(vector_a, vector_b):
    ax, ay = vector_a
    bx, by = vector_b
    return ax * by - bx * ay

def vector_dot(vector_a, vector_b):
    ax, ay = vector_a
    bx, by = vector_b
    return ax * bx + ay * by

def segment_circle_intersections(circle_params, segment_points):
    center_x, center_y, radius = circle_params
    seg_start, seg_end = segment_points
    seg_start_x, seg_start_y = seg_start
    seg_end_x, seg_end_y = seg_end

    segment_dx = seg_end_x - seg_start_x
    segment_dy = seg_end_y - seg_start_y
    segment_length_squared = segment_dx ** 2 + segment_dy ** 2

    shifted_start_x = seg_start_x - center_x
    shifted_start_y = seg_start_y - center_y
    shifted_end_x = seg_end_x - center_x
    shifted_end_y = seg_end_y - center_y

    start_to_center_distance_squared = shifted_start_x ** 2 + shifted_start_y ** 2
    dot_product_with_direction = vector_dot((shifted_start_x, shifted_start_y), (segment_dx, segment_dy))
    radius_squared = radius ** 2

    discriminant = dot_product_with_direction ** 2 - segment_length_squared * (start_to_center_distance_squared - radius_squared)
    valid_intersections = []

    if math.isclose(discriminant, 0.0, abs_tol=1e-9):
        t = -dot_product_with_direction / segment_length_squared
        if is_greater_or_equal(t, 0.0) and is_less_or_equal(t, 1.0):
            intersect_x = seg_start_x + t * segment_dx
            intersect_y = seg_start_y + t * segment_dy
            valid_intersections.append((intersect_x, intersect_y))
    elif discriminant > 0.0:
        sqrt_discriminant = math.sqrt(discriminant)
        t1 = (-dot_product_with_direction - sqrt_discriminant) / segment_length_squared
        t2 = (-dot_product_with_direction + sqrt_discriminant) / segment_length_squared
        for t_candidate in (t1, t2):
            if is_greater_or_equal(t_candidate, 0.0) and is_less_or_equal(t_candidate, 1.0):
                intersect_x = seg_start_x + t_candidate * segment_dx
                intersect_y = seg_start_y + t_candidate * segment_dy
                valid_intersections.append((intersect_x, intersect_y))

    return valid_intersections

def is_less_or_equal(value_a, value_b):
    return value_a < value_b or math.isclose(value_a, value_b, abs_tol=1e-9)

def is_greater_or_equal(value_a, value_b):
    return value_a > value_b or math.isclose(value_a, value_b, abs_tol=1e-9)

def set_minus_zero_to_zero(float_value):
    if math.isclose(float_value, 0.0, abs_tol=1e-9):
        return 0.0
    else:
        return float_value

def main_execution_loop():
    polygon_vertex_count, circle_radius_value = [int(token) for token in input().split()]
    polygon_vertex_list = []
    for _ in range(polygon_vertex_count):
        input_x, input_y = [int(token) for token in input().split()]
        polygon_vertex_list.append((input_x, input_y))
    computed_area = circle_polygon_intersection_area((0, 0, circle_radius_value), polygon_vertex_list)
    sanitized_area = set_minus_zero_to_zero(computed_area)
    print("{:.10f}".format(sanitized_area))

if __name__ == '__main__':
    main_execution_loop()