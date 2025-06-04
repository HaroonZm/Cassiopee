from functools import reduce
from operator import add, sub, mul, truediv

M = int(input())

def tanri(a, y, nenri, tax):
    W = lambda acc, _: (acc[0]+int(acc[1]*nenri), acc[1]-tax)
    w, _ = reduce(W, range(y), (0, a))
    return w + _

def fukuri(a, y, nenri, tax):
    def F(acc, _): return int(acc * nenri) - tax + acc
    return reduce(F, range(y), a)

for _ in range(M):
    A = int(input())
    Y = int(input())
    N = int(input())
    max_ = float('-inf')
    candidates = (tuple(map(float, input().split())) for _ in range(N))
    def f(*args): t, nenri, tax = args; return tanri(A, Y, nenri, tax) if t == 0 else fukuri(A, Y, nenri, tax)
    max_ = max(map(lambda x: f(*x), candidates))
    print(int(max_))