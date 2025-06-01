#!/usr/bin/python3

import array
from fractions import Fraction
import functools
import itertools
import math
import os
import sys

def main_entry_point():
    total_items, total_containers = read_multiple_ints()
    items_list = [(size, value) for size, value in [read_multiple_ints() for _ in range(total_items)]]
    containers_list = [read_single_int() for _ in range(total_containers)]
    print(compute_max_allocation(total_items, total_containers, items_list, containers_list))

def compute_max_allocation(total_items, total_containers, items_data, container_sizes):
    items_data.sort(key=lambda item: (-item[1], -item[0]))
    container_sizes.sort(reverse=True)
    container_index = 0
    allocated_count = 0
    for item_index in range(total_items):
        if container_index == total_containers:
            break
        item_size = items_data[item_index][0]
        if container_sizes[container_index] >= item_size:
            container_index += 1
            allocated_count += 1
    return allocated_count

###############################################################################
# AUXILIARY FUNCTIONS

DEBUG_MODE = 'DEBUG' in os.environ

def input_line():
    return sys.stdin.readline().rstrip()

def read_single_int():
    return int(input_line())

def read_multiple_ints():
    return [int(element) for element in input_line().split()]

def debug_print(*args, sep=' ', end='\n'):
    if DEBUG_MODE:
        print(*args, sep=sep, end=end)

if __name__ == '__main__':
    main_entry_point()