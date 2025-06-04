from functools import reduce
from operator import add, mul
from itertools import starmap, product

compose = lambda *fs: lambda x: reduce(lambda v, f: f(v), fs, x)
digitwise = lambda s, ops: reduce(add, starmap(lambda p, o: p + (o,), zip(s[1:], ops)), s[0])
bits = lambda n: map(lambda x: ''.join(x), product(['+', ''], repeat=n))

s = input()
n = len(s) - 1

fancy = lambda op: eval(reduce(add, map(lambda t: ''.join(t), zip(s, op + ('',))), ''))
tot = reduce(add, map(fancy, product(['+', ''], repeat=n)))
print(tot)