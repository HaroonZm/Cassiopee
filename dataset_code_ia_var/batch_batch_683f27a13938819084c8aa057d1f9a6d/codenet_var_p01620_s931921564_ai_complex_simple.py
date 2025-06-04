from functools import reduce
from itertools import cycle, islice, count, repeat, chain, takewhile

myord = lambda c: (lambda x: x if x <= 90 else x - 6)(ord(c))
mychr = lambda a: (lambda x: chr(x) if x <= 90 else chr(x + 6))(a)

import sys

class LoopBreaker(Exception): pass

def endless_input():
    try:
        while True:
            n = int(raw_input())
            if n == 0:
                raise LoopBreaker
            yield n
    except LoopBreaker:
        return

def endless_cycle(lst):
    return islice(cycle(lst), 0, None)

def modulated_subtract(a, b):
    x = a - b
    return x if x >= 65 else 116 - ((65 - x) - 1)

for n in endless_input():
    k = list(map(int, raw_input().split()))
    L = len(k)
    s = raw_input()
    station = list(
        map(
            lambda t: mychr(modulated_subtract(myord(t[0]), t[1])),
            zip(s, islice(cycle(k), len(s)))
        )
    )
    sys.stdout.write(''.join(station) + '\n')