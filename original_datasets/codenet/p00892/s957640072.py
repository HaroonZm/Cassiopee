# aoj 1313
import sys
input = sys.stdin.readline

# the width of the polygon sliced at x
def width(X, Y, x):
    n = len(X)
    lb, ub = float('inf'), -float('inf')
    for i in range(n):
        x1, y1, x2, y2 = X[i], Y[i], X[(i+1) % n], Y[(i+1) % n]
        if (x1-x)*(x2-x) <= 0 and x1 != x2:
            y = y1 + (y2-y1) * (x-x1) / (x2-x1)
            lb = min(lb, y)
            ub = max(ub, y)
    return max(0, ub-lb)

while True:
    m, n = map(int, input().split())
    if m == n == 0:
        break
    X1 = [0] * m
    Y1 = [0] * m
    X2 = [0] * n
    Z2 = [0] * n
    for i in range(m):
        X1[i], Y1[i] = map(int, input().split())
    for i in range(n):
        X2[i], Z2[i] = map(int, input().split())
    min1, max1 = min(X1), max(X1)
    min2, max2 = min(X2), max(X2)
    X = X1 + X2
    X.sort()
    ans = 0
    for i in range(len(X)-1):
        a, b = X[i], X[i+1]
        c = (a+b) / 2
        if min1 <= c <= max1 and min2 <= c <= max2:
            fa = width(X1, Y1, a) * width(X2, Z2, a)
            fb = width(X1, Y1, b) * width(X2, Z2, b)
            fc = width(X1, Y1, c) * width(X2, Z2, c)
            ans += (b-a) / 6 * (fa+4*fc+fb)
    print(ans)