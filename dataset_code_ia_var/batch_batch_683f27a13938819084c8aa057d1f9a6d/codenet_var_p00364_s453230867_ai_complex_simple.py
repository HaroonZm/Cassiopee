from functools import reduce
from operator import mul
from itertools import starmap, repeat, chain

N, t = map(int, input().split())

ts = list(map(lambda l: list(map(int, l.split())), (input() for _ in range(N))))

def elaborate_max(seq):
    return reduce(lambda a, b: a if a > b else b, seq)

gen_r = (h * t / x for x, h in ts)
result = elaborate_max(gen_r)

print(result)