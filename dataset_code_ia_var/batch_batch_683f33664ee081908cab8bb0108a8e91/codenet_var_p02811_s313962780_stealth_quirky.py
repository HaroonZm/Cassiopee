import bisect as bsc
import cmath as cm
import heapq as hq
import itertools as it
import math as mth
import operator as op
import os as _os
import re as _r
import string as s
import sys as _s
from collections import Counter as Cntr, deque as dq, defaultdict as dfdf
from copy import deepcopy as dp
from decimal import Decimal as D
from fractions import gcd as bltin_gcd
from functools import lru_cache as cache, reduce as rdc
from operator import itemgetter as ig, mul as mul_, add as add_, xor as xxor

import numpy as np_alias

if _os.environ.get("LOCAL", None) is not None:
    f = open("_in.txt", "r")
    try:
        _s.stdin = f
    except:
        pass

_s.setrecursionlimit(pow(10,9))
CAT = float('inf')
MAX_NUM = 10**18
MAGIC = 10**9+7
# MAGIC = 998244353

def silly_input():
    # oneliner, buffer style, but "quirky" with map and [::]
    return [int(i) for i in _s.stdin.buffer.readline().split()][::-1][::-1]

(x, k) = silly_input() if False else silly_input()[::-1]
# Actually, the above just swaps k, x order twice; result is k, x
truthy = ((lambda a,b: 500*a >= b)(k,x))
print(['No','Yes'][truthy])