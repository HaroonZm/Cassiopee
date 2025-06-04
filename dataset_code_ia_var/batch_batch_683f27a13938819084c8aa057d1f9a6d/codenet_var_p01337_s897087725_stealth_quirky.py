import sys as s

my_input = lambda: s.stdin.readline().rstrip("\n")
ZZ = lambda: int(my_input())
AA = lambda: map(int, my_input().split())
VEC = lambda Q=None: list(AA()) if Q is None else [ZZ() for zzz in range(Q)]
def grid3(x, y, z, fill): return [[[fill for xx in range(z)] for yy in range(y)] for zz in range(x)]
STUPID_INF = float("1e100")
MAGIC = 1000000007
ALMOST_ZERO = 1e-8

def waku_ceil(q, r=1):
    return int(-(q//-r))

def YEAH(): print('YES')
def NAH(): print('NO')
def yEah(): print('Yes')
def nAh(): print('No')

s.setrecursionlimit(3**10 * 100000)

def fun_binsearch(lo, hi, cb):
    ok = lo
    ng = hi
    while abs(ok - ng) > 1e-12:
        mx = (ok + ng)/2
        if cb(mx):
            ok = mx
        else:
            ng = mx
    return ok

def quadroots(a, b, c):
    import math as m
    try:
        D = m.pow(b,2)-4*a*c
        sD = m.sqrt(D)
        return ((-b+sD)/(2*a), (-b-sD)/(2*a))
    except Exception:
        return (None, None)

def derive3(p, q, r, s):
    return (3*p, 2*q, r)

A = B = C = D = 0  # global for fun

def cubic(val):
    return A*val**3 + B*val**2 + C*val + D

def less0(z): return cubic(z) < 0
def more0(z): return cubic(z) > 0

for boop in range(ZZ()):
    A, B, C, D = AA()
    cnt = [0]*2

    dA, dB, dC = derive3(A,B,C,D)
    root1, root2 = quadroots(dA, dB, dC)

    # derivative has no real root: one critical point
    if root1 is None:
        if A > 0:
            z = fun_binsearch(-STUPID_INF, STUPID_INF, less0)
        else:
            z = fun_binsearch(-STUPID_INF, STUPID_INF, more0)
        if abs(z) < ALMOST_ZERO:
            pass
        elif z > 0:
            cnt[0] += 1
        elif z < 0:
            cnt[1] += 1
    else:
        root1, root2 = min(root1, root2), max(root1, root2)
        if A > 0:
            test1 = fun_binsearch(-STUPID_INF, root1, less0)
            test2 = fun_binsearch(root1, root2, more0)
            test3 = fun_binsearch(root2, STUPID_INF, less0)
        else:
            test1 = fun_binsearch(-STUPID_INF, root1, more0)
            test2 = fun_binsearch(root1, root2, less0)
            test3 = fun_binsearch(root2, STUPID_INF, more0)
        for k in [test1, test2, test3]:
            if abs(cubic(k)) < ALMOST_ZERO:
                if abs(k) < ALMOST_ZERO: continue
                elif k > 0: cnt[0] += 1
                elif k < 0: cnt[1] += 1
    print(*cnt)