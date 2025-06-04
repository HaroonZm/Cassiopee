#!/usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

def read_int_list(): return [int(x) for x in sys.stdin.readline().split()]
def read_int(): return int(sys.stdin.readline())
def read_str_list(): return [list(x) for x in sys.stdin.readline().split()]
def read_str(): return list(sys.stdin.readline())[:-1]
def read_int_repeat(count): return [read_int() for _ in range(count)]
def read_int_list_repeat(count): return [read_int_list() for _ in range(count)]
def read_str_repeat(count): return [read_str() for _ in range(count)]
def read_str_list_repeat(count): return [read_str_list() for _ in range(count)]

sys.setrecursionlimit(1000000)
MODULO = 1000000007

def process_entries(entry_count):
    entry_data_list = []
    for entry_index in range(entry_count):
        input_fields = input().split()
        (
            name,
            param_p,
            param_a,
            param_b,
            param_c,
            param_d,
            param_e,
            param_f,
            param_s,
            param_m
        ) = input_fields[0], *[int(value) for value in input_fields[1:]]
        metric_value = (param_f * param_s * param_m - param_p) / (param_a + param_b + param_c + (param_d + param_e) * param_m)
        entry_data_list.append((metric_value, name))
    entry_data_list.sort(key=lambda item: (-item[0], item[1]))
    for metric_value, name in entry_data_list:
        print(name)
    print("#")
    return

if __name__ == "__main__":
    while True:
        total_entries = read_int()
        if total_entries == 0:
            break
        process_entries(total_entries)