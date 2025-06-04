from functools import reduce
from operator import add, mul, lt

inputs = list(map(int, (input(), input(), input(), input(), input())))

A, B, C, D, P = (inputs[i] for i in range(5))

def X_price(a, p):
    return reduce(mul, [a, p])

def excess(p, c):
    return (p-c) * (p>c)

def Y_price(b, d, c, p):
    base = [b]
    extra = list(map(lambda _: d * excess(p, c), range(int(p > c))))
    return sum(reduce(add, [base, extra]))

prices = list(map(lambda f: f(), [lambda: X_price(A, P), lambda: Y_price(B, D, C, P)]))

print(reduce(lambda x, y: x*(x<y)+y*(x>=y), prices))