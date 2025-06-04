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

sys.setrecursionlimit(10**7)
CONST_INF = 10**20
CONST_EPS = 1.0 / 10**10
CONST_MOD = 10**9 + 7
DIRECTION_4 = [(0, -1), (1, 0), (0, 1), (-1, 0)]
DIRECTION_8 = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]

def read_int_list(): return [int(value) for value in sys.stdin.readline().split()]
def read_zero_based_int_list(): return [int(value) - 1 for value in sys.stdin.readline().split()]
def read_float_list(): return [float(value) for value in sys.stdin.readline().split()]
def read_str_list(): return sys.stdin.readline().split()
def read_int(): return int(sys.stdin.readline())
def read_float(): return float(sys.stdin.readline())
def read_string(): return input()
def print_flush(output): return print(output, flush=True)

def main():
    result_list = []

    while True:
        num_entries = read_int()
        if num_entries == 0:
            break
        log_entries = [read_str_list() for _ in range(num_entries)]
        last_time_dict = {}
        total_time_dict = collections.defaultdict(int)
        event_list = []
        for day_str, time_str, event_flag, person_id_str in log_entries:
            person_id = int(person_id_str)
            time_components = time_str.split(':')
            event_time = int(time_components[0]) * 60 + int(time_components[1])
            if person_id == 0:
                if event_flag == 'I':
                    for other_id in list(last_time_dict.keys()):
                        total_time_dict[other_id] -= event_time - last_time_dict[other_id]
                    last_time_dict[person_id] = event_time
                else:
                    del last_time_dict[person_id]
                    for other_id in list(last_time_dict.keys()):
                        total_time_dict[other_id] += event_time - last_time_dict[other_id]
            else:
                if event_flag == 'I':
                    last_time_dict[person_id] = event_time
                else:
                    if 0 in last_time_dict:
                        total_time_dict[person_id] += event_time - last_time_dict[person_id]
                    del last_time_dict[person_id]
        if len(total_time_dict) == 0:
            result_list.append(0)
        else:
            result_list.append(max(total_time_dict.values()))

    return '\n'.join(map(str, result_list))

print(main())