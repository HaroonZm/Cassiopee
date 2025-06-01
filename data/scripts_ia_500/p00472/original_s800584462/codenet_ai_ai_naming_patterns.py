#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""
#
# Author:   Noname
# URL:      https://github.com/pettan0818
# License:  MIT License
# Created: 木 11/ 9 19:01:14 2017

# Usage
#
"""
from itertools import accumulate

def input_data():
    number_of_inns, number_of_ryotei = [int(value) for value in input().split(" ")]
    inns_distances = []
    ryotei_steps = []
    for _ in range(number_of_inns - 1):
        inns_distances.append(int(input()))
    for _ in range(number_of_ryotei):
        ryotei_steps.append(int(input()))
    return inns_distances, ryotei_steps

def calculate_total_distance(distance_list, ryotei_step_list):
    """Calculate total travelled distance based on steps.

    >>> calculate_total_distance([2, 1, 1, 3, 2, 1], [2, -1, 3, 2, -3])
    18
    """
    accumulated_distances = [0] + list(accumulate(distance_list))
    accumulated_ryotei_indices = [0] + list(accumulate(ryotei_step_list))

    segment_distances = []
    for idx in range(1, len(accumulated_ryotei_indices)):
        start_index = accumulated_ryotei_indices[idx - 1]
        end_index = accumulated_ryotei_indices[idx]
        segment_distance = abs(accumulated_distances[end_index] - accumulated_distances[start_index])
        segment_distances.append(segment_distance)

    return sum(segment_distances)

if __name__ == '__main__':
    distances, ryotei_steps = input_data()
    print(calculate_total_distance(distances, ryotei_steps) % 100000)