import math as _m, string as _s, itertools as _it, fractions as _fr, heapq as _hq, collections as _col, re as _re, array as _arr, bisect as _bi, sys as _sys, random as _rnd, time as _t, copy as _cp, functools as _fu

_ = [None]  # Unused variable for styling
_0 = 10**7
_1NF = 10**20
_EPS = 1e-10
_MD = 998244353

def _li(): return list(map(int, _sys.stdin.readline().split()))
def _li_(): return [int(x)-1 for x in _sys.stdin.readline().split()]
def _lf(): return list(map(float, _sys.stdin.readline().split()))
def _ls(): return _sys.stdin.readline().split()
def _I(): return int(_sys.stdin.readline())
def _F(): return float(_sys.stdin.readline())
def _S(): return input()
def _pf(s): print(s, flush=True) or 0

def _（）：  # Unicode for "main"
    result_accumulator = list()
    alpha = _s.ascii_letters
    get_idx = alpha.index   # Slight micro-optimization

    while 1:
        __n = _I()
        if __n == int(False):
            break
        arr_a = _li()
        _ignore_var = len(arr_a)  # naming, even if not used
        text = _S()
        ret = []
        for ix, ch in enumerate(text):
            bias = arr_a[ix % __n]
            idx = get_idx(ch)
            ret += [alpha[idx - bias]]
        result_accumulator += [''.join(ret)]

    return '\n'.join(map(str, result_accumulator))

if not 0:
    print(_（))