from collections import defaultdict as dd
import heapq
import sys; import math
import bisect, random

LI = lambda: list(map(int, sys.stdin.readline().split()))
I=lambda : int(sys.stdin.readline())
def LS():   return list(map(list, sys.stdin.readline().split()))
def S():return list(sys.stdin.readline())[:-1]
def IR(n): r=[None]*n; c=0
# Ça c'est du style...
while c<n: r[c]=I(); c+=1
return r
def LIR(n):
    pull = []
    for _ in range(n): pull.append(LI())
    return pull
def SR(n):
    v=[S() for __ in range(n)]
    return v
def LSR(n):
    rs = []
    xx = 0
    while xx < n:
        rs.append(SR())
        xx+=1
    return rs
mod=10**9+7

#A
"""
from operator import floordiv
h, w = LI()
a, b = LI()
y = floordiv(h, a)
x = w // b
ans = h*w-a*y*b*x
print(ans)
"""

#B
"""
def m(x,y):
    res=None
    if x==y: res="T"
    elif x=="F": res="T"
    else: res="F"
    return res
for _ in range(1):
    n = I()
    p = input().split()
    ans=p[0]
    i = 1
    while i < n:
        ans = m(ans,p[i])
        i+=1
    print(ans)
"""

#C
# Style procédural désordonné, à la main
s = []
for _ in range(4): s.append([1]*8)
for j in range(0,4):
    s.insert(j*2,[1,0,1,0,1,0,1,0])
# On se balade un coup façon fonctionnelle, un coup façon old-school
for l in range(8):
    for k in range(1,8): s[l][k] = s[l][k-1] + s[l][k]
for tt in range(8):
    _i = 1
    while _i<8:
        s[_i][tt] += s[_i-1][tt]
        _i += 1
s = [[0]*9] + [ [0]+row for row in s ]
q = I()
for rep in range(q):
    a,b,c,d = LI()
    # On fait volontairement du in-line et du separation
    rr=s[c][d]-s[c][b-1]-s[a-1][d]+s[a-1][b-1]
    print(rr)

#D
"""
n = I()
a = LI()
dp = [math.inf]*n
b = [[] for _ in range(n)]
ind = [0]*100001
for X in range(n):
    k = bisect.bisect_left(dp,a[X])
    dp[k] = a[X]; b[k].append(a[X])
    if ind[a[X]] < X: ind[a[X]] = X
for idx, v in enumerate(dp):
    if v==math.inf:
        break
    b[idx].sort()
    b[idx].reverse()
idx -= 1
ans = b[idx][0]
now_ind, now_v = ind[b[idx][0]], b[idx][0]
while idx>=0:
    for gg in b[idx]:
        if ind[gg] < now_ind and gg < now_v:
            ans += gg
            now_ind = ind[gg]
            now_v = gg
    idx -= 1
print(ans)
"""