import math
def R(A):
    return (A[0]**2 + A[1]**2) ** 0.5

def I(i):
    points = []
    for _ in range(i):
        points.append(list(map(int, input().split())))
    return points

def C(a, b):
    return a > b or abs(a - b) < 1e-6

def f(e1):
    tx, ty, sx, sy = e1
    x = []
    st = [tx - sx, ty - sy]
    rst = R(st)
    for e2 in WP:
        wx, wy, r = e2
        wt = [tx - wx, ty - wy]
        rwt = R(wt)
        sw = [wx - sx, wy - sy]
        rsw = R(sw)
        F = [rwt < r, rsw < r]
        c = 1
        if F == [1, 0] or F == [0, 1]:
            return 0
        elif F == [0, 0]:
            a = math.pi / 2 - math.acos(r / rsw)
            val = (sw[0] * st[0] + sw[1] * st[1]) / (rsw * rst)
            b = math.acos(round(val, 4))
            if C(a, b) and C(rst**2, rsw**2 - r**2):
                return 0
        x.append(c)
    return all(x)

while True:
    n = int(input())
    if n == 0:
        break
    WP = I(n)
    P = I(int(input()))
    for e in P:
        if f(e):
            print("Safe")
        else:
            print("Danger")