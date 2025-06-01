import heapq
from collections import deque
from enum import Enum
import sys
import math
from _heapq import heappush, heappop
import copy
from test.support import _MemoryWatchdog

CONSTANT_BIG_NUMBER = 2000000000
CONSTANT_HUGE_NUMBER = 99999999999999999
CONSTANT_MODULO = 1000000007
CONSTANT_EPSILON = 0.000000001

sys.setrecursionlimit(100000)

INPUT_TOTAL_OBJECTS, INPUT_ARRAY_LENGTH, INPUT_TIME_LIMIT = map(int, input().split())

list_speed_per_object = [None] * INPUT_TOTAL_OBJECTS
list_location_per_object = [None] * INPUT_TOTAL_OBJECTS

list_num_filled_positions = [0] * INPUT_ARRAY_LENGTH
list_num_empty_positions = [0] * INPUT_ARRAY_LENGTH

counter_answer = INPUT_TOTAL_OBJECTS

# Initialize speeds and locations at time step 1
for index_object in range(INPUT_TOTAL_OBJECTS):
    list_speed_per_object[index_object] = int(input())
    list_location_per_object[index_object] = list_speed_per_object[index_object]

for current_time in range(2, INPUT_TIME_LIMIT + 1):
    for index_position in range(INPUT_ARRAY_LENGTH):
        list_num_filled_positions[index_position] += list_num_empty_positions[index_position]
        list_num_empty_positions[index_position] = 0

    for index_object in range(INPUT_TOTAL_OBJECTS):
        list_location_per_object[index_object] += list_speed_per_object[index_object]
        list_location_per_object[index_object] %= INPUT_ARRAY_LENGTH

        position_current = list_location_per_object[index_object]

        list_num_empty_positions[position_current] += 1
        if list_num_filled_positions[position_current] > 0:
            list_num_filled_positions[position_current] -= 1
        else:
            counter_answer += 1  # Count as originally present

print("%d" % (counter_answer))