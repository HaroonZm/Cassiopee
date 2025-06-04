import sys
import math
import bisect
sys.setrecursionlimit(1000000000)
from heapq import heappush, heappop, heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations

CONST_MOD = 10**9 + 7
CONST_INF = float('inf')

def read_int(): 
    return int(sys.stdin.readline())
def read_int_list(): 
    return list(map(int, sys.stdin.readline().split()))

count_n, value_a, value_b, coef_c, coef_d = read_int_list()

range_map = defaultdict(list)
range_tuples = []
index_start = 0
index_end = count_n - 1

for loop_idx in range(count_n):
    lower_bound = value_a + index_start * coef_c - index_end * coef_d
    upper_bound = value_a + index_start * coef_d - index_end * coef_c
    range_tuples.append((lower_bound, upper_bound))
    index_start += 1
    index_end -= 1

for bound_left, bound_right in range_tuples:
    if bound_left <= value_b <= bound_right:
        print('YES')
        quit()
print('NO')