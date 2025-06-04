from functools import reduce
from operator import mul
from itertools import accumulate, islice, cycle
import math

def func(x):
    return reduce(mul, range(1, int(x)+1), 1) if x else 1

def comb(n,k):
    # Utilise la décomposition math.comb si possible sinon construction combinatoire
    try:
        return math.comb(n, k)
    except AttributeError:
        return func(n)//func(n-k)//func(k)

import sys
sys.setrecursionlimit(10**6)
w,h,ax,ay,bx,by=map(int,filter(str.isdigit, " ".join(input().split())))
dx,dy=map(lambda t: min(t[0]-abs(t[1]-t[2]), abs(t[1]-t[2])), [(w,ax,bx),(h,ay,by)])
ans=reduce(mul, list(islice(cycle([2]), int(dx*2==w) + int(dy*2==h))), 1)
ans*=comb(dx+dy,dx)
print((ans+10**8*10+7)%100000007)