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

sys.setrecursionlimit(10**7)
CONSTANT_INFINITY = 10**20
CONSTANT_MODULUS = 10**9 + 7

def read_int_list():
    return list(map(int, input().split()))

def read_float_list():
    return list(map(float, input().split()))

def read_single_int():
    return int(input())

def read_str_list():
    return input().split()

def read_single_str():
    return input()

def solve():
    num_elements, segment_length = read_int_list()
    value_list = read_int_list()
    result_sum = 0
    current_index = 0
    while True:
        segment_min = segment_max = value_list[current_index % num_elements]
        for offset in range(1, segment_length):
            segment_value = value_list[(current_index + offset) % num_elements]
            if segment_min > segment_value:
                segment_min = segment_value
            elif segment_max < segment_value:
                segment_max = segment_value
        result_sum += segment_max - segment_min
        current_index += segment_length
        if current_index % num_elements == 0:
            break
    return result_sum

print(solve())