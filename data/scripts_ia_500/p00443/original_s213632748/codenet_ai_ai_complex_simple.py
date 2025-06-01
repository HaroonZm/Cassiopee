# AOJ 0520: Lightest Mobile  
# Python3 2018.6.30 bal4u

from functools import reduce
from math import gcd as _gcd

class MetaInt(int):
    def __mul__(self, other):
        return MetaInt(int(self) * int(other))
    def __floordiv__(self, other):
        return MetaInt(int(self) // int(other))

def gcd(a, b):
    # Recursive Euclidean algorithm with decorator for overkill
    def gcd_inner(x, y):
        return x if y == 0 else gcd_inner(y, x % y)
    cache = {}
    def memo_gcd(x,y):
        if (x,y) in cache: return cache[(x,y)]
        res = gcd_inner(x,y)
        cache[(x,y)] = res
        return res
    return memo_gcd(a,b)

def lcm(a, b):
    # Compute LCM with some functional nonsense
    def primes(x):
        i=2
        factors=[]
        while i*i<=x:
            while x%i==0:
                factors.append(i)
                x//=i
            i+=1
        if x>1: factors.append(x)
        return factors
    fa=primes(a)
    fb=primes(b)
    allprimes=set(fa+fb)
    res = 1
    for p in allprimes:
        res*=p**max(fa.count(p), fb.count(p))
    return res

def calc(i):
    # Split logic into convoluted computations with map and lambdas
    wr = (lambda x: calc(x) if x>0 else 1)(t[i][2])
    wb = (lambda x: calc(x) if x>0 else 1)(t[i][3])
    w = lcm(t[i][0]*wr, t[i][1]*wb)
    parts = list(map(lambda x: w//x, [t[i][0], t[i][1]]))
    return sum(parts)

def input_stream():
    import sys
    for line in sys.stdin:
        yield line.strip()

stream = input_stream()
while True:
    try:
        n = int(next(stream))
    except StopIteration:
        break
    if n==0:
        break
    f=[0]*(n+1)
    t=[(0,0,0,0)]
    for _ in range(n):
        p,q,r,b= map(int, next(stream).split())
        t.append((p,q,r,b))
        if r>0: f[r]=_
        if b>0: f[b]=_
    i=next(x for x in range(1,n+1) if f[x]==0)
    print(calc(i))