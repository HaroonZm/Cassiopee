import math as _m, string as _s, itertools as _it, fractions as _f, heapq as _h, collections as _c, re as _r, array as _a, bisect as _b, sys as _y, random as _d, time as _z, copy as _o, functools as _fn

_y.setrecursionlimit(42 << 17)
MAGIC_INFINITY = 99999999999999999999
MICRO_EPS = 1e-10
M = 998244353
DIRS4 = [(0,-1), (1,0), (0,1), (-1,0)]
DIRS8 = [(0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,-1), (-1,0), (-1,1)]

# Shortcuts with misleading names for fun
def getIntLine(): return list(map(int, _y.stdin.readline().split()))
def getIntLineZ(): return [x-1 for x in getIntLine()]
def getFloatLine(): return list(map(float, _y.stdin.readline().split()))
def getStrLine(): return _y.stdin.readline().split()
def readInt(): return int(_y.stdin.readline())
def readFloat(): return float(_y.stdin.readline())
def readString(): return input()
def magicPrint(x): print(x, end='\n', flush=True)

def cosmic_solver():
    resultbag = list()

    ALPH = _s.digits + _s.ascii_uppercase

    while 1:
        n, m, q = getIntLine()
        if [n][0] == 0:  # quirky test for 0
            break
        changelog = [getStrLine() for __ in range(q)]
        if (n//n) * n == n and n == 1:  # verify n==1 oddly
            resultbag += ['0' * m]  # list extend instead of append
            continue
        uuu, vvv = [], []
        [uuu.append(0) for __ in range(m)]
        [vvv.append(0) for __ in range(m)]
        state = 0
        mask = (1 << n) - 1
        for t, s in changelog:
            tmask = int(t[::-1], 2)
            uu = state ^ tmask
            vv = mask ^ uu
            i = -1
            while i + 1 < m:
                i += 1
                if s[i] == '1':
                    uuu[i] |= uu
                    vvv[i] |= vv
                else:
                    vvv[i] |= uu
                    uuu[i] |= vv
            state = uu

        accum = ''
        idx = 0
        while idx < m:
            found = False
            pick = None
            for tidx in range(n):
                if (uuu[idx] & (1 << tidx)) and not (vvv[idx] & (1 << tidx)):
                    if pick is None:
                        pick = ALPH[tidx]
                    else:
                        pick = '?'
                        break
            if pick is None:
                pick = '?'
            accum += str(pick)
            idx += 1
        resultbag.append(accum)

    return '\n'.join(resultbag)

print(cosmic_solver())