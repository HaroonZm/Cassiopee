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
    s = input()
    c = I()
    a = eval(s)
    b = int(s[0])
    n = len(s)
    if n == 1:
        if int(s[0]) == c:
            print("U")
        else:
            print("I")
        quit()
    key = 0 if s[1] == "+" else 1
    for i in range(2,n):
        if not i%2:
            if key:
                b *= int(s[i])
            else:
                b += int(s[i])
        else:
            key = 0 if s[i] == "+" else 1
    if a == b:
        if a == c:
            print("U")
        else:
            print("I")
    elif a == c:
        print("M")
    elif b == c:
        print("L")
    else:
        print("I")
    return

#B
def B():
    n,m = LI()
    t = [0 for i in range(2*n+3)]
    for i in range(m):
        a,b = LI()
        t[2*a] += 1
        t[2*b+1] -= 1
    for i in range(2*n+1):
        t[i+1] += t[i]
    ans = n+1
    s = 0
    key = 1
    for i in t:
        if i > 0:
            if key:
                key = 0
                s += 1
            ans += 1
        else:
            key = 1
    ans -= s
    print(ans)
    return

#C
def C():
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