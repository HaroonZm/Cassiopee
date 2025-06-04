from functools import reduce
from operator import sub, mul
coords = [tuple(map(int, input().split())) for _ in range(3)]
diffs = [[sub(*p) for p in zip(coords[i], coords[(i+1)%3])] for i in range(3)]
lengths = [sum(map(lambda x: x**2, d))**.5 for d in diffs]
triple = [[*coords[i], *coords[j], *coords[k]] for i,j,k in [(0,1,2)]][0]
area = abs(reduce(sub, (mul(*p) for p in zip(triple[::2], triple[1::2]))))
radius = area / sum(lengths)
f = lambda l: l*radius/(2*radius+l)
print(f(max(lengths)))