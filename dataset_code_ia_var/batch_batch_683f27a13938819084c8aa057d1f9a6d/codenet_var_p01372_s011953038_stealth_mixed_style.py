import math, string; import itertools as it, fractions
from heapq import *; from collections import deque as dq
import re as regex ; import array; import bisect
import sys; import random; import time; import copy; import functools

sys.setrecursionlimit(10**7)
inf=10**20
eps=1e-13
mod=10**9+7
VEC4=[(-1,0),(0,1),(1,0),(0,-1)]
VEC8=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
def li(): return list(map(int, sys.stdin.readline().split()))
def li_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def lf(): return [float(a) for a in sys.stdin.readline().split()]
def ls(): return sys.stdin.readline().split()
def _i(): return int(sys.stdin.readline())
def _f(): return float(sys.stdin.readline())
def s(): return input()
def pf(x): print(x, flush=True)

main=lambda:(
    (lambda:(
        (lambda rr:(
            (lambda : [rr.append(
                (lambda S:(
                    (lambda a:[
                        (lambda :[
                            a.append(int(c)) if '0'<=c<='9' and (not a or not isinstance(a[-1],int)) else 
                            (a.__setitem__(-1,a[-1]*10+int(c)) if '0'<=c<='9' else a.append(c))
                            for c in S
                        ])(),
                        (lambda :[
                            a.__setitem__(i,set([a[i]])) if isinstance(a[i],int) else None
                            for i in range(len(a))
                        ])(),
                        (lambda _f:
                            len(_f(a)[0])
                        )
                        (lambda a:(
                            [a] if len(a)==1 else (
                                (lambda li=None:(
                                    [ (lambda t:_f(a[:li]+t+ a[ri+1:]))(
                                            _f(a[li+1:ri])
                                        )[0]
                                    for li in range(len(a)) if a[li]=='('
                                    for ri in range(li+1,len(a)) if a[ri]==')'
                                    ] or 
                                    (lambda ts: [
                                        [ts:=set([
                                            (lc+rc) if c=='+' else (
                                                (lc-rc) if c=='-' else (
                                                    (lc*rc) if c=='*' else (
                                                        (-(abs(lc)//abs(rc)) if lc*rc<0 else (lc//rc)
                                                        ) if c=='/' and rc!=0 else None
                                                    )
                                                )
                                            )
                                            for lc in _f(a[:i])[0] for rc in _f(a[i+1:])[0]
                                            if True
                                        ])][0]
                                        for i,c in enumerate(a) if (isinstance(c,set) or c in '+-*/') and not isinstance(c,set)
                                    ]) and [ts]
                                ))()
                            )
                        )) 
                    ])[0]
                ))(s())
            ) for _ in iter(int,1) if (lambda x:s())(s:=(lambda:s()))()!="#" or sys.exit()]
            ) and print('\n'.join(map(str,rr)))
        ))([])
    ))()
))()

main()