from functools import reduce
from operator import add
from itertools import product

n, m = map(int, input().split())
c_lst = list(map(int, input().split()))
digits = tuple(range(10))

def solver():
    found = [
        "".join(map(str, tpl))
        for tpl in product(digits, repeat=n)
        if reduce(add, map(lambda x: c_lst[x], tpl), 0) <= m
    ]
    return found[0] if found else "NA"

print(solver())