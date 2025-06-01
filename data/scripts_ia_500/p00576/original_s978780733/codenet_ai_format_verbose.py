import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

from math import floor, ceil, sqrt, factorial, log
from heapq import heappop, heappush, heappushpop
from collections import Counter, defaultdict, deque
from itertools import accumulate, permutations, combinations, product, combinations_with_replacement
from bisect import bisect_left, bisect_right
from copy import deepcopy

INFINITY = float('inf')
MODULUS = 10**9 + 7

def pretty_print(*lists): 
    for single_list in lists:     
        print(*single_list, sep='\n')

def decrement_index(value): 
    return int(value) - 1

def map_to_ints():
    return map(int, input().split())

def map_to_floats(): 
    return map(float, input().split())

def map_to_decremented_ints(): 
    return map(decrement_index, input().split())

def list_of_ints(): 
    return list(map_to_ints())

def list_of_decremented_ints(): 
    return [int(x) - 1 for x in input().split()]

def list_of_floats(): 
    return list(map_to_floats())

def read_multiple_ints_lines(count: int): 
    return [integer_input() for _ in range(count)]

def read_multiple_lists_of_ints(count: int): 
    return [list_of_ints() for _ in range(count)]

def read_multiple_lists_of_decremented_ints(count: int): 
    return [list_of_decremented_ints() for _ in range(count)]

def parse_line_to_list_of_ints(): 
    return [list(map(int, line.split())) for line in input()]

def integer_input(): 
    return int(input())

def float_input(): 
    return float(input())

def string_input(): 
    return input().replace('\n', '')

def main():

    number_of_elements = integer_input()

    list_of_values = list_of_ints()

    number_of_positions = integer_input()

    zero_based_positions = list_of_decremented_ints()

    presence_array = [0] * 2021

    for value in list_of_values:
        presence_array[value] += 1

    for position_index in zero_based_positions:
        
        current_value = list_of_values[position_index]

        if current_value == 2019:
            continue

        if presence_array[current_value + 1] > 0:
            continue

        presence_array[current_value] -= 1
        presence_array[current_value + 1] += 1

        list_of_values[position_index] = current_value + 1

    print(*list_of_values, sep="\n")

if __name__ == '__main__':
    main()