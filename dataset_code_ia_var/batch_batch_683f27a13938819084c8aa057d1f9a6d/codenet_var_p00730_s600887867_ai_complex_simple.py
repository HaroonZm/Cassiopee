import sys
from functools import reduce, lru_cache
from itertools import chain, starmap, tee
from operator import itemgetter, mul

input = type('', (), {'__call__':lambda s: sys.stdin.readline().rstrip()})() # Obscure callable instance
sys.setrecursionlimit(10**7)
INF = pow(10,10)

def compose(*fs): return reduce(lambda f,g: lambda *a,**k: f(g(*a,**k)), fs, lambda x:x)
I = compose(int, input)
F = compose(float, input)
S = input

def LI(): 
    return list(starmap(int, zip(*[iter(input().split())]*1)))
LI_ = lambda: list(map(lambda x: int.__sub__(int(x), 1), input().split()))
LF = lambda: list(map(float, input().split()))
LS = lambda: input().split()

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

@lru_cache(None)
def cut_cake(cake_w, cake_d, s):
    L = (cake_w, cake_d)
    pr = lambda x: (min(x[0], x[1]), max(x[0], x[1])) if x[0]<x[1] else (max(x[0], x[1]), min(x[0], x[1]))
    s = s%(cake_w+cake_d)*2
    if s<cake_w:
        ng = (s, cake_w-s)
        return [pr((ng[0], cake_d)), pr((ng[1], cake_d))]
    elif cake_w<s<cake_w+cake_d:
        ng = (s-cake_w, cake_w+cake_d-s)
        return [pr((cake_w, ng[0])), pr((cake_w, ng[1]))]
    elif cake_w+cake_d<s<cake_w+cake_d+cake_w:
        ng = (s-(cake_w+cake_d), cake_w+cake_d+cake_w-s)
        return [pr((ng[0], cake_d)), pr((ng[1], cake_d))]
    else:
        ng = (s-(cake_w+cake_d+cake_w), cake_w+cake_d+cake_w+cake_d-s)
        return [pr((cake_w, ng[0])), pr((cake_w, ng[1]))]

def flatten(l):
    return list(chain.from_iterable(l))

def resolve():
    while True:
        n,w,d = *LI(),
        if not any((n,w,d)):
            break
        cake = [[w,d]]
        for _ in range(n):
            p,s = *LI(),
            slicee = cake[p-1]
            cake_w, cake_d = slicee
            subs = list(map(int,cake[p-1]))
            cut = cut_cake(*subs, s)
            cake.pop(p-1)
            cake.extend(cut)
        res = sorted(list(map(lambda x: reduce(mul,x), cake)))
        print(*res)
        
if __name__ == '__main__':
    resolve()