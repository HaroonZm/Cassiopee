import sys
import random
from collections import defaultdict, deque, Counter
from decimal import Decimal
import heapq
import math
from fractions import gcd
import string
import copy
from itertools import permutations
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(1000000000)
MODULUS = 10 ** 9 + 7

def read_string_from_input():
    return sys.stdin.readline().rstrip()

def read_single_integer_from_input():
    return int(read_string_from_input())

def read_two_integers_from_input():
    integer_1, integer_2 = map(int, read_string_from_input().split())
    return integer_1, integer_2

def read_list_of_integers_from_input():
    return list(map(int, read_string_from_input().split()))

def read_multiple_integers_from_input(number_of_integers):
    return [int(read_string_from_input()) for _ in range(number_of_integers)]

def generate_random_integer_in_range(min_value, max_value):
    return random.randint(min_value, max_value)

def generate_random_integer_list(min_value, max_value, list_length):
    return [random.randint(min_value, max_value) for _ in range(list_length)]

def generate_unique_random_integers_list(min_value, max_value, desired_length):
    unique_random_integers = []
    while len(unique_random_integers) < desired_length:
        random_integer = random.randint(min_value, max_value)
        if random_integer not in unique_random_integers:
            unique_random_integers.append(random_integer)
    return sorted(unique_random_integers)

def generate_unique_random_queries(min_value, max_value, number_of_queries):
    unique_random_queries = []
    while len(unique_random_queries) < number_of_queries:
        query = generate_unique_random_integers_list(min_value, max_value, 2)
        if query not in unique_random_queries:
            unique_random_queries.append(query)
    return sorted(unique_random_queries)

##########################
#        Main Code       #
##########################

input_string = read_string_from_input()
input_string_length = len(input_string)

def compute_score_for_substring(substring, substring_start_index, total_length):
    substring_length = len(substring)
    score = 0
    if substring_length == 1 and substring_start_index == total_length - 1:
        if substring == 'g':
            score += 1
    elif substring_length == 2:
        if substring == 'gg':
            score += 1
        elif substring == 'pp':
            score -= 1
    return score

final_score = 0

for substring_start_index in range(-1, input_string_length, 2):
    substring_to_check = input_string[max(0, substring_start_index):min(input_string_length - 1, substring_start_index + 1) + 1]
    final_score += compute_score_for_substring(substring_to_check, substring_start_index, input_string_length)

print(final_score)