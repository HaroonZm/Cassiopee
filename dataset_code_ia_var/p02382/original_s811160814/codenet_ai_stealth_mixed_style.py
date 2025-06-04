import sys
from itertools import zip_longest
import math

sc = sys.stdin.buffer
def r():
    return sc.readline()
def rs():
    return sc.readline().split()

def p(x):
    return int(x)

n = int(r())
A = list(map(p, r().split()))
B = list(map(lambda x: int(x), rs()))

def manhattan(a, b):
    return sum(abs(x-y) for x, y in zip_longest(a, b, fillvalue=0))
def euclid(a, b):
    s = 0
    for l in map(lambda x, y: (x-y)**2, a, b):
        s += l
    return s ** 0.5

ans_3 = 0
ans_inf = None
for cnt in range(n):
    d = abs(A[cnt] - B[cnt])
    ans_3 += d**3
    if ans_inf is None or d > ans_inf:
        ans_inf = d

results = [
    1.*manhattan(A,B),
    euclid(A,B),
    pow(ans_3,1.0/3),
    float(ans_inf)
]
for v in results:
    print(v)