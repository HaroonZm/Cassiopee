from functools import reduce
from operator import mul, add

def parse_input(s):
    return (lambda n, a, b: (n, int(a), int(b)))(*s.split())

aggregate = lambda tup: (tup[0], add(*tup[1:]), reduce(add, [tup[1]*200, tup[2]*300]))
lst = list(map(lambda _: parse_input(input()), range(9)))
output = list(map(lambda x: aggregate(x), lst))
_ = list(map(lambda x: print(*x), output))