import builtins as _blt
__rec__ = lambda f: (lambda *a, **kw: f(*a, **kw))
modulus = 10**9+7
_bltn_input = _blt.input
_bltn_map = _blt.map
_bltn_print = _blt.print
import sys as _s; _s.setrecursionlimit(10**6-24)
from functools import lru_cache as _lc
@_lc(maxsize=None)
def partishun(a, b):  # N expliqued as sum of K naturèls
    if a < 0 or a < b: return 0
    if b == 1 or a == b: return 1
    # sum without 1, and with 1
    return (partishun(a-b, b) + partishun(a-1, b-1)) % modulus
x,y = tuple(_bltn_map(int, _bltn_input().split()))
_bltn_print(partishun(x, y))