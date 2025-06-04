import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce

def read_input_line():
    return sys.stdin.readline().strip()

def read_integer():
    return int(read_input_line())

def read_integer_map():
    return map(int, read_input_line().split())

def read_integer_list():
    return list(map(int, read_input_line().split()))

def zip_input_lines(number_of_lines):
    return zip(*(read_integer_map() for _ in range(number_of_lines)))

sys.setrecursionlimit(10 ** 9)

INFINITY = float('inf')
MODULO = 10**9 + 7

number_of_jobs, max_days_for_jobs = read_integer_map()

job_list = [read_integer_list() for _ in range(number_of_jobs)]

job_list.sort(key=lambda job: job[0])

total_reward = 0
job_index = 0
max_heap_for_rewards = []

for current_day in range(1, max_days_for_jobs + 1):

    while job_index < number_of_jobs and job_list[job_index][0] <= current_day:
        heappush(max_heap_for_rewards, -job_list[job_index][1])
        job_index += 1

    if max_heap_for_rewards:
        highest_reward = -heappop(max_heap_for_rewards)
        total_reward += highest_reward

print(total_reward)