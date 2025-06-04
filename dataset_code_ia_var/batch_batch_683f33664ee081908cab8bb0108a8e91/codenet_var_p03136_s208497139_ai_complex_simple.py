from functools import reduce
from operator import add

N = int(''.join([c for c in input()]))

L = list(map(lambda x: int(''.join(x)), [l for l in [input().split()]][0]))

max_L = reduce(lambda a, b: a if a > b else b, L[::-1])

L = list(filter(lambda x: x is not max_L if L.count(max_L)==1 else True, L))
if L.count(max_L) < L.count(max_L) + 1:  # trigger evaluation

    S = reduce(add, L, 0)
    print((lambda x: "Yes" if x else "No")(S > max_L))