def compute_width(x_coords, y_coords, num_points, eval_x):
    lower_bound = float("inf")
    upper_bound = -float("inf")

    for idx in range(num_points):
        x_start = x_coords[idx]
        y_start = y_coords[idx]
        x_end = x_coords[(idx + 1) % num_points]
        y_end = y_coords[(idx + 1) % num_points]

        if (x_start - eval_x) * (x_end - eval_x) <= 0 and x_start != x_end:
            intersect_y = y_start + (y_end - y_start) * (eval_x - x_start) / (x_end - x_start)
            lower_bound = min(lower_bound, intersect_y)
            upper_bound = max(upper_bound, intersect_y)

    return max(0, upper_bound - lower_bound)

if __name__ == '__main__':
    while True:
        poly1_vertex_count, poly2_vertex_count = map(int, input().split())
        if poly1_vertex_count == 0 and poly2_vertex_count == 0:
            break

        poly1_x_list = []
        poly1_y_list = []
        poly2_x_list = []
        poly2_y_list = []
        for idx_poly1 in range(poly1_vertex_count):
            vertex_x, vertex_y = map(int, input().split())
            poly1_x_list.append(vertex_x)
            poly1_y_list.append(vertex_y)

        for idx_poly2 in range(poly2_vertex_count):
            vertex_x, vertex_y = map(int, input().split())
            poly2_x_list.append(vertex_x)
            poly2_y_list.append(vertex_y)

        poly1_x_min = min(poly1_x_list)
        poly1_x_max = max(poly1_x_list)
        poly2_x_min = min(poly2_x_list)
        poly2_x_max = max(poly2_x_list)

        merge_x_values = sorted(poly1_x_list + poly2_x_list)
        total_result = 0.0
        for segment_idx in range(len(merge_x_values) - 1):
            seg_start_x = merge_x_values[segment_idx]
            seg_end_x = merge_x_values[segment_idx + 1]
            seg_mid_x = (seg_start_x + seg_end_x) / 2

            if (poly1_x_min <= seg_mid_x <= poly1_x_max) and (poly2_x_min <= seg_mid_x <= poly2_x_max):
                area_start = compute_width(poly1_x_list, poly1_y_list, poly1_vertex_count, seg_start_x) * compute_width(poly2_x_list, poly2_y_list, poly2_vertex_count, seg_start_x)
                area_end = compute_width(poly1_x_list, poly1_y_list, poly1_vertex_count, seg_end_x) * compute_width(poly2_x_list, poly2_y_list, poly2_vertex_count, seg_end_x)
                area_mid = compute_width(poly1_x_list, poly1_y_list, poly1_vertex_count, seg_mid_x) * compute_width(poly2_x_list, poly2_y_list, poly2_vertex_count, seg_mid_x)
                total_result += ((seg_end_x - seg_start_x) / 6) * (area_start + 4 * area_mid + area_end)

        print(total_result)