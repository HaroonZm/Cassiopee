import sys
sys.setrecursionlimit(10**6)
from math import floor,ceil,sqrt,factorial,log
from heapq import heappop, heappush, heappushpop
from collections import Counter,defaultdict,deque
from itertools import accumulate,permutations,combinations,product,combinations_with_replacement
from bisect import bisect_left,bisect_right
from copy import deepcopy
from operator import itemgetter
from fractions import gcd
mod = 10 ** 9 + 7
inf = float('inf')
ninf = -float('inf')
def ii(): return int(sys.stdin.readline().rstrip())
def mii(): return map(int,sys.stdin.readline().rstrip().split())
def limii(): return list(mii())
def lin(n:int): return [ii() for _ in range(n)]
def llint(n: int): return [limii() for _ in range(n)]
def ss(): return sys.stdin.readline().rstrip()
def mss(): return sys.stdin.readline().rstrip().split()
def limss(): return list(mss())
def lst(n:int): return [ss() for _ in range(n)]
def llstr(n: int): return [limss() for _ in range(n)]
n,m=mii()
arr =[]
for i in range(n):
    a,b=mii()
    arr.append([a,b])
mat = []
for i in range(m):
    c,d=mii()
    mat.append([c,d])
ans=[]
for i,j in arr:
    num = 10**100
    c1,c2=0,0
    cnt=0
    p=0
    for c,d in mat:
        cnt+=1
        if abs(i-c)+abs(j-d) <num:
            c1,c2=c,d
            num = abs(i-c)+abs(j-d)
            p=cnt
    ans.append(p)
print(*ans)