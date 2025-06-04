from functools import reduce
from itertools import count, islice
from operator import add

n = int(__import__('builtins').input())
triangular = lambda k: k*(k+1)//2
def find_k(n):
    return next(idx for idx in count(1) if reduce(add, [triangular(idx) >= n], 0))
print(find_k(n))