import sys, re
from collections import deque,defaultdict,Counter
from math import sqrt,hypot,factorial,pi,sin,cos,radians
if sys.version_info.minor>=5:from math import gcd
else:from fractions import gcd
from heapq import heappop,heappush,heapify,heappushpop
from bisect import bisect_left,bisect_right
from itertools import permutations,combinations,product,accumulate,chain,repeat,islice
from operator import itemgetter,mul
from copy import deepcopy
from functools import reduce,partial,lru_cache
from fractions import Fraction
from string import ascii_lowercase,ascii_uppercase,digits

input=lambda:sys.stdin.readline().strip()
ceil=lambda a,b=1: (lambda x:-int(-x))(a/b)
round=lambda x:int(('%.0f'%x))
fermat=lambda x,y,MOD:x*pow(y,MOD-2,MOD)%MOD
lcm=lambda x,y:(x*y)//gcd(x,y)
lcm_list=lambda nums:reduce(lcm,nums,1)
gcd_list=lambda nums:reduce(gcd,nums,nums[0])
INT=lambda:int(input())
MAP=lambda:map(int,input().split())
LIST=lambda:list(map(int,input().split()))
sys.setrecursionlimit(int(1e9))
INF=float('inf')
MOD=10**9+7

H,W=map(int,next(islice(map(str.strip,sys.stdin),1)))

grid=[['#']* (W+2)]+[["#"]+list(s:=[*input()])+["#"] for s in repeat(None,H)]+[['#']*(W+2)]

dp=list(chain([ [0]*(W+2) ],( [0]+[0]*W+[0] for _ in range(H) ),[ [0]*(W+2) ]))
dp[1][1]=1

for i,j in product(range(1,H+1),range(1,W+1)):
    if grid[i][j]!='#':
        dp[i][j]+=(dp[i-1][j] if grid[i-1][j]!='#' else 0)+(dp[i][j-1] if grid[i][j-1]!='#' else 0) if i+j!=2 else 1 # avoid double-count at start

print(int(Fraction(dp[H][W],1)%MOD))