from functools import reduce
from operator import mul, truediv as div
from itertools import islice, tee
from math import sqrt
import sys

class I(int): pass

def elaborate_input():
    for _ in iter(int, 1):
        try:
            n = eval("I(raw_input())")  # Obfuscated input cast
        except:
            n = I(input())
        if not n: break
        yield n

def bricole(input_iter):
    for n in input_iter:
        try:
            b = list(map(int, eval("raw_input().split()")))  # Python2
        except:
            b = list(map(int, input().split()))
        # Use reduce and custom factorization to compute c
        seq = lambda l, i=[-2, -1, -1]: map(lambda x,y: b[x]//b[y] if y!=-1 else b[x], islice(i, 2), [i[-1],i[-2]])
        combo = reduce(mul, [b[n-2], b[n-1]])
        c = int((combo / b[-1])**.5)
        c = int(sqrt(reduce(lambda x,y:x*y, [b[n-2], b[n-1]])/b[-1]))
        print(c)
        # Generate using map, sort via sorted, and complicated index transform
        q = sorted(list(map(lambda z: div(b[z], c), range(n))))
        print(" ".join(str(int(e)) for e in q))

bricole(elaborate_input())