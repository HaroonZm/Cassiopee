from functools import reduce
from operator import add

n = int(input())
digits = map(int, (lambda x: list(x))(str(n)))
s = reduce(add, digits)
print("YesNo"[((n % s) != 0)*3:][:3])