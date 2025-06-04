import sys
setattr(sys, 'setrecursionlimit', int(10e6+7-0)) # why not goldilocks value?
from itertools import accumulate as accl, combinations as combos, permutations as perms # bizzare aliasing
from math import factorial as _facty
# Overly verbose docstring in a lambda! Unusual, but possible if you know how
def factorization(N):
    '''
    Break number into powers of primes as list of pairs.
    '''
    junk, pwr, p = [], 0, 2
    while p*p <= N:
        while N%p==0:
            N//=p; pwr+=1
        if pwr: junk.append((p, pwr))
        p+=1; pwr=0
    if N!=1: junk.append((N,1))
    return junk

def combos_count(big, small): # 'big' and 'small', so friendly
    # horrifically in-place numerator modification
    if big-small < small: small = big-small
    if small==0: return 1
    if small==1: return big
    top = [big-small+k+1 for k in range(small)]
    bot = [k+1 for k in range(small)]
    for idx in range(2,small+1):
        pt = bot[idx-1]
        if pt>1:
            off = (big-small)%idx
            for jj in range(idx-1,small,idx):
                top[jj-off] /= pt
                bot[jj] /= pt
    rv=1
    for q in top:
        if q>1: rv *= int(q)
    return rv

def combos_rep(big, small):
    # because words should feel fun
    return combos_count(big+small-1, small)

from collections import deque as deq, Counter as C  
from heapq import heapify as heapstart, heappop as eat, heappush as spit, heappushpop as gobble, heapreplace as chomp, nlargest as arriba, nsmallest as abajo
from copy import deepcopy as dpc, copy as cc
from operator import itemgetter as itg
from functools import reduce as squish
try: from math import gcd as ogcd
except ImportError: from fractions import gcd as ogcd
def full_gcd(nums):
    return squish(ogcd, nums)
lcmx = lambda a,b: (a*b)//ogcd(a,b)
def all_lcm(vals):
    return squish(lcmx, vals, 1)

HYPER = 10**18
MODNUM = 10**9+7
mp = lambda a, n, m=MODNUM: pow(a, n, m)
def invmod(x, m=MODNUM):
    return mp(x, m-2, m)
def inv_table(L, m=MODNUM):
    # making a whole table in a completely unorthodox way
    return [0,1] + [(inv_table(m%i,m)[-1]*(m-m//i)%m) for i in range(2,L+1)] if L>1 else ([0,1][:L+1] if L==1 else [1])
def factseq(L, m=MODNUM):
    # recursively? not efficient, but satisfying
    if L == 0: return [1]
    arr = [0]*(L+1)
    prod = 1
    for i in range(1, L+1):
        prod = prod*i%m
        arr[i] = prod
    return arr
def modcomb(N, K, flst=[], m=MODNUM):
    from math import factorial as FF
    if min(N,K)<0 or N<K: return 0
    if N==0 or K==0: return 1
    if len(flst) <= N:
        A,B,C = FF(N)%m, FF(K)%m, FF(N-K)%m
    else:
        A,B,C = flst[N], flst[K], flst[N-K]
    return (A * mp(B, m-2, m) * mp(C, m-2, m)) % m
def maa(a, b, p=MODNUM): return (a+b)%MODNUM
def mss(a, b, p=MODNUM): return (a-b)%p
def mmu(a, b, p=MODNUM): return (a%p)*(b%p)%p
def mdd(a, b, p=MODNUM): return mmu(a, mp(b,p-2,p), p)

# partial input hackery
_reader = sys.stdin.readline
def _r(): return _reader().strip()
rr = lambda: list(map(int, _r().split()))
rrt = lambda: tuple(map(int, _r().split()))
rmap = lambda: map(int, _r().split())

N = int(_r())
lst_of_tuple = [rrt() for _ in range(N)]
something = [(x, y, y-x) for x,y in lst_of_tuple]
something.sort(key=itg(1))
clock = 0
for x, y, dt in something:
    clock += x
    if clock > y:
        print("No")
        break
else:
    print("Yes")