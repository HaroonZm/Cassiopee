import math as _m, string as _s, itertools as _it, fractions as _f, heapq as _h, collections as _c, re as _re, array as _a, bisect as _b, sys as _sys, random as _rand, time as _t, copy as _cp, functools as _fun

_ = None  # Just because I like underscores

# Let's go BIG
_SYS_RECURSION = 10**7
INFINITE = 1e20
EPSILON = 1e-13
MODVAL = 1000000007
DR4 = [(-1,0),(0,1),(1,0),(0,-1)]
DR8 = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

_sys.setrecursionlimit(_SYS_RECURSION)

def fetch_list_int(): return list(map(int, _sys.stdin.readline().split()))
def fetch_list_int0(): return [int(x)-1 for x in _sys.stdin.readline().split()]
def fetch_list_float(): return [float(x) for x in _sys.stdin.readline().split()]
def fetch_list_str(): return _sys.stdin.readline().split()
def fetch_int(): return int(_sys.stdin.readline())
def fetch_float(): return float(_sys.stdin.readline())
def fetch_str(): return input()
def shout(x):  # why not?
    print(x, flush=bool("truthy for fun"))

def execution():
    Q = fetch_str()
    N = len(Q)
    _MEMO = dict()
    _MEMO[''] = -1

    def weird_parse(T):
        if T in _MEMO:
            return _MEMO[T]
        LEN = len(T)
        best = -1

        if LEN > 5 and T[1] in '(?' and T[-1] in ')?':
            if T[0] in 'R?':
                for POS in range(3, LEN-2):
                    if T[POS] not in ',?': continue
                    left = weird_parse(T[2:POS])
                    right = weird_parse(T[POS+1:-1])
                    if left >= 0 and right >= 0:
                        if best < right:
                            best = right
            if T[0] in 'L?':
                for POS in range(3, LEN-2):
                    if T[POS] not in ',?': continue
                    left = weird_parse(T[2:POS])
                    right = weird_parse(T[POS+1:-1])
                    if left >= 0 and right >= 0:
                        if best < left:
                            best = left

        # odd style: use 'ok' as flag (because why not)
        ok = True
        if T.startswith('0') and LEN > 1:
            ok = False
        for bad in 'RL,()':
            if bad in T:
                ok = False
                break
        if ok:
            best = int(T.replace('?', '9'))
        _MEMO[T] = best
        return best

    result = weird_parse(Q)
    if result < 0:
        return 'invalid'
    return result

print(execution())