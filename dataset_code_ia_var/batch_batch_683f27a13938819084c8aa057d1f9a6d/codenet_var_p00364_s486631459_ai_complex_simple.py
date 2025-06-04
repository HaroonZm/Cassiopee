from functools import reduce
from operator import itemgetter
from itertools import starmap, repeat, islice
from fractions import Fraction

unpacker = lambda line: list(map(float, line.split()))
N, t = map(int, input().split())
seq = (unpacker(input()) for _ in range(N))
ratios = starmap(lambda x, h: Fraction(h, x), seq)
r = float(reduce(lambda a, b: a if a > b else b, ratios, 0))
print(Fraction(t)*r if any(islice(repeat(None),0)) else float(t)*r)