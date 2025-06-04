import sys

input_stream = sys.stdin
output_stream = sys.stdout

TOLERANCE_EPSILON = 1e-9

def get_line_intersection(point_a_start, point_a_end, point_b_start, point_b_end):
    ax0, ay0 = point_a_start
    ax1, ay1 = point_a_end
    bx0, by0 = point_b_start
    bx1, by1 = point_b_end

    a_dx = ax1 - ax0
    a_dy = ay1 - ay0
    b_dx = bx1 - bx0
    b_dy = by1 - by0

    numerator = (ay0 - by0) * b_dx - (ax0 - bx0) * b_dy
    denominator = a_dx * b_dy - a_dy * b_dx

    if -TOLERANCE_EPSILON < denominator < TOLERANCE_EPSILON:
        return None

    intersection_x = ax0 + numerator * a_dx / denominator
    intersection_y = ay0 + numerator * a_dy / denominator
    return (intersection_x, intersection_y)

def get_angle_bisectors(line1_start, line1_end, line2_start, line2_end):
    l1_x0, l1_y0 = line1_start
    l1_x1, l1_y1 = line1_end
    l2_x0, l2_y0 = line2_start
    l2_x1, l2_y1 = line2_end

    l1_dx = l1_x1 - l1_x0
    l1_dy = l1_y1 - l1_y0
    l2_dx = l2_x1 - l2_x0
    l2_dy = l2_y1 - l2_y0

    intersection_point = get_line_intersection(line1_start, line1_end, line2_start, line2_end)
    if intersection_point is None:
        return None

    ix, iy = intersection_point

    l1_length = (l1_dx ** 2 + l1_dy ** 2) ** 0.5
    l2_length = (l2_dx ** 2 + l2_dy ** 2) ** 0.5

    bisector_1_end = (ix + (l1_dx * l2_length + l2_dx * l1_length), iy + (l1_dy * l2_length + l2_dy * l1_length))
    bisector_2_end = (ix + (l1_dx * l2_length - l2_dx * l1_length), iy + (l1_dy * l2_length - l2_dy * l1_length))

    return [((ix, iy), bisector_1_end), ((ix, iy), bisector_2_end)]

def calculate_point_line_distance(line_start, line_end, point):
    px, py = point
    lx0, ly0 = line_start
    lx1, ly1 = line_end

    line_dx = lx1 - lx0
    line_dy = ly1 - ly0
    line_length_squared = line_dx ** 2 + line_dy ** 2

    value = (px - lx0) * line_dy - (py - ly0) * line_dx
    return abs(value / (line_length_squared ** 0.5))

def point_equidistant_from_lines(line_segments, query_point):
    distances = [calculate_point_line_distance(seg_start, seg_end, query_point) for seg_start, seg_end in line_segments]
    first_distance = distances[0]
    for dist in distances:
        if abs(first_distance - dist) >= TOLERANCE_EPSILON:
            return False
    return True

def main_process():
    while True:
        try:
            num_lines = int(input_stream.readline())
        except Exception:
            break
        if num_lines == 0:
            return
        segment_list = []
        for _ in range(num_lines):
            coords = list(map(int, input_stream.readline().split()))
            segment_list.append(((coords[0], coords[1]), (coords[2], coords[3])))
        if num_lines <= 2:
            output_stream.write("Many\n")
            continue

        bisector_collection = []
        found = False
        for idx_i in range(num_lines):
            seg_i_start, seg_i_end = segment_list[idx_i]
            for idx_j in range(idx_i):
                seg_j_start, seg_j_end = segment_list[idx_j]
                bisectors = get_angle_bisectors(seg_i_start, seg_i_end, seg_j_start, seg_j_end)
                if bisectors is None:
                    continue
                bisector_collection.append(bisectors)
                if len(bisector_collection) > 1:
                    found = True
                    break
            if found:
                break

        if len(bisector_collection) < 2:
            output_stream.write("None\n")
            continue

        candidate_points = []
        bisectors_a, bisectors_b = bisector_collection[:2]
        for a_start, a_end in bisectors_a:
            for b_start, b_end in bisectors_b:
                intersection = get_line_intersection(a_start, a_end, b_start, b_end)
                if intersection is None:
                    continue
                if point_equidistant_from_lines(segment_list, intersection):
                    ix, iy = intersection
                    duplicate = False
                    for ox, oy in candidate_points:
                        if abs(ix - ox) < TOLERANCE_EPSILON and abs(iy - oy) < TOLERANCE_EPSILON:
                            duplicate = True
                            break
                    if not duplicate:
                        candidate_points.append(intersection)

        if not candidate_points:
            output_stream.write("None\n")
        elif len(candidate_points) > 1:
            output_stream.write("Many\n")
        else:
            output_stream.write("%.16f %.16f\n" % candidate_points[0])

main_process()