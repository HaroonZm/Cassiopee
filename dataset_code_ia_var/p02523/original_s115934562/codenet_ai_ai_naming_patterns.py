from math import sqrt as math_sqrt, pow as math_pow

def calculate_distance(point1_x, point1_y, point2_x, point2_y):
    delta_x = point2_x - point1_x
    delta_y = point2_y - point1_y
    return math_sqrt(math_pow(delta_x, 2) + math_pow(delta_y, 2))

coordinate_1_x, coordinate_1_y, coordinate_2_x, coordinate_2_y = map(float, raw_input().split(' '))
print calculate_distance(coordinate_1_x, coordinate_1_y, coordinate_2_x, coordinate_2_y)