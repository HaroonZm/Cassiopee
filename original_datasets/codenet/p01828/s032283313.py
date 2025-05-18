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
    for i in range(n):l[i] = LS()
    return l
sys.setrecursionlimit(1000000)
mod = 1000000007

#A
def A():
    n = I()
    s = 0
    ans = "YES"
    for i in range(n):
        k = input()
        if k == "Un":
            s -= 1
        else:
            s += 1
        if s < 0:
            ans = "NO"
    if s:
        print("NO")
    else:
        print(ans)
    return

#B
def B():
    s = S()
    t = S()
    n = len(s)
    t_ = [s[i*2] for i in range(n//2)]
    j = 0
    if not t_:
        print("Yes")
        quit()
    for i in range(n):
        if t_[j] == t[i]:
            j += 1
            if j == len(t_):
                print("Yes")
                quit()
    t_ = [s[i*2+1] for i in range(n//2)]
    j = 0
    if not t_:
        print("Yes")
        quit()
    for i in range(n):
        if t_[j] == t[i]:
            j += 1
            if j == len(t_):
                print("Yes")
                quit()
    print("No")
    return

#C
def C():
    n,q = LI()
    p = LIR(n)
    for _ in range(q):
        x0,y0,z0,s,t,u = LI()
        a,b,c = (s-x0,t-y0,u-z0)
        ans = 0
        su = a**2+b**2+c**2
        for xr,yr,zr,r,l in p:
            x = (su-a**2)/su*x0-a/su*(b*y0+c*z0-a*xr-b*yr-c*zr)
            y = (su-b**2)/su*y0-b/su*(a*x0+c*z0-a*xr-b*yr-c*zr)
            z = (su-c**2)/su*z0-c/su*(b*y0+a*x0-a*xr-b*yr-c*zr)
            if min(x0,s)-1e-4 <= x <= max(x0,s)+1e-4 and min(y0,t)-1e-4 <= y <= max(y0,t)+1e-4 and min(z0,u)-1e-4 <= z <= max(z0,u)+1e-4:
                x -= xr
                y -= yr
                z -= zr
                r2 = x**2+y**2+z**2
                if r2 <= r**2+1e-4:
                    ans += l
        print(ans)
    return

#D
def D():
    return

#E
def E():
    return

#F
def F():
    return

#G
def G():
    return

#H
def H():
    return

#I
def I_():
    return

#J
def J():
    return

#Solve
if __name__ == "__main__":
    B()