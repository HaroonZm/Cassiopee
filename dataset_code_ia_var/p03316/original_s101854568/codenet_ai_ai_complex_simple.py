from functools import reduce
from operator import add

n = int(input())
digits = map(int, str(n))
s = reduce(lambda x, y: add(x, y), digits, 0)
print(('No', 'Yes')[divmod(n, s)[1] == 0])