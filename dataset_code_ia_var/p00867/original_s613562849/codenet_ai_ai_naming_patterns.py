import sys
input_reader = sys.stdin.readline
output_writer = sys.stdout.write

def calc_dot_product(reference_point, point_a, point_b):
    ref_x, ref_y = reference_point
    a_x, a_y = point_a
    b_x, b_y = point_b
    return (a_x - ref_x) * (b_x - ref_x) + (a_y - ref_y) * (b_y - ref_y)

def calc_cross_product(reference_point, point_a, point_b):
    ref_x, ref_y = reference_point
    a_x, a_y = point_a
    b_x, b_y = point_b
    return (a_x - ref_x) * (b_y - ref_y) - (b_x - ref_x) * (a_y - ref_y)

def calc_squared_distance(point_a, point_b):
    a_x, a_y = point_a
    b_x, b_y = point_b
    return (a_x - b_x) ** 2 + (a_y - b_y) ** 2

def check_segment_intersection(seg1_start, seg1_end, seg2_start, seg2_end):
    cross1 = calc_cross_product(seg1_start, seg1_end, seg2_start)
    cross2 = calc_cross_product(seg1_start, seg1_end, seg2_end)
    cross3_val = calc_cross_product(seg2_start, seg2_end, seg1_start)
    cross4 = calc_cross_product(seg2_start, seg2_end, seg1_end)
    if cross1 == cross2 == 0:
        dot1 = calc_dot_product(seg1_start, seg1_end, seg2_start)
        dot2 = calc_dot_product(seg1_start, seg1_end, seg2_end)
        if not dot1 < dot2:
            dot1, dot2 = dot2, dot1
        return dot1 <= calc_squared_distance(seg1_start, seg1_end) and 0 <= dot2
    return cross1 * cross2 <= 0 and cross3_val * cross4 <= 0

def main_solution():
    num_segments = int(input_reader())
    if num_segments == 0:
        return False
    segment_list = []
    for segment_index in range(num_segments):
        x1, y1, x2, y2 = map(int, input_reader().split())
        segment_list.append(((x1, y1), (x2, y2)))
    parent_list = list(range(num_segments))
    def find_root(idx):
        if idx == parent_list[idx]:
            return idx
        parent_list[idx] = parent_id = find_root(parent_list[idx])
        return parent_id
    def merge_components(idx1, idx2):
        root1 = find_root(idx1)
        root2 = find_root(idx2)
        if root1 < root2:
            parent_list[root2] = root1
        else:
            parent_list[root1] = root2
    for i in range(num_segments):
        segment_i_start, segment_i_end = segment_list[i]
        for j in range(i):
            segment_j_start, segment_j_end = segment_list[j]
            if check_segment_intersection(segment_i_start, segment_i_end, segment_j_start, segment_j_end):
                merge_components(i, j)
    component_count = 0
    component_segments = []
    label_list = [0] * num_segments
    for i in range(num_segments):
        if find_root(i) == i:
            component_segments.append([segment_list[i]])
            label_list[i] = component_count
            component_count += 1
            continue
        root_idx = label_list[find_root(i)]
        component_segments[root_idx].append(segment_list[i])
    result_array = [0] * 10
    for component in component_segments:
        if len(component) == 1:
            result_array[1] += 1
            continue
        endpoint_degree = {}
        for seg_start, seg_end in component:
            endpoint_degree[seg_start] = endpoint_degree.get(seg_start, 0) + 1
            endpoint_degree[seg_end] = endpoint_degree.get(seg_end, 0) + 1
        if len(component) == 5:
            degree_count = {}
            for seg_start, seg_end in component:
                degree_start, degree_end = endpoint_degree[seg_start], endpoint_degree[seg_end]
                degree_key = (degree_start, degree_end) if degree_start < degree_end else (degree_end, degree_start)
                degree_count[degree_key] = degree_count.get(degree_key, 0) + 1
            if (1, 1) in degree_count:
                result_array[8] += 1
            else:
                endpoint_pairs = []
                for seg_start, seg_end in component:
                    if endpoint_degree[seg_start] == 1:
                        endpoint_pairs.append((seg_start, seg_end))
                    if endpoint_degree[seg_end] == 1:
                        endpoint_pairs.append((seg_end, seg_start))
                (first_start, first_end), (second_start, second_end) = endpoint_pairs
                for seg in component:
                    ref_start, ref_end = seg
                    if endpoint_degree[ref_start] != 2 or endpoint_degree[ref_end] != 2:
                        continue
                    if (check_segment_intersection(first_start, first_end, ref_start, ref_end) and first_end not in seg) or \
                       (check_segment_intersection(second_start, second_end, ref_start, ref_end) and second_end not in seg):
                        result_array[6] += 1
                        break
                else:
                    if calc_cross_product(first_start, first_end, second_end) < 0:
                        result_array[2] += 1
                    else:
                        result_array[5] += 1
            continue
        if len(component) == 3:
            if len(endpoint_degree) == 4:
                result_array[7] += 1
            else:
                result_array[4] += 1
        elif len(component) == 4:
            if len(endpoint_degree) == 4:
                result_array[0] += 1
            elif len(endpoint_degree) == 5:
                result_array[9] += 1
            else:
                result_array[3] += 1
    output_writer(" ".join(map(str, result_array)))
    output_writer("\n")
    return True

while main_solution():
    ...