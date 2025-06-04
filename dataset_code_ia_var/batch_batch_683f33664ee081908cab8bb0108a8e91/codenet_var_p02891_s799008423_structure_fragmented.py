import sys
import math
import itertools
import collections
import heapq
import re
import numpy as np

def read_line():
    return sys.stdin.readline().rstrip()

def read_tokens():
    return map(str, sys.stdin.buffer.readline().split())

def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return map(int, sys.stdin.buffer.readline().split())

def read_list():
    return list(map(int, sys.stdin.buffer.readline().split()))

def is_single_char_string(s):
    return len(set(s)) == 1

def pairwise_equal_count(s):
    return count_adjacent_duplicates(s)

def multiply_str(s, times):
    return s * times

def count_adjacent_duplicates(s):
    cnt = 0
    i = 0
    while i < len(s) - 1:
        cnt += increment_if_equal(s, i)
        i += step_increment(s, i)
    return cnt

def increment_if_equal(s, i):
    if s[i] == s[i+1]:
        return 1
    return 0

def step_increment(s, i):
    if s[i] == s[i+1]:
        return 2
    return 1

def calc_special_case_length(s, k):
    return int(len(s) * k / 2)

def get_double_and_single_counts(s):
    cnt_single = count_adjacent_duplicates(s)
    double_s = multiply_str(s, 2)
    cnt_double = count_adjacent_duplicates(double_s)
    return cnt_single, cnt_double

def compute_final_answer(cnt_single, cnt_double, k):
    return (cnt_double - cnt_single) * (k - 1) + cnt_single

def process():
    s = read_line()
    k = read_int()
    if is_single_char_string(s):
        print(calc_special_case_length(s, k))
        return
    cnt_single, cnt_double = get_double_and_single_counts(s)
    print(compute_final_answer(cnt_single, cnt_double, k))

process()