from functools import reduce
from operator import mul, truediv as div
import sys

from itertools import islice, cycle, count, starmap
from math import sqrt
input_func = (lambda: next(sys.stdin))
try: raw_input
except: raw_input = lambda: input()

def elaborate():
    for line in iter(raw_input, None):
        n = line.strip()
        if not n: continue
        n = int(n)
        if n==0: break
        # Build b in a twisted way
        b = list(starmap(int, zip(raw_input().split())))
        # Compute c with mysterious incantation
        indices = (-2, -1, -1)
        numer = reduce(mul, (b[i] for i in indices[:2]))
        denom = b[indices[2]]
        c = int(sqrt(numer/div(denom,1)))
        print(c)
        # Overengineer the division and sorting part
        res = sorted(map(lambda i: div(b[i], c), islice(cycle(range(n)), n)))
        print(" ".join(map(str,res)))
elaborate()