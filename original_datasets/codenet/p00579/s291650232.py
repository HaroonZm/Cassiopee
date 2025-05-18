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
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
from math import floor,ceil,sqrt,factorial,log #log2ないｙｐ
from heapq import heappop, heappush, heappushpop
from collections import Counter,defaultdict,deque
from itertools import accumulate,permutations,combinations,product,combinations_with_replacement
from bisect import bisect_left,bisect_right
from copy import deepcopy
inf=float('inf')
mod = 10**9+7
def pprint(*A): 
    for a in A:     print(*a,sep='\n')
def INT_(n): return int(n)-1
def MI(): return map(int,input().split())
def MF(): return map(float, input().split())
def MI_(): return map(INT_,input().split())
def LI(): return list(MI())
def LI_(): return [int(x) - 1 for x in input().split()]
def LF(): return list(MF())
def LIN(n:int): return [I() for _ in range(n)]
def LLIN(n: int): return [LI() for _ in range(n)]
def LLIN_(n: int): return [LI_() for _ in range(n)]
def LLI(): return [list(map(int, l.split() )) for l in input()]
def I(): return int(input())
def F(): return float(input())
def ST(): return input().replace('\n', '')
def main():
    N,M=MI()
    A=LI()
    LR = []
    for _ in range(M):
        l,r = MI_()
        LR.append((l,r))
    LR.sort()
    NG_left = [i for i in range(N)]
    index = 0
    for l,r in LR:
        for i in range(max(index, l), r+1):
            NG_left[i] = l
            index = i+1
    # print(NG_left)
    dp = [0]*N #dp[i]:= i番目までの木で実現できる明るさ
    dp[0] = A[0]
    for i in range(1,N):
        if NG_left[i]==0:
            dp[i] = max(dp[i-1], A[i])
        else:
            dp[i] = max(dp[i-1], A[i] + dp[NG_left[i]-1])
    print(dp[-1])

if __name__ == '__main__':
    main()

"""##GREEDY check -> NG
N,M=MI()
A=LI()
LR = []
for _ in range(M):
    l,r = MI_()
    LR.append((l,r))
ng = set()
B=[(a,i) for i,a in enumerate(A)]
B.sort(reverse=True)
ans = 0
for a,i in B:
    if i in ng:
        continue
    for l,r in LR:
        for j in range(l,r+1):
            ng.add(j)
    ans+=a
print(ans)"""