from functools import reduce
from itertools import combinations,repeat,starmap,chain
from operator import add
from math import hypot

n = int(input())
ls = list(starmap(lambda *args: list(map(int,args)),*(zip(*(input().split() for _ in range(n))))))

coords = list(zip(*ls))
points = list(zip(*coords))
pairs = list(combinations(range(n),2))
dists = list(starmap(lambda i,j: hypot(points[i][0]-points[j][0], points[i][1]-points[j][1]), pairs))
s = reduce(add, dists, 0)
b = s/(len(pairs))
print(b*(n-1))