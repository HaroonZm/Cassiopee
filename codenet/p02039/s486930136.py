#!usr/bin/env python3
from collections import defaultdict
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS():return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]
def IR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = I()
    return l
def LIR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = LI()
    return l
def SR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = S()
    return l
def LSR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = SR()
    return l
mod = 1000000007

#A
"""
h,w = LI()
a,b = LI()
y = h//a
x = w//b
ans = h*w-a*y*b*x
print(ans)
"""

#B
"""
def m(x,y):
    if x == y:
        return "T"
    if x == "F":
        return "T"
    return "F"
n = I()
p = input().split()
ans = p[0]
for i in range(1,n):
    ans = m(ans,p[i])
print(ans)
"""

#C
s = [[1]*8 for i in range(4)]
for i in range(4):
    s.insert(2*i,[1,0,1,0,1,0,1,0])
for j in range(8):
    for i in range(1,8):
        s[j][i] += s[j][i-1]
for j in range(8):
    for i in range(1,8):
        s[i][j] += s[i-1][j]
s.insert(0,[0,0,0,0,0,0,0,0,0])
for i in range(1,9):
    s[i].insert(0,0)
q = I()
for _ in range(q):
    a,b,c,d = LI()
    print(s[c][d]-s[c][b-1]-s[a-1][d]+s[a-1][b-1])

#D
"""
n = I()
a = LI()
dp = [float("inf") for i in range(n)]
b = [[] for i in range(n)]
ind = [0 for i in range(100001)]
for i in range(n):
    k = bisect.bisect_left(dp,a[i])
    dp[k] = a[i]
    b[k].append(a[i])
    ind[a[i]] = max(i,ind[a[i]])
for i in range(n):
    if dp[i] == float("inf"):break
    b[i].sort()
    b[i] = b[i][::-1]
i -= 1
ans = b[i][0]
now_ind = ind[b[i][0]]
now_v = b[i][0]
while i >= 0:
    for j in b[i]:
        if ind[j] < now_ind and j < now_v:
            ans += j
            now_ind = ind[j]
            now_v = j
    i -= 1
print(ans)
"""
#E

#F

#G

#H

#I

#J

#K

#L

#M

#N

#O

#P

#Q

#R

#S

#T