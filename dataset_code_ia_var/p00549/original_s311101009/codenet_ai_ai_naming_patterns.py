import heapq
from collections import deque
from enum import Enum
import sys
import math
from _heapq import heappush, heappop
import copy
from test.support import _MemoryWatchdog

CONST_BIG_NUM = 2000000000
CONST_HUGE_NUM = 99999999999999999
CONST_MODULO = 1000000007
CONST_EPSILON = 0.000000001
sys.setrecursionlimit(100000)

IDX_J = 0
IDX_O = 1
IDX_I = 2
IDX_JO = 3
IDX_OI = 4

count_joi_triplets = 0

input_length = int(input())
input_sequence = input()

dp_table = [[0] * 5 for _ in range(input_length + 1)]

for pos in range(1, input_length + 1):
    char = input_sequence[pos - 1]
    if char == "J":
        dp_table[pos][IDX_J] += 1
    elif char == "O":
        dp_table[pos][IDX_O] += 1
        dp_table[pos][IDX_JO] += dp_table[pos - 1][IDX_J]
    else:  # char == "I"
        dp_table[pos][IDX_I] += 1
        dp_table[pos][IDX_OI] += dp_table[pos - 1][IDX_O]
        count_joi_triplets += dp_table[pos - 1][IDX_JO]
    for idx in range(5):
        dp_table[pos][idx] += dp_table[pos - 1][idx]

max_increment = max(dp_table[input_length][IDX_JO], dp_table[input_length][IDX_OI])

for pos in range(1, input_length + 1):
    char = input_sequence[pos - 1]
    if char == "J":
        max_increment = max(
            max_increment,
            dp_table[pos][IDX_J] * (dp_table[input_length][IDX_I] - dp_table[pos][IDX_I])
        )
    elif char == "O":
        max_increment = max(
            max_increment,
            dp_table[pos - 1][IDX_J] * (dp_table[input_length][IDX_I] - dp_table[pos][IDX_I])
        )
    else:
        max_increment = max(
            max_increment,
            dp_table[pos - 1][IDX_J] * (dp_table[input_length][IDX_I] - dp_table[pos][IDX_I] + 1)
        )

print("%d" % (count_joi_triplets + max_increment))