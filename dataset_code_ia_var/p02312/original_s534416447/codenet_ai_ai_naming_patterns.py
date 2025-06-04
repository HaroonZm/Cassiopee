num_vertices, radius = map(int, raw_input().split())
polygon_points = [map(int, raw_input().split()) for point_index in xrange(num_vertices)]

from math import sqrt as math_sqrt, atan2 as math_atan2

def compute_circle_segment_intersection(circle_center_x, circle_center_y, circle_radius, seg_start_x, seg_start_y, seg_end_x, seg_end_y):
    delta_x = seg_end_x - seg_start_x
    delta_y = seg_end_y - seg_start_y
    origin_to_start_x = seg_start_x - circle_center_x
    origin_to_start_y = seg_start_y - circle_center_y
    quadratic_a = delta_x ** 2 + delta_y ** 2
    quadratic_b = delta_x * origin_to_start_x + delta_y * origin_to_start_y
    quadratic_c = origin_to_start_x ** 2 + origin_to_start_y ** 2 - circle_radius ** 2
    discriminant = quadratic_b ** 2 - quadratic_a * quadratic_c
    intersection_points = []
    if discriminant > 0:
        sqrt_discriminant = math_sqrt(discriminant)
        if 0 < -quadratic_b - sqrt_discriminant < quadratic_a:
            intersection_scalar_1 = (-quadratic_b - sqrt_discriminant) / quadratic_a
            intersection_points.append((seg_start_x + delta_x * intersection_scalar_1, seg_start_y + delta_y * intersection_scalar_1))
        if 0 < -quadratic_b + sqrt_discriminant < quadratic_a:
            intersection_scalar_2 = (-quadratic_b + sqrt_discriminant) / quadratic_a
            intersection_points.append((seg_start_x + delta_x * intersection_scalar_2, seg_start_y + delta_y * intersection_scalar_2))
    elif discriminant == 0:
        if 0 < -quadratic_b < quadratic_a:
            intersection_scalar = -quadratic_b / float(quadratic_a)
            intersection_points.append((seg_start_x + delta_x * intersection_scalar, seg_start_y + delta_y * intersection_scalar))
    return intersection_points

def compute_area_contribution(segment_start_x, segment_start_y, segment_end_x, segment_end_y, circle_radius_squared):
    if segment_start_x ** 2 + segment_start_y ** 2 - circle_radius_squared <= 1e-8 and segment_end_x ** 2 + segment_end_y ** 2 - circle_radius_squared <= 1e-8:
        return (segment_start_x * segment_end_y - segment_end_x * segment_start_y) / 2.0
    angle_theta = math_atan2(segment_start_x * segment_end_y - segment_end_x * segment_start_y, segment_start_x * segment_end_x + segment_start_y * segment_end_y)
    return angle_theta * circle_radius_squared / 2.0

circle_radius_squared = radius ** 2
computed_area = 0
for vertex_index in xrange(num_vertices):
    prev_vertex_x, prev_vertex_y = polygon_points[vertex_index - 1]
    curr_vertex_x, curr_vertex_y = polygon_points[vertex_index]

    segment_intersections = compute_circle_segment_intersection(0, 0, radius, prev_vertex_x, prev_vertex_y, curr_vertex_x, curr_vertex_y)
    area_segment_start_x = prev_vertex_x
    area_segment_start_y = prev_vertex_y
    for intersection_x, intersection_y in segment_intersections:
        computed_area += compute_area_contribution(area_segment_start_x, area_segment_start_y, intersection_x, intersection_y, circle_radius_squared)
        area_segment_start_x = intersection_x
        area_segment_start_y = intersection_y
    computed_area += compute_area_contribution(area_segment_start_x, area_segment_start_y, curr_vertex_x, curr_vertex_y, circle_radius_squared)
print "%.08f" % computed_area