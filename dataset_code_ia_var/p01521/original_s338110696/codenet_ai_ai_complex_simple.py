from functools import reduce
from operator import mul

s = input()
print((lambda f: f(s))(lambda t: reduce(lambda a, b: b if t[0] == 'o' else a, [t[-1], 'o'])))