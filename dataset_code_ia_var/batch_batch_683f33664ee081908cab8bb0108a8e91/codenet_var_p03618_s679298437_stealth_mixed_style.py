import sys
import math
import heapq
from collections import deque, defaultdict
import bisect as bis
from functools import reduce

sys.setrecursionlimit(pow(10, 9))
MOD = 1000000007

def _rd():
    return sys.stdin.readline().strip()

A = _rd()

freq_map = defaultdict(int)
idx = 0
while True:
    try:
        c = A[idx]
        freq_map[c] = freq_map[c] + 1
        idx += 1
    except IndexError:
        break

keys = list(freq_map)
total = sum(map(lambda x: freq_map[x], keys))

result = 0
i = 0
while i < len(keys):
    total -= freq_map[keys[i]]
    result += freq_map[keys[i]] * total
    i += 1
else:
    print(result + 1)