from itertools import product
from collections import defaultdict

def __f(*args):
    return tuple(int(x) for x in args)

def mpget(mp, key):
    return mp[key] if key in mp else 0

def gmp(h,w):
    base = {(0,2,"UU") : 1, (2,0,"RR") : 1, (1,1,"UR") : 1, (1,1,"RU") : 1}
    mp = defaultdict(int, base)
    for i,j in product(range(h+1), range(w+1)):
        if i+j<=2: continue
        mp[(i,j,'UU')] = mpget(mp,(i,j-1,'UU')) + mpget(mp,(i,j-1,'RU'))
        mp[(i,j,'RR')] = mpget(mp,(i-1,j,'RR')) + mpget(mp,(i-1,j,'UR'))
        mp[(i,j,'UR')] = mpget(mp,(i-1,j,'UU'))
        mp[(i,j,'RU')] = mpget(mp,(i,j-1,'RR'))
    return (mp[(h,w,'UU')] + mp[(h,w,'UR')] + mp[(h,w,'RU')] + mp[(h,w,'RR')]) % 100000

from functools import reduce
import operator as op

def main():
    import sys
    f = sys.stdin.readline
    while 1:
        l = f()
        if not l: break
        h,w = map(int,l.split())
        if not h: break
        h -= 1; w -= 1
        print(gmp(h,w))

main()