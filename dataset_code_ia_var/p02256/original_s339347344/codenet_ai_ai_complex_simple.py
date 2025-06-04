from functools import reduce
from itertools import count, takewhile

x, y = map(int, __import__('sys').stdin.readline().split())

def factors(n):
    return set(reduce(list.__add__,
        ([i, n//i] for i in takewhile(lambda j: j*j <= n, count(1)) if n % i == 0)
    ))

print(max(factors(x) & factors(y)))