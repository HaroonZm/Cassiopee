from functools import reduce
from operator import mul

a = int(input())

def is_even(n):
    # via all, any and unorthodox boolean logic
    return all(map(lambda x: x==0, [n%2]))

def double_if_odd(n):
    return reduce(mul, [n, 2]) if not is_even(n) else n

print([double_if_odd(a), a][is_even(a)])