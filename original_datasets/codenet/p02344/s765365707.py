#!usr/bin/env python3
from collections import defaultdict
from collections import deque
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
sys.setrecursionlimit(1000000)
mod = 1000000007

#1:set
#1_A
"""
n,q = map(int, input().split(" "))
group = [[i] for i in range(n)]
key = [i for i in range(n)]
for i in range(q):
    com, x, y = map(int, input().split(" "))
    if com == 0:
        if key[x] != key[y]:
            v = key[y]
            group[key[x]] = group[key[x]] + group[key[y]]
            for j in group[v]:
                key[j] = key[x]
            group[v] = []
    if com == 1:
        if key[x] == key[y]:
            print(1)
        else:
            print(0)
"""

#1_B 重み付きunionfind
def root(x):
    if par[x] == x:
        return x
    r = root(par[x])
    w[x] += w[par[x]]
    par[x] = r
    return par[x]

def same(x,y):
    return root(x) == root(y)

def unite(x,y,z):
    z += w[x]-w[y]
    x = root(x)
    y = root(y)
    if rank[x] < rank[y]:
        par[x] = y
        w[x] = -z
    else:
        par[y] = x
        w[y] = z
        if rank[x] == rank[y]:
            rank[x] += 1
n,Q = LI()
par = [i for i in range(n)]
rank = [0 for i in range(n)]
w = [0 for i in range(n)]
for _ in range(Q):
    q = LI()
    if q[0]:
        x,y = q[1],q[2]
        if same(x,y):
            print(w[y]-w[x])
        else:
            print("?")
    else:
        x,y,z = q[1:]
        if not same(x,y):
            unite(x,y,z)
#2:range quary
#2_A rmq
"""
def rmq(a,b,k,l,r):
    if r <= a or b <= l:
        return inf
    if a <= l and r <= b:
        return st[k]
    vl = rmq(a,b,2*k+1,l,(l+r)//2)
    vr = rmq(a,b,2*k+2,(l+r)//2,r)
    return min(vl,vr)

n,Q = LI()
n1 = 1
while n1 <= n:
    n1 *= 2
n = n1
inf = pow(2,31)-1
st = [inf for i in range(2*n-1)]
for _ in range(Q):
    q = LI()
    if not q[0]:
        x,y = q[1:]
        i = n+x-1
        st[i] = y
        while i > 0:
            i = (i-1)//2
            st[i] = min(st[2*i+1],st[2*i+2])
    else:
        a,b = q[1:]
        print(rmq(a,b+1,0,0,n))
"""

#2_B rsq
"""
def rsq(a,b,k,l,r):
    if r <= a or b <= l:
        return 0
        if a <= l and r <= b:
            return st[k]
            vl = rsq(a,b,2*k+1,l,(l+r)//2)
            vr = rsq(a,b,2*k+2,(l+r)//2,r)
            return vl+vr

            n,Q = LI()
            n1 = 1
            while n1 <= n:
                n1 *= 2
                n = n1
                st = [0 for i in range(2*n-1)]
                for _ in range(Q):
                    q = LI()
                    if not q[0]:
                        x,y = q[1:]
                        i = n+x-1
                        st[i] += y
                        while i > 0:
                            i = (i-1)//2
                            st[i] += y
                        else:
                            a,b = q[1:]
                            print(rsq(a,b+1,0,0,n))
"""
#2_C

#2_D
"""
def ruq(a,b,k,l,r,z):
    if r <= a or b <= l:
        return
    if a <= l and r <= b:
        st[k] = z
        return
    vl = ruq(a,b,2*k+1,l,(l+r)//2,z)
    vr = ruq(a,b,2*k+2,(l+r)//2,r,z)
    return

n,Q = LI()
n1 = 1
while n1 <= n:
    n1 *= 2
n = n1
d = pow(2,31)-1
st = [d for i in range(2*n-1)]
for _ in range(Q):
    q = LI()
    if not q[0]:
        x,y,z = q[1:]
        ruq(x,y+1,0,0,n,z)
    else:
"""
#2_E

#2_F

#2_G

#2_H

#2_I

#3:sliding window
#3_A
"""
n,s = MI()
a = LI()
for i in range(1,n):
    a[i] += a[i-1]
a.insert(0,0)
l = 0
r = 0
ans = float("inf")
if a[1] >= s:
    print(1)
    quit()
while r < n:
    r += 1
    if a[r]-a[l] >= s:
        while a[r]-a[l] >= s and l < r:
            l += 1
        ans = min(ans, r-l+1)
if ans == float("inf"):
    print(0)
    quit()
print(ans)
"""

