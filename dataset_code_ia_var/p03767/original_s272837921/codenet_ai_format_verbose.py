import sys
import math
from bisect import bisect_right as bisect_right_position
from bisect import bisect_left as bisect_left_position
sys.setrecursionlimit(2147483647)
from heapq import heappush, heappop, heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations

MODULO = 10 ** 9 + 7
INFINITY = float('inf')

def read_single_integer():
    return int(sys.stdin.readline())

def read_integer_list():
    return list(map(int, sys.stdin.readline().split()))

number_of_elements = read_single_integer()

input_integer_list = read_integer_list()

input_integer_list.sort(reverse=True)

sum_selected_values = 0
number_of_values_summed = 0
current_index = 1

while number_of_values_summed < number_of_elements:
    sum_selected_values += input_integer_list[current_index]
    current_index += 2
    number_of_values_summed += 1

print(sum_selected_values)