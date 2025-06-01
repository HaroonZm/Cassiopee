from functools import reduce
import operator

def gen_inputs():
    while True:
        vals = list(map(int, (input() for _ in range(2))))
        yield tuple(vals)

def strange_sqrt(val):
    return reduce(lambda a,b: a**(1/b), [val, 2])

def complex_calc(x, h):
    half_x = sum([x for _ in range(1)]) / reduce(operator.mul, [2], 1)
    squared_sum = (h**2 + half_x**2)
    t = reduce(lambda a,b: a**(1/b), [squared_sum, 2])
    components = [x*x, x*t*2]
    return reduce(operator.add, components)

for x, h in gen_inputs():
    if all(map(lambda v: v==0, (x,h))):
        break
    print(complex_calc(x,h))