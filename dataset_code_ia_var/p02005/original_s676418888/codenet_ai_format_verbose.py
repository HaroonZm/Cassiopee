from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
from functools import reduce
import sys
import math
import bisect
import random

def read_integer():
    return int(sys.stdin.readline())

def read_float():
    return float(sys.stdin.readline())

def read_string():
    return input()

def read_integer_list():
    return list(map(int, sys.stdin.readline().split()))

def read_zero_based_integer_list():
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def read_float_list():
    return list(map(float, sys.stdin.readline().split()))

def read_string_list():
    return sys.stdin.readline().split()

def read_matrix_of_strings(row_count):
    return [list(sys.stdin.readline())[:-1] for _ in range(row_count)]

def read_integer_rows(row_count):
    return [int(sys.stdin.readline()) for _ in range(row_count)]

def read_matrix_of_integers(row_count):
    return [list(map(int, sys.stdin.readline().split())) for _ in range(row_count)]

def read_matrix_of_lists(row_count):
    return [list(map(list, sys.stdin.readline().split())) for _ in range(row_count)]

def compute_gcd(a, b):
    return compute_gcd(b, a % b) if (a % b) else b

def compute_lcm(a, b):
    return a * b // compute_gcd(a, b)

def gcd_of_list(*numbers):
    return reduce(compute_gcd, numbers)

def lcm_of_list(*numbers):
    return reduce(compute_lcm, numbers)

sys.setrecursionlimit(1000000)

INFINITY = float('inf')
MODULO = 1000000007

directions_4_possibilities = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]

directions_8_possibilities = [
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1)
]

def solve(item_dictionary):
    return

number_of_items = read_integer()

item_dictionary = defaultdict(list)

for _ in range(number_of_items):
    category, value = read_string_list()
    value = int(value)
    item_dictionary[category].append(value)

for category_key in item_dictionary.keys():
    item_dictionary[category_key].sort()

number_of_order_items = read_integer()

order_sequence = []

for _ in range(number_of_order_items):
    order_item = read_string_list()[0]
    order_sequence.append(order_item)

order_possible = True
previous_selected_value = MODULO

if number_of_items >= number_of_order_items:
    for current_category in reversed(order_sequence):
        while True:
            if len(item_dictionary[current_category]) == 0:
                order_possible = False
                break

            current_value = item_dictionary[current_category].pop(-1)

            if current_value >= previous_selected_value:
                continue
            else:
                previous_selected_value = current_value
                break
else:
    order_possible = False

print("Yes" if order_possible else "No")