import sys
import math
import bisect
import random
from collections import defaultdict
from heapq import heappush, heappop

MOD_CONST = 1000000007

def read_int_list():
    return list(map(int, sys.stdin.readline().split()))

def read_int():
    return int(sys.stdin.readline())

def read_str_list_of_lists():
    return list(map(list, sys.stdin.readline().split()))

def read_str_list():
    return list(sys.stdin.readline())[:-1]

def read_n_ints(count):
    result_list = [None for _ in range(count)]
    for idx in range(count):
        result_list[idx] = read_int()
    return result_list

def read_n_int_lists(count):
    result_list = [None for _ in range(count)]
    for idx in range(count):
        result_list[idx] = read_int_list()
    return result_list

def read_n_str_lists(count):
    result_list = [None for _ in range(count)]
    for idx in range(count):
        result_list[idx] = read_str_list()
    return result_list

def read_n_str_list_of_lists(count):
    result_list = [None for _ in range(count)]
    for idx in range(count):
        result_list[idx] = read_n_str_lists()
    return result_list

# Section A
input_n, input_m = read_int_list()
input_list_a = read_int_list()
input_list_b = read_int_list()

union_set = list(set(input_list_a) | set(input_list_b))
intersection_set = list(set(input_list_a) & set(input_list_b))
union_set.sort()
intersection_set.sort()

print(len(intersection_set), len(union_set))
for value in intersection_set:
    print(value)
for value in union_set:
    print(value)

# Section B

# Section C

# Section D

# Section E

# Section F

# Section G

# Section H

# Section I

# Section J

# Section K

# Section L

# Section M

# Section N

# Section O

# Section P

# Section Q

# Section R

# Section S

# Section T