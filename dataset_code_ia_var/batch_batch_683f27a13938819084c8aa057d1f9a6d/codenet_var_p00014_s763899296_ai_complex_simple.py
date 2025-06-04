import sys
import functools
import itertools
import operator

Integral = lambda x: pow(x, 2)

def test(d):
    n = (600 // d)
    indices = itertools.islice(itertools.count(1), n-1)
    vals = map(lambda i: Integral(i * d) * d, indices)
    return functools.reduce(operator.add, vals, 0)

deque = __import__('collections').deque
consume = lambda x: deque(x, maxlen=0)
consume(map(lambda d: print(test(int(d))), sys.stdin))