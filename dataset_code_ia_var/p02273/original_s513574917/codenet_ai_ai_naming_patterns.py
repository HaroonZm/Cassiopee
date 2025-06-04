#!/usr/bin/env python

import sys
import math

sys.setrecursionlimit(10000000)

def koch_curve_step(iteration_level, start_x, start_y, end_x, end_y):
    if iteration_level == 0:
        print(end_x, end_y)
        return
    delta_x = end_x - start_x
    delta_y = end_y - start_y

    point1_x = start_x + delta_x / 3.0
    point1_y = start_y + delta_y / 3.0

    point3_x = end_x - delta_x / 3.0
    point3_y = end_y - delta_y / 3.0

    rotated_x = delta_x / 2.0 - math.sqrt(3) * delta_y / 2.0
    rotated_y = math.sqrt(3) * delta_x / 2.0 + delta_y / 2.0

    point2_x = point1_x + rotated_x / 3.0
    point2_y = point1_y + rotated_y / 3.0

    koch_curve_step(iteration_level - 1, start_x, start_y, point1_x, point1_y)
    koch_curve_step(iteration_level - 1, point1_x, point1_y, point2_x, point2_y)
    koch_curve_step(iteration_level - 1, point2_x, point2_y, point3_x, point3_y)
    koch_curve_step(iteration_level - 1, point3_x, point3_y, end_x, end_y)

def main():
    recursion_depth = int(input())
    print(0.0, 0.0)
    koch_curve_step(recursion_depth, 0.0, 0.0, 100.0, 0.0)

if __name__ == "__main__":
    main()