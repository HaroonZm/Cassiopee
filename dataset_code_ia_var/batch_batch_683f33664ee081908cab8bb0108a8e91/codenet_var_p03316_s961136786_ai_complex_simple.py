from functools import reduce
from operator import floordiv, mod, add

n = int(__import__('builtins').input())
digits = list(map(int, filter(str.isdigit, str(n))))
divisible = (lambda s, n: not mod(n, s))
print(('No', 'Yes')[divisible(reduce(add, digits, 0), n)])