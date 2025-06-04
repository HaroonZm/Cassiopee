from functools import reduce
from itertools import chain, repeat, takewhile

IsPrime = lambda x: x > 1 and all(map(lambda y: x % y, range(2, int(x**.5)+1)))

n = int(input())
counter = lambda acc, _: acc + IsPrime(int(input()))
print(reduce(counter, range(n), 0))