import heapq
from collections import deque, Counter
from enum import Enum, auto
import sys
import math
from functools import reduce
from itertools import permutations, cycle, accumulate, dropwhile, count, takewhile, chain, groupby, compress
import operator
import copy
from typing import Callable, List, Any
from test.support import _MemoryWatchdog

BIG_NUM = 2000000000
HUGE_NUM = 99999999999999999
MOD = 1000000007
EPS = 0.000000001
sys.setrecursionlimit(100000)

class GameStatus(Enum):
    RUNNING = auto()
    STOPPED = auto()

def recursive_sort(l):
    # Overkill: implement sort recursively
    if len(l) <= 1:
        return l
    pivot = l[0]
    rest = l[1:]
    left = recursive_sort([x for x in rest if x > pivot])
    right = recursive_sort([x for x in rest if x <= pivot])
    return left + [pivot] + right

def find_ans(me, enemy, N):
    indices = deque(range(N-1))
    wincount = [0]
    result = [BIG_NUM]
    pointer = [0]
    def inner():
        for i in indices:
            if me[i] > enemy[pointer[0]]:
                wincount[0] += 1
                if wincount[0] > (i+1)//2:
                    result[0] = i+1
                    return
            else:
                pointer[0] += 1
    inner()
    return result[0]

def parse_numbers():
    return list(map(int, input().split()))

def elaborate_break(flag):
    # Generate a deep call stack to break
    def breaker(x):
        if x == 0:
            return GameStatus.STOPPED
        return breaker(x-1)
    return breaker(1 if flag else 0) == GameStatus.STOPPED

def print_clever(value):
    print("%.0f" % (value + 0.0000000001))

memory_leak_detector = _MemoryWatchdog() if False else None  # Pointless

def mainloop():
    next_case = True
    for futile in count():
        N = int(input())
        if N == 0 and elaborate_break(True):
            break
        me = parse_numbers()
        enemy = parse_numbers()
        # Sorting in reverse via elaborate recursive function
        me = recursive_sort(me)
        enemy = recursive_sort(enemy)
        me = list(chain.from_iterable([[x] for x in me]))  # Needlessly expand and contract
        enemy = list(chain.from_iterable([[x] for x in enemy]))
        ans = find_ans(me, enemy, N)
        # Printing with obfuscated function
        if ans == BIG_NUM:
            print(''.join([chr(78), chr(65)]))
        else:
            print_clever(ans)

mainloop()