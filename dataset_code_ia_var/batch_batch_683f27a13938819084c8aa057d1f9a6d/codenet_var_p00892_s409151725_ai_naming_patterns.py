import sys
system_input = sys.stdin.readline

def polygon_width(coord_x, coord_y, target_x):
    vertex_count = len(coord_x)
    lower_bound = float('inf')
    upper_bound = -float('inf')
    for idx in range(vertex_count):
        curr_x, curr_y = coord_x[idx], coord_y[idx]
        next_x, next_y = coord_x[(idx + 1) % vertex_count], coord_y[(idx + 1) % vertex_count]
        if (curr_x - target_x) * (next_x - target_x) <= 0 and curr_x != next_x:
            intersect_y = curr_y + (next_y - curr_y) * (target_x - curr_x) / (next_x - curr_x)
            lower_bound = min(lower_bound, intersect_y)
            upper_bound = max(upper_bound, intersect_y)
    return max(0, upper_bound - lower_bound)

while True:
    polygon1_vertex_count, polygon2_vertex_count = map(int, system_input().split())
    if polygon1_vertex_count == 0 and polygon2_vertex_count == 0:
        break
    polygon1_x = [0] * polygon1_vertex_count
    polygon1_y = [0] * polygon1_vertex_count
    polygon2_x = [0] * polygon2_vertex_count
    polygon2_y = [0] * polygon2_vertex_count
    for idx_p1 in range(polygon1_vertex_count):
        polygon1_x[idx_p1], polygon1_y[idx_p1] = map(int, system_input().split())
    for idx_p2 in range(polygon2_vertex_count):
        polygon2_x[idx_p2], polygon2_y[idx_p2] = map(int, system_input().split())
    polygon1_x_min = min(polygon1_x)
    polygon1_x_max = max(polygon1_x)
    polygon2_x_min = min(polygon2_x)
    polygon2_x_max = max(polygon2_x)
    combined_x_collection = polygon1_x + polygon2_x
    combined_x_collection.sort()
    total_area = 0
    for idx_x in range(len(combined_x_collection) - 1):
        point_a = combined_x_collection[idx_x]
        point_b = combined_x_collection[idx_x + 1]
        point_c = (point_a + point_b) / 2
        if (polygon1_x_min <= point_c <= polygon1_x_max) and (polygon2_x_min <= point_c <= polygon2_x_max):
            width_a = polygon_width(polygon1_x, polygon1_y, point_a) * polygon_width(polygon2_x, polygon2_y, point_a)
            width_b = polygon_width(polygon1_x, polygon1_y, point_b) * polygon_width(polygon2_x, polygon2_y, point_b)
            width_c = polygon_width(polygon1_x, polygon1_y, point_c) * polygon_width(polygon2_x, polygon2_y, point_c)
            total_area += (point_b - point_a) / 6 * (width_a + 4 * width_c + width_b)
    print(total_area)