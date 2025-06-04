import math as mth
import string as strg
import itertools as it
import fractions as fr
import heapq as hp
import collections as cl
import re as rgx
import array as arr
import bisect as bct
import sys as sysmod
import random as rnd
import time as tme
import copy as cpy
import functools as fn

sysmod.setrecursionlimit(10**7)
CONST_INF = 10**20
CONST_EPS = 1.0 / 10**13
CONST_MOD = 10**9 + 7
DIR_4 = [(-1,0), (0,1), (1,0), (0,-1)]
DIR_8 = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def read_int_list(): return [int(item) for item in sysmod.stdin.readline().split()]
def read_int_zero_indexed_list(): return [int(item)-1 for item in sysmod.stdin.readline().split()]
def read_float_list(): return [float(item) for item in sysmod.stdin.readline().split()]
def read_str_list(): return sysmod.stdin.readline().split()
def read_int(): return int(sysmod.stdin.readline())
def read_float(): return float(sysmod.stdin.readline())
def read_str(): return input()
def print_flush(obj): return print(obj, flush=True)

def main():
    results_list = []

    def process_group(group_size):
        input_list = [read_int_list() for _ in range(group_size)]
        priority_queue = []
        current_times = [0] * 2
        for time_unit, count in input_list:
            hp.heappush(priority_queue, (0, 0, time_unit, count * 2))

        while priority_queue:
            current_time, label, time_unit, count = hp.heappop(priority_queue)
            next_label = label ^ 1
            next_time = current_time + time_unit
            if current_times[next_label] > next_time:
                next_time = current_times[next_label]
            else:
                current_times[next_label] = next_time
            if count > 1:
                hp.heappush(priority_queue, (next_time, next_label, time_unit, count - 1))

        return max(current_times)

    while True:
        n_val = read_int()
        if n_val == 0:
            break
        results_list.append(process_group(n_val))

    return '\n'.join(str(val) for val in results_list)

print(main())