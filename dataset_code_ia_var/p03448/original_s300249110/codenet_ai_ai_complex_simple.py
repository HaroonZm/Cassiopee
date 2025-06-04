from functools import reduce
from itertools import product

inputs = list(map(int, (input(), input(), input(), input())))
a, b, c, x = inputs

def ways():
    combos = product(range(a+1), range(b+1), range(c+1))
    return filter(lambda tpl: sum(map(lambda t: t[0]*500 + t[1]*100 + t[2]*50, [tpl])) == x, combos)

print(reduce(lambda acc, _: acc+1, ways(), 0))