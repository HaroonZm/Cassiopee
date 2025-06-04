from math import sqrt

def calculate_distance(point_x1, point_y1, point_x2, point_y2):
    return sqrt((point_x1 - point_x2) ** 2 + (point_y1 - point_y2) ** 2)

while True:
    point_count = int(raw_input())
    if point_count == 0:
        break

    position_x_list = [0 for idx_point in range(point_count)]
    position_y_list = [0 for idx_point in range(point_count)]
    velocity_list  = [0 for idx_point in range(point_count)]

    for idx_point in range(point_count):
        input_x, input_y, input_v = map(int, raw_input().split())
        position_x_list[idx_point] = input_x
        position_y_list[idx_point] = input_y
        velocity_list[idx_point]   = input_v

    centroid_x = 0.0
    centroid_y = 0.0
    delta_distance = 1000.0

    minimum_time = 100000.0
    while delta_distance > 0.1 ** 8:
        max_time_index_tuple = (0.0, 0)
        for idx_point in range(point_count):
            current_time = calculate_distance(
                centroid_x, centroid_y,
                position_x_list[idx_point], position_y_list[idx_point]
            ) / velocity_list[idx_point]
            max_time_index_tuple = max(
                max_time_index_tuple,
                (current_time, idx_point)
            )
        minimum_time = max_time_index_tuple[0]
        move_ratio = delta_distance / minimum_time
        centroid_x += move_ratio * (position_x_list[max_time_index_tuple[1]] - centroid_x)
        centroid_y += move_ratio * (position_y_list[max_time_index_tuple[1]] - centroid_y)
        delta_distance /= 1.01

    print "%.8f" % minimum_time