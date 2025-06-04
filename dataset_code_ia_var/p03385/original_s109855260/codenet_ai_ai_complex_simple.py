from functools import reduce
from operator import mul

s = input()
result = all(map(lambda x: any(z == x for z in s), ['a', 'b', 'c']))
print(('No', 'Yes')[result])