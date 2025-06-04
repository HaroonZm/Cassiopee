#!/usr/bin/env python

import sys

# Ignore the first input line (possibly the number of test cases)
input()

for input_line in sys.stdin:

    circle_data = list(map(float, input_line.split()))

    x_center_a = circle_data[0]
    y_center_a = circle_data[1]
    radius_a = circle_data[2]
    x_center_b = circle_data[3]
    y_center_b = circle_data[4]
    radius_b = circle_data[5]

    distance_between_centers = ((x_center_a - x_center_b) ** 2 + (y_center_a - y_center_b) ** 2) ** 0.5

    sum_of_radii = radius_a + radius_b

    if distance_between_centers > sum_of_radii:

        print(0)

    elif distance_between_centers + radius_b < radius_a:

        print(2)

    elif distance_between_centers + radius_a < radius_b:

        print(-2)

    else:

        print(1)