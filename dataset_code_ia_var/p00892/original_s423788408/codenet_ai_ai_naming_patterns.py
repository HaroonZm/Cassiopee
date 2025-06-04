def compute_vertical_width(polygon_x, polygon_y, x_coord):
    num_vertices = len(polygon_x)
    min_y_intersection, max_y_intersection = float('inf'), -float('inf')
    for vertex_idx in range(num_vertices):
        x_start, y_start = polygon_x[vertex_idx], polygon_y[vertex_idx]
        x_end, y_end = polygon_x[(vertex_idx + 1) % num_vertices], polygon_y[(vertex_idx + 1) % num_vertices]
        if (x_start - x_coord) * (x_end - x_coord) <= 0 and x_start != x_end:
            y_intersect = y_start + (y_end - y_start) * (x_coord - x_start) / (x_end - x_start)
            min_y_intersection = min(min_y_intersection, y_intersect)
            max_y_intersection = max(max_y_intersection, y_intersect)
    return max(0, max_y_intersection - min_y_intersection)

while True:
    polygon1_vertex_count, polygon2_vertex_count = map(int, input().split())
    if not (polygon1_vertex_count and polygon2_vertex_count):
        break
    polygon1_x = [0] * polygon1_vertex_count
    polygon1_y = [0] * polygon1_vertex_count
    polygon2_x = [0] * polygon2_vertex_count
    polygon2_y = [0] * polygon2_vertex_count
    all_x_coords = [0] * (polygon1_vertex_count + polygon2_vertex_count)
    for idx in range(polygon1_vertex_count):
        polygon1_x[idx], polygon1_y[idx] = map(int, input().split())
    for idx in range(polygon2_vertex_count):
        polygon2_x[idx], polygon2_y[idx] = map(int, input().split())
    all_x_coords = polygon1_x + polygon2_x
    all_x_coords.sort()
    min_x1, max_x1 = min(polygon1_x), max(polygon1_x)
    min_x2, max_x2 = min(polygon2_x), max(polygon2_x)
    total_area = 0
    for i in range(len(all_x_coords) - 1):
        left_x = all_x_coords[i]
        right_x = all_x_coords[i + 1]
        middle_x = (left_x + right_x) / 2
        if min_x1 <= middle_x <= max_x1 and min_x2 <= middle_x <= max_x2:
            left_area = compute_vertical_width(polygon1_x, polygon1_y, left_x) * compute_vertical_width(polygon2_x, polygon2_y, left_x)
            right_area = compute_vertical_width(polygon1_x, polygon1_y, right_x) * compute_vertical_width(polygon2_x, polygon2_y, right_x)
            middle_area = compute_vertical_width(polygon1_x, polygon1_y, middle_x) * compute_vertical_width(polygon2_x, polygon2_y, middle_x)
            total_area += (right_x - left_x) / 6 * (left_area + 4 * middle_area + right_area)
    print('%.10f' % total_area)