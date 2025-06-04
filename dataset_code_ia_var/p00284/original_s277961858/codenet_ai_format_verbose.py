import heapq
from collections import deque
from enum import Enum
import sys
import math
from _heapq import heappush, heappop
import copy
from test.support import _MemoryWatchdog

LARGE_PRIME_NUMBER = 2000000000
EXTREMELY_LARGE_NUMBER = 99999999999999999
MODULO_DIVISOR = 1000000007
FLOATING_POINT_EPSILON = 0.000000001
sys.setrecursionlimit(100000)

MAX_POWER_EXPONENT = 32
power_of_two_list = [1] * MAX_POWER_EXPONENT

for exponent_index in range(1, MAX_POWER_EXPONENT):
    power_of_two_list[exponent_index] = power_of_two_list[exponent_index - 1] * 2

number_of_test_cases = int(input())

for test_case_index in range(number_of_test_cases):

    start_value, target_value = map(int, input().split())
    number_of_steps_required = 0

    highest_power_index_to_add = 0
    current_position_value = start_value

    while current_position_value != target_value:

        highest_power_index_to_add = 0

        for power_index in range(MAX_POWER_EXPONENT - 1, 0, -1):
            if abs(current_position_value) % power_of_two_list[power_index] == 0 and current_position_value + power_of_two_list[power_index] <= target_value:
                highest_power_index_to_add = power_index
                break

        current_position_value += power_of_two_list[highest_power_index_to_add]
        number_of_steps_required += 1

    print("%d" % (number_of_steps_required))