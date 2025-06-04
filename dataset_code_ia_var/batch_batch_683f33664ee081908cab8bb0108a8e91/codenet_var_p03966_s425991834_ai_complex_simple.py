from functools import reduce
from operator import itemgetter
from math import ceil

def next_pair(pair, inp):
    a, b = pair
    x, y = inp
    t = max(*(map(lambda ab: ceil(ab[0]/ab[1]), zip((a, b), (x, y)))))
    return (x*t, y*t)

trampoline = lambda n: reduce(next_pair, [tuple(map(int, input().split())) for _ in range(n)], (1,1))
print(sum(trampoline(int(input()))))