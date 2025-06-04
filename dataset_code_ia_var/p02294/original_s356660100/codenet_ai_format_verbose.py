#!/usr/bin/env python

"""
input:
3
0 0 3 0 1 1 2 -1
0 0 3 0 3 1 3 -1
0 0 3 0 3 -2 5 0

output:
1
1
0
"""

import sys

MINIMUM_FLOAT_DIFFERENCE = 1e-9

def vector_cross_product(vector_a, vector_b):
    return vector_a.real * vector_b.imag - vector_a.imag * vector_b.real

def vector_dot_product(vector_a, vector_b):
    return vector_a.real * vector_b.real + vector_a.imag * vector_b.imag

def check_counter_clockwise_orientation(point_origin, point_first, point_second):
    vector_from_origin_to_first = point_first - point_origin
    vector_from_origin_to_second = point_second - point_origin

    cross_product_result = vector_cross_product(vector_from_origin_to_first, vector_from_origin_to_second)
    dot_product_result = vector_dot_product(vector_from_origin_to_first, vector_from_origin_to_second)

    if cross_product_result > MINIMUM_FLOAT_DIFFERENCE:
        orientation_flag = 1
    elif cross_product_result < -MINIMUM_FLOAT_DIFFERENCE:
        orientation_flag = -1
    elif dot_product_result < -MINIMUM_FLOAT_DIFFERENCE:
        orientation_flag = 2
    elif abs(vector_from_origin_to_first) < abs(vector_from_origin_to_second):
        orientation_flag = -2
    else:
        orientation_flag = 0
    return orientation_flag

def check_line_segments_intersection(list_of_lines):
    for coordinates_of_segment in list_of_lines:
        coordinates = tuple(map(int, coordinates_of_segment))
        point1, point2, point3, point4 = (x + y * 1j for x, y in zip(coordinates[::2], coordinates[1::2]))

        first_line_orientation = check_counter_clockwise_orientation(point1, point2, point3) * \
                                check_counter_clockwise_orientation(point1, point2, point4)
        second_line_orientation = check_counter_clockwise_orientation(point3, point4, point1) * \
                                 check_counter_clockwise_orientation(point3, point4, point2)

        do_segments_intersect = (first_line_orientation <= 0) and (second_line_orientation <= 0)

        if do_segments_intersect:
            print('1')
        else:
            print('0')

if __name__ == '__main__':
    input_lines_from_stdin = sys.stdin.readlines()
    number_of_test_cases = int(input_lines_from_stdin[0])
    iterable_lines_coordinates = map(lambda line: line.split(), input_lines_from_stdin[1:])

    check_line_segments_intersection(iterable_lines_coordinates)