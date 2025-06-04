import sys
input_reader = sys.stdin.readline
output_writer = sys.stdout.write

def process_polygons():
    count_polygon_a, count_polygon_b = map(int, input_reader().split())
    if count_polygon_a == 0 and count_polygon_b == 0:
        return False
    polygon_a_points = [list(map(int, input_reader().split())) for idx_a in range(count_polygon_a)]
    polygon_b_points = [list(map(int, input_reader().split())) for idx_b in range(count_polygon_b)]
    coordinate_x_set = set()
    coordinate_x_set.update(point_x for point_x, point_y in polygon_a_points)
    coordinate_x_set.update(point_x for point_x, point_z in polygon_b_points)
    coordinate_x_list = list(coordinate_x_set)
    coordinate_x_list.sort()

    def calculate_area_at_x(current_x):
        polygon_a_y_max = -100
        polygon_a_y_min = 100
        for idx_a in range(count_polygon_a):
            prev_x_a, prev_y_a = polygon_a_points[idx_a - 1]
            curr_x_a, curr_y_a = polygon_a_points[idx_a]
            if prev_x_a <= current_x <= curr_x_a or curr_x_a <= current_x <= prev_x_a:
                if prev_x_a == curr_x_a:
                    polygon_a_y_max = max(polygon_a_y_max, max(curr_y_a, prev_y_a))
                    polygon_a_y_min = min(polygon_a_y_min, min(curr_y_a, prev_y_a))
                else:
                    interpolated_y = (current_x - prev_x_a) * (curr_y_a - prev_y_a) / (curr_x_a - prev_x_a) + prev_y_a
                    polygon_a_y_max = max(polygon_a_y_max, interpolated_y)
                    polygon_a_y_min = min(polygon_a_y_min, interpolated_y)
        if not polygon_a_y_min <= polygon_a_y_max:
            return 0
        polygon_b_z_max = -100
        polygon_b_z_min = 100
        for idx_b in range(count_polygon_b):
            prev_x_b, prev_z_b = polygon_b_points[idx_b - 1]
            curr_x_b, curr_z_b = polygon_b_points[idx_b]
            if prev_x_b <= current_x <= curr_x_b or curr_x_b <= current_x <= prev_x_b:
                if prev_x_b == curr_x_b:
                    polygon_b_z_max = max(polygon_b_z_max, max(curr_z_b, prev_z_b))
                    polygon_b_z_min = min(polygon_b_z_min, min(curr_z_b, prev_z_b))
                else:
                    interpolated_z = (current_x - prev_x_b) * (curr_z_b - prev_z_b) / (curr_x_b - prev_x_b) + prev_z_b
                    polygon_b_z_max = max(polygon_b_z_max, interpolated_z)
                    polygon_b_z_min = min(polygon_b_z_min, interpolated_z)
        if not polygon_b_z_min <= polygon_b_z_max:
            return 0
        return (polygon_b_z_max - polygon_b_z_min) * (polygon_a_y_max - polygon_a_y_min)

    total_area = 0
    num_x = len(coordinate_x_list)
    for idx_x in range(num_x - 1):
        x_start = coordinate_x_list[idx_x]
        x_end = coordinate_x_list[idx_x + 1]
        area_start = calculate_area_at_x(x_start)
        area_mid = calculate_area_at_x((x_start + x_end) / 2)
        area_end = calculate_area_at_x(x_end)
        if area_mid > 0:
            total_area += (x_end - x_start) * (area_start + area_end + 4 * area_mid) / 6
    output_writer("%.16f\n" % total_area)
    return True

while process_polygons():
    pass