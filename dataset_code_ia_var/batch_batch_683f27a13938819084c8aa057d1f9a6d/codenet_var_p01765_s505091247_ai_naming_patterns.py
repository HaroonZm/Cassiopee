import sys

input_point_count_1 = int(sys.stdin.readline())
point_list_1 = [[int(coord) for coord in sys.stdin.readline().split()] for _ in range(input_point_count_1)]
point_list_1.insert(0, [0, 0])
point_list_1.append([1000, 0])

input_point_count_2 = int(sys.stdin.readline())
point_list_2 = [[int(coord) for coord in sys.stdin.readline().split()] for _ in range(input_point_count_2)]
point_list_2.insert(0, [0, 1000])
point_list_2.append([1000, 1000])

min_distance_squared = float("inf")

for px1, py1 in point_list_1:
    for px2, py2 in point_list_2:
        current_distance_squared = (px1 - px2) ** 2 + (py1 - py2) ** 2
        if current_distance_squared < min_distance_squared:
            min_distance_squared = current_distance_squared

for px, py in point_list_1:
    for idx in range(input_point_count_2 + 1):
        seg_start_x, seg_start_y = point_list_2[idx]
        seg_end_x, seg_end_y = point_list_2[idx + 1]
        seg_vec_x = seg_end_x - seg_start_x
        seg_vec_y = seg_end_y - seg_start_y
        delta_a = seg_vec_y
        delta_b = seg_start_x - seg_end_x
        product_1 = (delta_b * (seg_end_x - px) - delta_a * (seg_end_y - py))
        product_2 = (delta_b * (seg_start_x - px) - delta_a * (seg_start_y - py))
        if product_1 * product_2 < 0:
            line_c = -delta_a * seg_start_x - delta_b * seg_start_y
            numer = (delta_a * px + delta_b * py + line_c) ** 2
            denom = delta_a ** 2 + delta_b ** 2
            distance_squared = numer / denom
            if distance_squared < min_distance_squared:
                min_distance_squared = distance_squared

for px, py in point_list_2:
    for idx in range(input_point_count_1 + 1):
        seg_start_x, seg_start_y = point_list_1[idx]
        seg_end_x, seg_end_y = point_list_1[idx + 1]
        seg_vec_x = seg_end_x - seg_start_x
        seg_vec_y = seg_end_y - seg_start_y
        delta_a = seg_vec_y
        delta_b = seg_start_x - seg_end_x
        product_1 = (delta_b * (seg_end_x - px) - delta_a * (seg_end_y - py))
        product_2 = (delta_b * (seg_start_x - px) - delta_a * (seg_start_y - py))
        if product_1 * product_2 < 0:
            line_c = -delta_a * seg_start_x - delta_b * seg_start_y
            numer = (delta_a * px + delta_b * py + line_c) ** 2
            denom = delta_a ** 2 + delta_b ** 2
            distance_squared = numer / denom
            if distance_squared < min_distance_squared:
                min_distance_squared = distance_squared

print(min_distance_squared ** 0.5)