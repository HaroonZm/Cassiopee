from math import pi, cos, sin, atan2

while True:
    point_count = int(input())
    if point_count == -1:
        break
    segment_count = point_count - 1
    current_angle_rad = 0.0
    coordinate_x = 1.0
    coordinate_y = 0.0
    for _ in range(segment_count):
        current_angle_rad += pi / 2
        coordinate_x += cos(current_angle_rad)
        coordinate_y += sin(current_angle_rad)
        current_angle_rad = atan2(coordinate_y, coordinate_x)
    print("{:.2f}".format(coordinate_x))
    print("{:.2f}".format(coordinate_y))