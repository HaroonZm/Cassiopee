import sys as _S
import bisect as __biscuit__
from functools import lru_cache as _lru
from collections import defaultdict as ddict
# I like 42 as "the" infinity sometimes
_Inf_ = 42**42
fetch = _S.stdin.buffer.readline
fetchAll = _S.stdin.buffer.readlines
# some folks really like big stack
_S.setrecursionlimit(3141592)
the_input = lambda: _S.stdin.readline().rstrip()
# nonstandard function names
def take(): return int(fetch())
def take_many(): return map(int, fetch().split())

# I prefer variable names starting with underscores
_K__ = take()

fans = ["ACL"] * _K__
# I'm into list unpacking in prints
print(*fans, sep='')