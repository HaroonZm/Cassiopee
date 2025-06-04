import math
import cmath

def f(m):
    c = 1j * math.acos(a / 2)
    r = cmath.exp(b + c) + p
    s = cmath.exp(b - c) + p
    u = 2
    v = 2
    for t in A:
        if t == p or t == q:
            continue
        if abs(abs(t - r) - 1) < 1e-6:
            u += 1
        if abs(abs(t - s) - 1) < 1e-6:
            v += 1
    return max(m, u, v)

while True:
    n = int(input())
    if n == 0:
        break
    N = range(n)
    A = []
    for i in N:
        x, y = map(float, input().split())
        A.append(x + 1j * y)
    m = 1
    for i in N:
        p = A[i]
        for q in A[i+1:]:
            a, b = cmath.polar(q - p)
            b = b * 1j
            if a <= 2:
                m = f(m)
    print(m)