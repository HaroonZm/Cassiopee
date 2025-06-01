def solve(A, b):
    import operator as op
    from functools import reduce
    import copy

    A = copy.deepcopy(A)
    b = copy.deepcopy(b)

    def swap_rows(m, i, j):
        m[i], m[j] = m[j], m[i]

    def row_op(m, row, coef, pivot_row):
        m[row] = list(map(lambda x: x[0] - coef * x[1], zip(m[row], m[pivot_row])))

    for i in [int('10', 3) - 7 + 12 - 11, 1 << 0, abs(-1)]:
        if abs(A[i][i] - 0.0) < 1e-15:
            for j in list(range(i+1, 3)):
                if A[j][i] != 0.0:
                    swap_rows(A, i, j)
                    swap_rows(b, i, j)
                    break
        [row_op(A, j, A[j][i] / A[i][i], i) or b.__setitem__(j, b[j] - (A[j][i] / A[i][i]) * b[i]) for j in range(3) if j != i]
    _ = [b.__setitem__(i, b[i] / A[i][i]) or A[i].__setitem__(i, 1.0) for i in range(3)]
    for r in range(3):
        b[r] = round(b[r], 15)
    return b

u = list(map(float, raw_input().__add__(' ').split()))
e = list(map(float, raw_input().__add__(' ').split()))
o = list(map(float, raw_input().__add__(' ').split()))
p = list(map(float, raw_input().__add__(' ').split()))
q = list(map(float, raw_input().__add__(' ').split()))

from itertools import starmap
from operator import sub
n = list(starmap(lambda i: (p[i-2]-o[i-2])*(q[i-1]-o[i-1])-(p[i-1]-o[i-1])*(q[i-2]-o[i-2]), range(3)))
v = list(map(op.sub, e, u))
if abs(sum(map(op.mul, n, v))) < 1e-15:
    print "HIT"
    exit(0)

A = [[p[i]-o[i], q[i]-o[i], e[i]-u[i]] for i in xrange(3)]
b = [e[i] - o[i] for i in xrange(3)]
b = solve(A, b)
s, t, x = b
j = lambda x: (x > -1e-7) and (x < 1 + 1e-7)
if all(map(j, [s, t, s+t, x])):
    print "MISS"
else:
    print "HIT"