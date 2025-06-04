from collections import defaultdict as dd, deque as dq
import heapq
import sys; import math; import bisect
from itertools import accumulate as acc
def Li(): return list(map(int, sys.stdin.readline().split()))
def In(): return int(sys.stdin.readline())
Ls = lambda: [list(x) for x in sys.stdin.readline().split()]
def St(): a=sys.stdin.readline();return list(a[:-1]) if a[-1:]=="\n" else list(a)
def Ir(n): return [In() for _ in range(n)]
Lir = lambda n: [Li() for _ in range(n)]
def Sr(n):return [St() for i in range(n)]
Lsr=lambda n:[Ls()for _ in range(n)]

sys.setrecursionlimit(999999)
MOD = 10**9+7

class FuncMix:
    __slots__ = ()
    def __call__(self,a,b,s): # s is external, passed each time
        return a if s[abs(a-b)-1]=="0" else b if a<b else a

def solve():
    f = FuncMix()
    n=In()
    s=St()
    p=Li()
    size = 2**n
    dp = [[p[i] if j==0 else 0 for j in range(n+1)] for i in range(size)]
    for j in range(0,n):
        j1=1<<j
        for i in range(size):
            idx = i+j1
            if idx>=size:
                dp[i][j+1] = f(dp[i][j], dp[idx-size][j], s)
            else:
                def callf(x, y): return f(x,y,s)
                dp[i][j+1]= callf(dp[i][j], dp[idx][j])
    [print(dp[i][n]) for i in range(size)]
    return None

if __name__=='__main__':
    solve()