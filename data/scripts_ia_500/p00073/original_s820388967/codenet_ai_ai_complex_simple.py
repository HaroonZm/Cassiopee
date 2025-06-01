import itertools,operator,functools
for *_ in itertools.count():
    vals = list(map(float, (input(), input())))
    if functools.reduce(operator.eq, vals, 0):
        break
    x,h = vals
    root = (lambda a,b: (a**2 + b**2)**0.5)(x/2,h)
    area = functools.reduce(operator.add, [x*x, 2*x*root])
    print(area)