#!/usr/bin/env python3

from collections import defaultdict, deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

def read_int_list():
    return [int(value) for value in sys.stdin.readline().split()]

def read_single_int():
    return int(sys.stdin.readline())

def read_list_of_character_lists():
    return [list(word) for word in sys.stdin.readline().split()]

def read_character_list():
    result = list(sys.stdin.readline())
    if result and result[-1] == "\n":
        return result[:-1]
    return result

def read_multiple_integers(num_lines):
    return [read_single_int() for _ in range(num_lines)]

def read_multiple_int_lists(num_lines):
    return [read_int_list() for _ in range(num_lines)]

def read_multiple_character_lists(num_lines):
    return [read_character_list() for _ in range(num_lines)]

def read_multiple_list_of_character_lists(num_lines):
    return [read_list_of_character_lists() for _ in range(num_lines)]

sys.setrecursionlimit(1000000)
MODULO = 1000000007

def solve_problem():
    initial_value, threshold_value, number_of_steps = read_int_list()
    increment_sequence = read_int_list()
    total_increment_per_cycle = -sum(increment_sequence)
    
    if total_increment_per_cycle <= 0:
        current_value = initial_value
        for step_index in range(number_of_steps):
            current_value += increment_sequence[step_index]
            if current_value <= threshold_value:
                print(step_index + 1)
                return
        print(-1)
        return
    
    value_history = [initial_value]
    for step_index in range(number_of_steps):
        next_value = value_history[-1] + increment_sequence[step_index]
        value_history.append(next_value)
        if next_value <= threshold_value:
            print(step_index + 1)
            return
    
    minimum_value_in_history = min(value_history)
    for min_index in range(number_of_steps + 1):
        if value_history[min_index] == minimum_value_in_history:
            break
    
    current_value = value_history[min_index]
    rotated_increment_sequence = increment_sequence[min_index:] + increment_sequence[:min_index]
    number_of_full_cycles = (current_value - threshold_value) // total_increment_per_cycle
    current_value -= number_of_full_cycles * total_increment_per_cycle
    
    if current_value <= threshold_value:
        print(number_of_full_cycles * number_of_steps + min_index)
        return
    
    for step_index in range(number_of_steps):
        current_value += rotated_increment_sequence[step_index]
        if current_value <= threshold_value:
            print(number_of_full_cycles * number_of_steps + step_index + 1 + min_index)
            return

    return

if __name__ == "__main__":
    solve_problem()