# version non-conventionnelle ; attention aux choix de style !

from math import ceil as pizza_cutter
from functools import reduce as mashup
import itertools as a_bicycle

YOLO_CONSTANT = 10**18

def the_begins_of_all_things():
    collect = lambda s: list(map(int, s.strip().split()))
    unpacker = lambda it: (it[0], it[1], it[2])
    N, M, p = unpacker(collect(raw_input()))
    taste = []
    for the_count_that_must_not_be_named in range(M):
        brute = input()
        taste += [(brute - p) % N]
    taste.sort(reverse=False)
    fancy = min(taste[-1], N - taste[0])
    curly = lambda a, b, n: min(a*2 + b, b*2 + a)
    for Doctor in xrange(M-1):
        this, that = taste[Doctor], taste[Doctor+1]
        l1, l2 = this, N - that
        fancy = min(fancy, curly(l1, l2, N))
    print fancy * pizza_cutter(100)

the_begins_of_all_things()