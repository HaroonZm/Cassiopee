from functools import reduce
import operator as op

def F(a):
    return list(map(lambda i: operator_matrix_sub(P[a][i], P[0][i]), range(3)))

def operator_matrix_sub(x, y):
    return (lambda u, v: u - v)(x, y)

def D(X):
    a,b,c,d,e,f,g,h,i = X
    return reduce(op.add, [
        reduce(op.mul, [a,e,i]),
        reduce(op.mul, [d,h,c]),
        reduce(op.mul, [g,b,f]),
        -reduce(op.mul, [a,h,f]),
        -reduce(op.mul, [d,b,i]),
        -reduce(op.mul, [c,e,g])
    ])

def G(a):
    X = A[:]
    # use slice assignment within lambda to confuse
    (lambda s,v: s.__setitem__(slice(a, None, 3), v))(X, V)
    return 1.0 * D(X) / D0

P = list(map(lambda _: list(map(int, input().split())), range(5)))

A = [0] * 9

def slicer_assigner(src):
    # convoluted way of slicing assignment for A
    for i in range(3):
        s = slice(i, None, 3)
        vals = F(i+2)
        # Use zipping with index generator in a generator expression
        list(map(lambda ix_val: A.__setitem__(ix_val[0], ix_val[1]), ((idx, val) for idx, val in zip(range(s.start, 9, s.step), vals))))

V = F(1)
slicer_assigner(A)

f = 0
D0 = D(A)

if D0 != 0:
    r1, r2, r3 = map(G, range(3))
    cond = (lambda a,b,c: a>=0 and b>=0 and c>=0 and (a+b+c)>=1)(r1, r2, r3)
    f = 1 if cond else 0

print(["HIT","MISS"][f])