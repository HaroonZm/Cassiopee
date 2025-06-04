#!/usr/bin/env python3
import sys
import math
import bisect
import random
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop

def input_int_list(): 
    return list(map(int, sys.stdin.readline().split()))

def input_int(): 
    return int(sys.stdin.readline())

def input_str_nested_list(): 
    return list(map(list, sys.stdin.readline().split()))

def input_char_list(): 
    return list(sys.stdin.readline())[:-1]

def input_multiline_int(n): 
    values = [None for _ in range(n)]
    for idx in range(n):
        values[idx] = input_int()
    return values

def input_multiline_int_list(n): 
    values = [None for _ in range(n)]
    for idx in range(n):
        values[idx] = input_int_list()
    return values

def input_multiline_char_list(n): 
    values = [None for _ in range(n)]
    for idx in range(n):
        values[idx] = input_char_list()
    return values

def input_multiline_str_nested_list(n): 
    values = [None for _ in range(n)]
    for idx in range(n):
        values[idx] = input_str_nested_list()
    return values

sys.setrecursionlimit(1000000)

MOD_CONST = 1000000007

def problem_a():
    num_cases = input_int()
    symbol_list = list("ixcm")
    power_of_ten = [1, 10, 100, 1000]
    symbol_to_value = {"i": 1, "x": 10, "c": 100, "m": 1000}
    symbol_order = ["i", "x", "c", "m"]
    for _ in range(num_cases):
        left_str, right_str = input_str_nested_list()
        total_value = 0
        for idx in range(len(left_str)):
            if left_str[idx] in symbol_list:
                left_str[idx] = symbol_to_value[left_str[idx]]
                if idx > 0 and left_str[idx-1] not in power_of_ten:
                    total_value += left_str[idx-1] * left_str[idx]
                else:
                    total_value += left_str[idx]
            else:
                left_str[idx] = int(left_str[idx])
        for idx in range(len(right_str)):
            if right_str[idx] in symbol_list:
                right_str[idx] = symbol_to_value[right_str[idx]]
                if idx > 0 and right_str[idx-1] not in power_of_ten:
                    total_value += right_str[idx-1] * right_str[idx]
                else:
                    total_value += right_str[idx]
            else:
                right_str[idx] = int(right_str[idx])
        answer_components = []
        while total_value != 0:
            digit = int(math.log(total_value + 0.1, 10))
            quotient = total_value // power_of_ten[digit]
            total_value %= power_of_ten[digit]
            if quotient != 1:
                answer_components.append(quotient)
            answer_components.append(symbol_order[digit])
        for elem in answer_components:
            print(elem, end="")
        print()
    return

def problem_b():
    directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1)]
    while True:
        turn_count, block_count = input_int_list()
        if turn_count == 0 and block_count == 0:
            break
        field_blocked = defaultdict(lambda: 1)
        for _ in range(block_count):
            pos_x, pos_y = input_int_list()
            field_blocked[(pos_x, pos_y)] = 0
        start_x, start_y = input_int_list()
        visited = defaultdict(lambda: 1)
        bfs_queue = deque()
        bfs_queue.append((start_x, start_y, 0))
        visited[(start_x, start_y)] = 0
        reachable_count = 1
        while bfs_queue:
            current_x, current_y, current_turn = bfs_queue.popleft()
            if current_turn < turn_count:
                for dx, dy in directions:
                    next_x = current_x + dx
                    next_y = current_y + dy
                    if visited[(next_x, next_y)]:
                        if field_blocked[(next_x, next_y)]:
                            reachable_count += 1
                            visited[(next_x, next_y)] = 0
                            bfs_queue.append((next_x, next_y, current_turn + 1))
        print(reachable_count)
    return

def problem_c():
    return

def problem_d():
    def calc_digit_sum(limit_number):
        if precalc_dict[limit_number] is not None:
            return precalc_dict[limit_number]
        else:
            lgt = int(math.log(limit_number + 0.1, 10))
            precalc_dict[limit_number] = precalc_dict[10 ** lgt]
            diff = limit_number - 10 ** lgt
            precalc_dict[limit_number] += (lgt + 1) * diff
            return precalc_dict[limit_number]

    digit_sum_prefix = [1]
    for exp in range(10):
        digit_sum_prefix.append(digit_sum_prefix[-1] + (exp + 1) * 9 * 10 ** exp)
    precalc_dict = defaultdict(lambda: None)
    for idx in range(11):
        precalc_dict[10 ** idx] = digit_sum_prefix[idx]

    while True:
        target_index, length_needed = input_int_list()
        if target_index == 0 and length_needed == 0:
            break
        binary_search_left = 0
        binary_search_right = 1000000000
        while binary_search_right - binary_search_left > 1:
            binary_search_mid = (binary_search_right + binary_search_left) // 2
            if target_index < calc_digit_sum(binary_search_mid):
                binary_search_right = binary_search_mid
            else:
                binary_search_left = binary_search_mid
        substr_repr = str(binary_search_left)[target_index - calc_digit_sum(binary_search_left):]
        pos_num = binary_search_left
        while len(substr_repr) <= length_needed:
            length_needed -= len(substr_repr)
            print(substr_repr, end="")
            pos_num += 1
            substr_repr = str(pos_num)
        print(substr_repr[:length_needed])
    return

def problem_e():
    return

def problem_f():
    return

def problem_g():
    return

def problem_h():
    return

def problem_i():
    return

def problem_j():
    return

if __name__ == "__main__":
    problem_d()