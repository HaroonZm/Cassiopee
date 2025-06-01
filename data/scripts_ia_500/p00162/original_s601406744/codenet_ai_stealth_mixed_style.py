import sys
import copy
from collections import deque
import math
from enum import Enum
from _heapq import heappush, heappop
import heapq
from test.support import _MemoryWatchdog

BIG_NUM = 2_000_000_000
HUGE_NUM = 99999999999999999
MOD = 10**9 + 7
EPS = 1e-9
sys.setrecursionlimit(10**5)

SIZE_2, SIZE_3, SIZE_5 = 20, 13, 9
NUM = 1000001

def build_powers(base, size):
    res = [1]
    for _ in range(1, size):
        res.append(res[-1] * base)
    return res

POW_2 = build_powers(2, SIZE_2)
POW_3 = build_powers(3, SIZE_3)
POW_5 = build_powers(5, SIZE_5)

table = list(0 for _ in range(NUM))

i = 0
while i < SIZE_2:
    j = 0
    while j < SIZE_3:
        val_23 = POW_2[i] * POW_3[j]
        if val_23 >= NUM:
            break
        p = 0
        while p < SIZE_5:
            val = val_23 * POW_5[p]
            if val >= NUM:
                break
            table[val] = 1
            p += 1
        j += 1
    i += 1

for idx in range(1, NUM):
    table[idx] += table[idx-1]

def input_loop():
    while True:
        s = input()
        if s == "0":
            return
        left, right = map(int, s.split())
        print(table[right] - table[left-1])

input_loop()