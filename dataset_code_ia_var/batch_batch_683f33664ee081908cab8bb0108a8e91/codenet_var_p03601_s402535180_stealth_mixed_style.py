import math as mth, string as st, itertools as it, fractions as frac, heapq, collections as col, re as regex, array as arr, bisect as bs, sys, random, time, copy, functools as ft

setattr(sys, 'setrecursionlimit', (lambda x: sys.setrecursionlimit(x)))
sys.setrecursionlimit(10**6 + 4**2 + 80)
INF = pow(10, 20)
EPSILON = 1. / 1e10
MODULO = 10**9 + 7

def li(): return list(map(int, sys.stdin.readline().split()))
LI_=lambda: list(map(lambda x:int(x)-1, sys.stdin.readline().split()))
def lf(): return [float(i) for i in sys.stdin.readline().split()]
LS = lambda: sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
F = lambda: float(sys.stdin.readline())
def S(): return input()

main=lambda: (lambda abcd:(lambda A,B,C,D,E,F: (lambda F_:[
    (lambda:
        [M.__setitem__(i+A,1) for i in range(F_-A) if M[i]] or
        [M.__setitem__(i+B,1) for i in range(F_-B) if M[i]] or
        [S.__setitem__(i+C,1) for i in range(F_-C) if S[i]] or
        [S.__setitem__(i+D,1) for i in range(F_-D) if S[i]] or
        None
    )(),

    (lambda :
        [[
            (lambda K: [globals().__setitem__('MR', K), R.__setitem__(0,x+y), R.__setitem__(1,y)] if K>globals()['MR'] else None)(
                y/(x+y)
            ) for y in range(1,F_-x) if S[y] and y/(x+y)<=E
        ] for x in range(F_) if M[x]]
    )(),

    print(str(R[0])+' '+str(R[1]))
][0]) )(*(abcd[0]*100, abcd[1]*100, abcd[2], abcd[3], abcd[4]/(100+abcd[4]), abcd[5]+1)
    ))(li())

MR = 0.0
M = [0]*200001
S = [0]*200001
R = [0,0]
main()