from math import atan2 as calc_atan2, degrees as to_degrees
from itertools import permutations as generate_permutations

point_count = int(input())
point_list = [list(map(int, input().split())) for _ in range(point_count)]

min_total_angle = float("inf")

for permuted_points in generate_permutations(point_list):
    current_x, current_y = 0, 0
    current_angle = 0
    accumulated_angle = 0

    for target_x, target_y in list(permuted_points) + [[0, 0]]:
        direction_angle = to_degrees(calc_atan2(target_y - current_y, target_x - current_x))
        angle_diff = current_angle - direction_angle
        if angle_diff < 0:
            angle_diff += 360
        if angle_diff > 180:
            angle_diff = 360 - angle_diff
        accumulated_angle += angle_diff

        current_x, current_y = target_x, target_y
        current_angle = direction_angle

    if accumulated_angle < min_total_angle:
        min_total_angle = accumulated_angle

print(min_total_angle)