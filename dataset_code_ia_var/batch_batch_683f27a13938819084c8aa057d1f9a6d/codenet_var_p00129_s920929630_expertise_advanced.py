import math
from functools import partial

def R(coords):
    return math.hypot(*coords)

def I(i, *, inp=input):
    return [list(map(int, inp().split())) for _ in range(i)]

def C(a, b, eps=1e-6):
    return abs(a - b) < eps or a > b

def f(e1, WP):
    tx, ty, sx, sy = e1
    st = [tx - sx, ty - sy]
    rst = R(st)
    for wx, wy, r in WP:
        wt = [tx - wx, ty - wy]
        rwt = R(wt)
        sw = [wx - sx, wy - sy]
        rsw = R(sw)
        F = [rwt < r, rsw < r]
        if sum(F) == 1:
            return False
        elif not any(F):
            a = math.pi / 2 - math.acos(r / rsw)
            dot = sw[0] * st[0] + sw[1] * st[1]
            b = math.acos(round(dot / (rsw * rst), 4))
            if C(a, b) and C(rst ** 2, rsw ** 2 - r ** 2):
                return False
    return True

def main():
    import sys
    inp = sys.stdin.readline
    while True:
        n = int(inp())
        if not n:
            break
        WP = I(n, inp=inp)
        m = int(inp())
        P = I(m, inp=inp)
        results = ("Safe", "Danger")
        optimize_f = partial(f, WP=WP)
        for e in P:
            print(results[not optimize_f(e)])

if __name__ == "__main__":
    main()