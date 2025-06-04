from math import sqrt
coord_x_start, coord_y_start, coord_x_end, coord_y_end = map(float, raw_input().split())
delta_x = coord_x_start - coord_x_end
delta_y = coord_y_start - coord_y_end
distance_result = sqrt(delta_x ** 2 + delta_y ** 2)
print(distance_result)