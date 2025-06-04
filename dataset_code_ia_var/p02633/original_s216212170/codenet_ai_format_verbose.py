from math import gcd

input_angle_degrees = int(input())

greatest_common_divisor = gcd(360, input_angle_degrees)

minimum_common_multiple = (360 * input_angle_degrees) // greatest_common_divisor

number_of_polygons_sides = minimum_common_multiple // input_angle_degrees

print(number_of_polygons_sides)