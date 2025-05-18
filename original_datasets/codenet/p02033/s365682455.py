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
n,m = LI()
a = LI()
b = LI()
li = list(set(a)|set(b))
li2 = list(set(a)&set(b))
li.sort()
li2.sort()
print(len(li2),len(li))
for i in li2:
    print(i)
for i in li:
    print(i)
"""

#B
"""
n = I()
p = LI()
ans = [None for i in range(2*n)]
ind = [i for i in range(n)]
for i in range(n):
    ind[p[i]-1] = i
l = 0
print(ind)
for i in range(n):
    while ans[l] != None:l += 1
    ans[l] = "("
    r = n+ind[i]
    while ans[r] != None:r += 1
    ans[r] = ")"
    print(ans)
k = []
q = []
a = 1
print(ans)
for i in range(2*n):
    if ans[i] == "(":
        q.append(a)
        a += 1
    else:
        k.append(q.pop(-1))
if k != p:
    print(":(")
else:
    for i in range(2*n-1):
        print(ans[i],end = "")
    print(ans[-1])
"""

#C
"""
def fact(n):
    i = 2
    a = n
    if n < 4:
        return [1,n],[n]
    li = [1,n]
    while i**2 <= a:
        if n%i == 0:
            li.append(i)
            if i != n//i:
                li.append(n//i)
        i += 1
    li.sort()
    i = 2
    if len(li) == 2:
        return li,[a]
    k = []
    b = a
    while i**2 <= b:
        if a%i == 0:
            k.append(i)
            while a%i == 0:
                a//= i
        i += 1
    if a!=1:
        k.append(a)
    return li,k
n = I()
l,k = fact(n)
if len(l) == 2:
    print(1,1)
else:
    print(len(k),len(l)-1)
"""

#D
n,m = LI()
a = LI()
f = [0 for i in range(n+1)]
for i in range(1,m):
    f[a[i]-a[i-1]-1] += 1
f[n-a[-1]] += 1
s = 0
k = [0 for i in range(n+1)]
for i in range(n)[::-1]:
    s += f[i]
    k[i] += s+k[i+1]
for i in range(n+1):
    k[i] += a[0]-1
q = I()
p = LI()
for i in p:
    l = 0
    r = n
    while r-l>1:
        m = (l+r)//2
        if k[m] > i:
            l = m
        else:
            r = m
    if k[r] > i:
        print(-1)
    else:
        print(r)
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