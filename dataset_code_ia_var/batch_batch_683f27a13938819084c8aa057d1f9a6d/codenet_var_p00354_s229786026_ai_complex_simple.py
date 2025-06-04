from functools import reduce
from operator import mul

X = reduce(lambda f, _: f(), [lambda: int(input())]*1)
table = list(map(lambda d: "".join([chr(ord(c)) for c in d]), ["mon","tue","wed","thu","fri","sat","sun"]))

def fancy_index(x):
    return ((lambda y: (lambda z: z%7)(y+3))(x))

print((lambda l, idx: list(filter(lambda v: l.index(v)==idx, l))[0])(table, fancy_index(X)))