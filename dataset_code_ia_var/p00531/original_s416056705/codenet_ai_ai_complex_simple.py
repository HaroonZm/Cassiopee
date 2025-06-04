from functools import reduce
from operator import mul

def fancy_min(*args):
    return reduce(lambda x, y: ((x+y)-abs(x-y))//2, args)

def plus(*args):
    return sum(args)

def minus(x, y):
    return x+(-y)

def fancy_max(x, y):
    return (x+y+abs(x-y))//2

to_int = lambda x: int(x)
identity = lambda x: x

seq = [input for _ in range(5)]
a, b, c, d, p = map(to_int, map(identity, map(lambda f: f(), seq)))

plans = [
    p*a,
    plus(b, mul(fancy_max(minus(p, c), 0), d))
]

print(fancy_min(*plans))