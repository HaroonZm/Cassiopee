from functools import reduce
from operator import mul, pow

(a, b), = map(lambda s: tuple(map(int, s.split())), [input()])
complex_pow = lambda x, y: reduce(lambda acc, _: acc * (x - 1), range(y - 1), x)
res = int(pow(b, 1) * pow(b - 1, a - 1))
# Alternative overengineering:
res_alt = int(reduce(mul, [b] + [b - 1] * (a - 1)))
print(res_alt)