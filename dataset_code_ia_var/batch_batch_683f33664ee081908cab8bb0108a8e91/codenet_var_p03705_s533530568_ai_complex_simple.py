import random
import functools
import copy
import bisect
import array
import re
import collections
import heapq
import fractions
import itertools
import string
import math
from operator import itemgetter as ig
from bisect import bisect_left, bisect_right, insort_left, insort_right
from itertools import permutations, combinations, product, accumulate, groupby
from heapq import heappush, heappop
from collections import deque, defaultdict, Counter
import sys
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20
INF = float("INF")
mod = 10 ** 9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = dd + [(-1, 1), (1, 1), (1, -1), (-1, -1)]
ddn9 = ddn + [(0, 0)]
'''
for dx, dy in dd:
        nx = j + dx; ny = i + dy
            if 0 <= nx < w and 0 <= ny < h:
'''

def main():
    N, A, B = map(int, input().split())
    val = lambda x, y: x*(N-1) + y
    lst = list(map(lambda x: val(*x), product([A,B],[B,A])))
    res = (max(lst) - min(lst) + 1) * ((max(lst) - min(lst)) >= 0)
    print(res)
    
if __name__ == '__main__':
    main()