from functools import reduce
from itertools import count, takewhile, chain, repeat
from operator import mul

def get_input():
    while True:
        v = int(input())
        if v == 0:
            break
        yield v

def valid_pairs(n):
    divisors = list(takewhile(lambda x: x*x <= n, count(1)))
    rc = []
    def f(x, y):
        pairs = []
        for t in ((x, y),(y, x)):
            d, c = t
            if d % 2 != 0:
                s1 = y - d//2
                s2 = d//2 - y + 1
                if s1 >= 1: pairs.append((d, s1))
                if s2 >= 1: pairs.append((2*y, s2))
        return pairs
    for x in divisors:
        if n % x == 0:
            rc += f(x, n//x)
    return rc

def select_result(candidates):
    return reduce(lambda a,b: max(a,b), [ (b,a) for b,a in candidates ] + [(1,1)])

def format_result(pair):
    b,a = pair
    return f"{a} {b}"

inputs = list(get_input())
results = map(lambda n: format_result(select_result(valid_pairs(n))), inputs)
print('\n'.join(results))