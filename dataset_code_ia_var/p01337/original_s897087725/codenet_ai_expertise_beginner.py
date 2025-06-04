import sys
import math

sys.setrecursionlimit(10**9)

INF = 10**18
MOD = 10**9 + 7
EPS = 1e-8

def read_int():
    return int(sys.stdin.readline().strip())

def read_ints():
    return map(int, sys.stdin.readline().strip().split())

def ceil(x, y=1):
    return int(-(-x // y))

def bisearch_max(mn, mx, func):
    ok = mn
    ng = mx
    while abs(ok - ng) > 1e-12:
        mid = (ok + ng) / 2
        if func(mid):
            ok = mid
        else:
            ng = mid
    return ok

def solve_quadratic(a, b, c):
    try:
        d = b*b - 4*a*c
        sqrt_d = math.sqrt(d)
        x1 = (-b + sqrt_d)/(2*a)
        x2 = (-b - sqrt_d)/(2*a)
        return (x1, x2)
    except:
        return (None, None)

def diff_cubic(a, b, c, d):
    a_new = a*3
    b_new = b*2
    return (a_new, b_new, c)

def calc_cubic(x):
    return A*x**3 + B*x**2 + C*x + D

def check_down(x):
    return calc_cubic(x) < 0

def check_up(x):
    return calc_cubic(x) > 0

T = read_int()
for _ in range(T):
    a, b, c, d = read_ints()
    ans = [0, 0]
    # グローバル変数として持ち回す（初心者的書き方）
    A = a
    B = b
    C = c
    D = d

    a1, b1, c1 = diff_cubic(a, b, c, d)
    sol1, sol2 = solve_quadratic(a1, b1, c1)

    if sol1 is None:
        if a > 0:
            x = bisearch_max(-INF, INF, check_down)
        else:
            x = bisearch_max(-INF, INF, check_up)
        if abs(x) < EPS:
            pass
        elif x > 0:
            ans[0] += 1
        elif x < 0:
            ans[1] += 1
    else:
        x1 = min(sol1, sol2)
        x2 = max(sol1, sol2)
        if a > 0:
            r1 = bisearch_max(-INF, x1, check_down)
            r2 = bisearch_max(x1, x2, check_up)
            r3 = bisearch_max(x2, INF, check_down)
        else:
            r1 = bisearch_max(-INF, x1, check_up)
            r2 = bisearch_max(x1, x2, check_down)
            r3 = bisearch_max(x2, INF, check_up)
        for xx in [r1, r2, r3]:
            if abs(calc_cubic(xx)) < EPS:
                if abs(xx) < EPS:
                    continue
                elif xx > 0:
                    ans[0] += 1
                elif xx < 0:
                    ans[1] += 1
    print(ans[0], ans[1])