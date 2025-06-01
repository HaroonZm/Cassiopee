#!/usr/bin/python3

import array
from fractions import Fraction
import functools
import itertools
import math
import os
import sys


def main():
    
    number_of_elements, number_of_ranges = read_ints()
    
    element_values = read_ints()
    
    list_of_ranges = [(left_bound, right_bound) for left_bound, right_bound in [read_ints() for _ in range(number_of_ranges)]]
    
    maximum_value = solve_max_value_with_ranges(number_of_elements, number_of_ranges, element_values, list_of_ranges)
    
    print(maximum_value)


def solve_max_value_with_ranges(total_elements, total_ranges, values_array, ranges_array):
    
    # Sort ranges by their left bound
    ranges_array.sort()
    
    current_range_index = 0
    dynamic_programming = [0] * (total_elements + 1)
    
    active_range_counts = []
    active_range_start_points = []
    
    first_active_range_index = 0
    
    start_point_to_range_index = {}
    end_point_to_active_range_indices = {}
    
    for position in range(1, total_elements + 1):
        
        # Add ranges starting at the current position
        while current_range_index < len(ranges_array) and ranges_array[current_range_index][0] == position:
            
            left_bound, right_bound = ranges_array[current_range_index]
            
            if left_bound not in start_point_to_range_index:
                start_point_to_range_index[left_bound] = len(active_range_counts)
                active_range_counts.append(0)
                active_range_start_points.append(left_bound)
            
            active_range_counts[start_point_to_range_index[left_bound]] += 1
            
            if right_bound not in end_point_to_active_range_indices:
                end_point_to_active_range_indices[right_bound] = []
            
            end_point_to_active_range_indices[right_bound].append(start_point_to_range_index[left_bound])
            
            current_range_index += 1
        
        left_index_for_dp = position - 1
        if first_active_range_index < len(active_range_counts):
            left_index_for_dp = active_range_start_points[first_active_range_index] - 1
        
        dynamic_programming[position] = max(
            dynamic_programming[position - 1],
            dynamic_programming[left_index_for_dp] + values_array[position - 1]
        )
        
        # Decrease counts for ranges that end at the current position
        if position in end_point_to_active_range_indices:
            for range_index in end_point_to_active_range_indices[position]:
                active_range_counts[range_index] -= 1
        
        # Advance to the next active range that still has counts > 0
        while first_active_range_index < len(active_range_counts) and active_range_counts[first_active_range_index] == 0:
            first_active_range_index += 1
    
    return dynamic_programming[-1]


###############################################################################
# AUXILIARY FUNCTIONS

DEBUG = 'DEBUG' in os.environ


def inp():
    return sys.stdin.readline().rstrip()


def read_int():
    return int(inp())


def read_ints():
    return [int(element) for element in inp().split()]


def dprint(*args, sep=' ', end='\n'):
    if DEBUG:
        print(*args, sep=sep, end=end)


if __name__ == '__main__':
    
    main()