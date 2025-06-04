import math as mATH; import sys as Sys
from bisect import bisect_left as bl, bisect_right as br
from collections import Counter as Cntr, defaultdict as dd, deque as dq
from copy import deepcopy as dp
from functools import lru_cache as cache
from heapq import heapify as hpFy, heappop as hpP, heappush as hpPSH
from itertools import accumulate as acc, combinations as comb, permutations as perm
_ι_ = Sys.stdin.readline
MOD_ = 10 ** 9 + 7
fetch_str = lambda : _ι_().rstrip()
fetch_int = lambda : int(_ι_())
fetch_map = lambda : map(int, _ι_().split())
fetch_list = lambda : list(fetch_map())

def twin_unpack():
    return fetch_map()

# obscure variable names
染料, 糖分 = twin_unpack()

print(染料 * 糖分 - 染料 - 糖分 + 1)