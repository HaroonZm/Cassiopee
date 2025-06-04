import sys
import collections as collections_alias
import bisect as bisect_alias
from fractions import gcd as fractions_gcd
from functools import reduce as functools_reduce

sys.setrecursionlimit(100000)
CONSTANT_MAX_VALUE = sys.maxsize

def input_int_list():
    return list(map(int, input().split()))

def input_int_map():
    return map(int, input().split())

def input_single_int():
    return int(input())

def run_length_encode(sequence):
    encoded = []
    current_element = sequence[0]
    count = 1
    for index in range(len(sequence) - 1):
        if current_element == sequence[index + 1]:
            encoded.append([current_element, count])
            current_element = sequence[index + 1]
            count = 1
        else:
            count += 1
    encoded.append([current_element, count])
    return encoded

def join_list_with_spaces(lst):
    return " ".join(map(str, lst))

def max_of_nested_list(nested_list):
    return max(map(max, nested_list))

def get_gcd(*args):
    return functools_reduce(fractions_gcd, args)

def get_gcd_from_list(int_list):
    return functools_reduce(fractions_gcd, int_list)

def lcm_pair(a, b):
    return (a * b) // fractions_gcd(a, b)

def get_lcm(*args):
    return functools_reduce(lcm_pair, args, 1)

def get_lcm_from_list(int_list):
    return functools_reduce(lcm_pair, int_list, 1)

input_count = input_single_int()
input_values = input_int_list()

print(get_lcm_from_list(input_values))