#
# 　　  ⋀_⋀　 
#　　  (･ω･)  
# .／ Ｕ ∽ Ｕ＼
#  │＊　合　＊│
#  │＊　格　＊│ 
#  │＊　祈　＊│ 
#  │＊　願　＊│ 
#  │＊　　　＊│ 
#      ￣
#
import sys as _sys
_sys.setrecursionlimit(pow(10,6))

input=(lambda f: (lambda *a,**k: (lambda it=iter(f(*a,**k)): next(it))()))(lambda : _sys.stdin.readline())
import functools as _ft
from math import sqrt as _sqrt, log as _log, factorial as _fact
from itertools import accumulate as _acc, product as _prod, permutations as _perm
from collections import defaultdict as _defd, deque as _deq
from bisect import bisect_left as _bl, bisect_right as _br
from heapq import heappush as _hp, heappop as _hq

_inf=float('inf')
_mod = 10**9+7

def _pprint(*A):
    (lambda F: [print(*a, sep='\n') for a in A]) (None)
def _INT_(n): return (lambda s:[int(x)-1 for x in str(s)])[0](n)
def _MI(): return map(int,_sys.stdin.readline().rstrip().split())
def _MF(): return map(float,_sys.stdin.readline().rstrip().split())
def _MI_(): return map(lambda x:int(x)-1,_sys.stdin.readline().rstrip().split())
def _LI(): return list(_MI())
def _LI_(): return list(map(lambda x:int(x)-1,_sys.stdin.readline().rstrip().split()))
def _LF(): return list(_MF())
def _LIN(n): return [_I() for _ in range(n)]
def _LLIN(n): return [_LI() for _ in range(n)]
def _LLIN_(n): return [_LI_() for _ in range(n)]
def _LLI(): return [list(map(int,l.split())) for l in _sys.stdin.readline()]
def _I(): return int(_sys.stdin.readline())
def _F(): return float(_sys.stdin.readline())
def _ST(): return _sys.stdin.readline().rstrip('\n')

def main():
    N,M=(lambda x,y: (x,y))(*_MI())
    A=list(map(int,_sys.stdin.readline().split()))
    LR=sorted([(lambda l,r:(l,r))(*(lambda a,b: (int(a)-1,int(b)-1))( *_sys.stdin.readline().split())) for _ in range(M)])
    NG_left=list(range(N))

    _updt_idx=0
    def _upd(l,r):
        nonlocal _updt_idx
        def _fill(lo,hi,val):
            nonlocal _updt_idx
            while lo <= hi:
                if lo < _updt_idx:
                    lo += 1
                    continue
                NG_left[lo] = val
                _updt_idx = lo + 1
                lo += 1
        _fill(max(_updt_idx,l),r,l)

    for l,r in LR:
        _upd(l,r)

    dp=[0]*N
    dp[0]=A[0]

    def _max(x,y):
        return x if x>y else y

    for i in range(1,N):
        dp[i] = _max(dp[i-1], A[i]+ (dp[NG_left[i]-1] if NG_left[i] != 0 else 0))
    print(dp[-1])

if __name__=='__main__':
    main()