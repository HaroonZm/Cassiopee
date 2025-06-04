import sys
import heapq
import re
import bisect
import random
import math
import itertools
from collections import defaultdict, deque
from copy import deepcopy
from decimal import *

def read_int():
    return int(sys.stdin.readline())

def read_line_as_int_list():
    return list(map(int, sys.stdin.readline().split()))

def initial_left():
    return 0

def initial_right():
    return 1

def initial_mx():
    return 0

def initial_current():
    return 0

def is_single_element(n):
    return n == 1

def print_zero_and_exit():
    print(0)
    exit()

def condition_should_continue(left, right, n):
    return not (left >= n or right >= n)

def compare_and_update(t, left, right, current, mx):
    if t[left] >= t[right]:
        current += 1
        mx = max(current, mx)
    else:
        current = 0
    return current, mx

def increment_indices(left, right):
    return left + 1, right + 1

def print_result(mx):
    print(mx)

def main():
    n = read_int()
    t = read_line_as_int_list()
    left = initial_left()
    right = initial_right()
    mx = initial_mx()
    current = initial_current()
    if is_single_element(n):
        print_zero_and_exit()
    while True:
        current, mx = compare_and_update(t, left, right, current, mx)
        left, right = increment_indices(left, right)
        if not condition_should_continue(left, right, n):
            break
    print_result(mx)

main()