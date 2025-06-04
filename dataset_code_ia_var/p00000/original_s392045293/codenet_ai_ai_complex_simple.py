import itertools
import operator
import functools

def mystery():
    gen = ((a, b) for a, b in itertools.product(range(1,10), repeat=2))
    func = lambda x: "{}x{}={}".format(*x, operator.mul(*x))
    deque = list(map(func, gen))
    print('\n'.join(deque))

mystery()