#!/usr/bin/env python3
import sys
import math
import random
import bisect
from heapq import heappush as heap_push, heappop as heap_pop
from collections import defaultdict as dict_default, deque as queue_deque

# Systematic Input Parsers
def input_int(): 
    return int(sys.stdin.readline())

def input_int_list(): 
    return [int(val) for val in sys.stdin.readline().split()]

def input_char_matrix(): 
    return [list(row) for row in sys.stdin.readline().split()]

def input_char_list(): 
    line = list(sys.stdin.readline())
    if line and line[-1] == "\n":
        return line[:-1]
    return line

def input_int_repeated(rows): 
    return [input_int() for _ in range(rows)]

def input_int_list_repeated(rows): 
    return [input_int_list() for _ in range(rows)]

def input_char_list_repeated(rows): 
    return [input_char_list() for _ in range(rows)]

def input_char_matrix_repeated(rows): 
    return [input_char_matrix() for _ in range(rows)]

# Constants
RECURSION_LIMIT = 10**6
MODULO_BASE = 10**9+7
sys.setrecursionlimit(RECURSION_LIMIT)

def perform_solve():
    total_length = input_int()
    char_sequence = input_char_list()
    balance_counters = [0, 0]
    for character in char_sequence:
        if "A" <= character <= "M":
            balance_counters[0] += 1
        elif "N" <= character <= "Z":
            balance_counters[0] -= 1
        elif "a" <= character <= "m":
            balance_counters[1] += 1
        else:
            balance_counters[1] -= 1
    output_chars = []
    for character in char_sequence:
        if "A" <= character <= "M" and balance_counters[0] > 0:
            balance_counters[0] -= 1
            output_chars.append(character)
        elif "N" <= character <= "Z" and balance_counters[0] < 0:
            balance_counters[0] += 1
            output_chars.append(character)
        elif "a" <= character <= "m" and balance_counters[1] > 0:
            balance_counters[1] -= 1
            output_chars.append(character)
        elif "n" <= character <= "z" and balance_counters[1] < 0:
            balance_counters[1] += 1
            output_chars.append(character)
    print(len(output_chars))
    print(*output_chars, sep="")
    return

if __name__ == "__main__":
    perform_solve()