#3_B
"""
n,k = MI()
a = LI()
l = 0
r = 0
ans = float("inf")
fl = [0 for i in range(k+1)]
s = 0
if k == 1 and a[0] == 1:
    print(1)
    quit()
if a[0] <= k:
    fl[a[0]] = 1
    s = 1
while r < n-1:
    r += 1
    if a[r] <= k:
        if not fl[a[r]]:
            s += 1
        fl[a[r]] += 1
    if s == k:
        while s == k:
            l += 1
            if a[l-1] <= k:
                if fl[a[l-1]] == 1:
                    s -= 1
                fl[a[l-1]] -= 1
        ans = min(ans, r-l+2)
if ans == float("inf"):
    print(0)
    quit()
print(ans)
"""

#3_C
"""
n,q = LI()
a = LI()
x = LI()
for i in range(q):
    ans = 0
    r = -1
    s = 0
    for l in range(n):
        while r+1 < n and s+a[r+1] <= x[i]:
            r += 1
            s += a[r]
        if s <= x[i]:
            ans += r-l+1
        if l == r:
            r += 1
            if r < n:
                s += a[r]
        s -= a[l]
    print(ans)
"""

#3_D
"""
n,l = LI()
a = LI()
k = [0 for i in range(l)]
for i in range(l):
    k[i] = a[i]
k.sort()
ans = [k[0]]
for i in range(n-l):
    j = bisect.bisect_left(k,a[i])
    x = k.pop(j)
    j = bisect.bisect_left(k,a[l+i])
    k.insert(j,a[l+i])
    ans.append(k[0])
for i in range(len(ans)-1):
    print(ans[i],end = " ")
print(ans[-1])
"""

#4:coordinate compression
#4_A
"""
n = int(sys.stdin.readline())
d = defaultdict(int)
lx = []
ly = []
for i in range(n):
    x,y,s,t = map(int,sys.stdin.readline()[:-1].split())
    d[(x,y)] += 1
    d[(x,t)] -= 1
    d[(s,y)] -= 1
    d[(s,t)] += 1
    i = bisect.bisect_left(lx,x)
    if i >= len(lx) or lx[i] != x:
        lx.insert(i,x)
    i = bisect.bisect_left(ly,y)
    if i >= len(ly) or ly[i] != y:
        ly.insert(i,y)
    i = bisect.bisect_left(lx,s)
    if i >= len(lx) or lx[i] != s:
        lx.insert(i,s)
    i = bisect.bisect_left(ly,t)
    if i >= len(ly) or ly[i] != t:
        ly.insert(i,t)

for x in lx:
    for j in range((len(ly))-1):
        d[(x,ly[j+1])] += d[(x,ly[j])]
for y in ly:
    for i in range((len(lx))-1):
        d[(lx[i+1],y)] += d[(lx[i],y)]
ans = 0
for j in range(len(ly)-1):
    y = ly[j]
    p_y = ly[j+1]
    for i in range(len(lx)-1):
        x = lx[i]
        p_x = lx[i+1]
        if d[(x,y)] >= 1:
            ans += (p_y-y)*(p_x-x)
print(ans)
"""
#5:comulative sum
#5_A
"""
n,t = map(int, input().split(" "))
num = [0 for i in range(t)]
for i in range(n):
    l,r = map(int, input().split(" "))
    num[l] += 1
    if r < t:
        num[r] -= 1
for i in range(1,t):
    num[i] += num[i-1]
print(max(num))
"""

#5_B
"""
n = int(input())
lec = [[0 for i in range(1001)] for j in range(1001)]
max_x = 0
max_y = 0
for i in range(n):
    x,y,s,t = map(int, input().split(" "))
    lec[y][x] += 1
    lec[y][s] -= 1
    lec[t][x] -= 1
    lec[t][s] += 1
    max_x = max(max_x, s)
    max_y = max(max_y, t)

for i in range(max_y+1):
    for j in range(1, max_x+1):
        lec[i][j] += lec[i][j-1]

for i in range(1, max_y+1):
    for j in range(max_x+1):
        lec[i][j] += lec[i-1][j]

ans = 0
for i in range(max_y+1):
    for j in range(max_x+1):
        ans = max(ans, lec[i][j])

print(ans)
"""