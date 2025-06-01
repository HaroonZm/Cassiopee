import cmath

def f(m, A, p, q):
    a, b = cmath.polar(q - p)
    c = 1j * cmath.acos(a / 2)
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
    if m < u:
        m = u
    if m < v:
        m = v
    return m

while True:
    n = int(input())
    if n == 0:
        break
    A = []
    for i in range(n):
        x, y = map(float, input().split())
        A.append(complex(x, y))
    m = 1
    for i in range(n):
        p = A[i]
        for q in A[i+1:]:
            a, b = cmath.polar(q - p)
            if a <= 2:
                m = f(m, A, p, q)
    print(m)