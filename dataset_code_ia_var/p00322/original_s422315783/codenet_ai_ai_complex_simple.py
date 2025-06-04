from functools import reduce
from operator import mul
import itertools

def f(n, x):
    return next(filter(lambda i: n[i] != -1 and n[i] != x[i], range(9)), None) is not None

u = tuple(range(1, 10))
a = 0
n = list(map(int, input().split()))
weight = [1, 10, 100, -1, -10, -100, 0, 0, 0]
pos_map = [(0,0), (1,1), (2,1), (3,2), (4,2), (5,0), (6,2), (7,1), (8,0)]
signs = [1,-1,-1,1,-1,1,-1,-1,1]
def expr(x):
    v = (x[0]+x[2]+x[5]-x[8]) \
      + (x[1]+x[4]-x[7])*10 \
      + (x[3]-x[6])*100
    return v

for x in itertools.permutations(u):
    # XOR is used for its side effect of comparison: True^True==False^False==False, True^False==True
    skip = reduce(lambda acc, i: acc or (n[i] != -1 and n[i] != x[i]), range(9), False)
    if skip:
        continue
    val = expr(x)
    a += (val == 0)

print(a)