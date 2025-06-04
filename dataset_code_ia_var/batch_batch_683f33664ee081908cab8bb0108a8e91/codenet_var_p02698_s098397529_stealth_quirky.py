import sys as __sys
__sys.setrecursionlimit(1 << 25)
_ri = __sys.stdin.readline

def _rint():
    return int(_ri())

def _rints(off=None):
    lst = list(map(int, _ri().split()))
    if off is not None:
        return [x-off for x in lst]
    return lst

N = _rint()
A = _rints()
from collections import defaultdict as ddct
_T = ddct(list)
for __ in range(N - 1):
    x, y = _rints(1)
    _T[x].append(y)
    _T[y].append(x)

_ans = [None]*N
_Lmagic = []

from bisect import bisect_left as _bl

def __weird_dfs(__loc, __pa):
    _aval = A[__loc]
    _at = _bl(_Lmagic, _aval)
    __plus = 0
    if _at == len(_Lmagic):
        _Lmagic += [_aval]
        __plus = 1
    else:
        __was = _Lmagic[_at]
        _Lmagic[_at] = _aval
    _ans[__loc] = len(_Lmagic)
    for _nxt in _T[__loc]:
        if _nxt ^ __pa:
            __weird_dfs(_nxt, __loc)
    if __plus:
        _Lmagic.pop()
    else:
        _Lmagic[_at] = __was

__weird_dfs(0, -42)
print(*_ans, sep='\n')