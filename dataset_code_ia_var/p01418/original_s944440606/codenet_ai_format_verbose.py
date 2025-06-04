import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time
import copy
import functools

sys.setrecursionlimit(10 ** 7)

INFINITY = 10 ** 20
EPSILON = 1.0 / 10 ** 10
MODULO = 10 ** 9 + 7

DIRECTION_4_NEIGHBORS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIRECTION_8_NEIGHBORS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def read_int_list():
    return [int(x) for x in sys.stdin.readline().split()]

def read_zero_based_int_list():
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def read_float_list():
    return [float(x) for x in sys.stdin.readline().split()]

def read_string_list():
    return sys.stdin.readline().split()

def read_single_int():
    return int(sys.stdin.readline())

def read_single_float():
    return float(sys.stdin.readline())

def read_single_string():
    return input()

def print_flush(output_to_print):
    print(output_to_print, flush=True)

def main():
    number_of_steps, right_boundary, left_boundary = read_int_list()
    probability = read_single_float()
    tolerance = read_single_float()
    target_value = read_single_float()

    def compute_probability(remaining_steps, current_right, current_left):
        if abs(current_right - target_value) <= tolerance and abs(target_value - current_left) <= tolerance:
            return 1
        if target_value - current_left > tolerance or current_right - target_value > tolerance:
            return 0
        if remaining_steps == 0:
            midpoint = (current_right + current_left) / 2
            if abs(target_value - midpoint) <= tolerance:
                return 1
            return 0

        midpoint = (current_right + current_left) / 2
        if midpoint >= target_value:
            return compute_probability(remaining_steps - 1, current_right, midpoint) * (1 - probability) + \
                   compute_probability(remaining_steps - 1, midpoint, current_left) * probability
        else:
            return compute_probability(remaining_steps - 1, current_right, midpoint) * probability + \
                   compute_probability(remaining_steps - 1, midpoint, current_left) * (1 - probability)

    final_probability = compute_probability(number_of_steps, right_boundary, left_boundary)

    return '{:0.9f}'.format(final_probability)

print(main())