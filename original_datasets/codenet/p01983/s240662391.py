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
    def parse_hash(s,i):
        if s[i] == "[":
            i += 1
            op,i = parse_op(s,i)
            h1,i = parse_hash(s,i)
            h2,i = parse_hash(s,i)
            i += 1
            return calc(op,h1,h2),i
        else:
            return parse_letter(s,i)

    def parse_op(s,i):
        return s[i],i+1

    def parse_letter(s,i):
        return s[i],i+1

    def calc(op,h1,h2):
        if op == "+":
            return h1|h2
        elif op == "*":
            return h1&h2
        else:
            return h1^h2

    while 1:
        s = S()
        if s[0] == ".":
            break
        t = S()
        n = len(s)
        s0 = [s[i] for i in range(n)]
        for i in range(n):
            if s0[i] == "a":
                s0[i] = int(t[0])
            elif s0[i] == "b":
                s0[i] = int(t[1])
            elif s0[i] == "c":
                s0[i] = int(t[2])
            elif s0[i] == "d":
                s0[i] = int(t[3])
        p = parse_hash(s0,0)[0]
        ans = 0
        for a in range(10):
            for b in range(10):
                for c in range(10):
                    for d in range(10):
                        s0 = [s[i] for i in range(n)]
                        for i in range(n):
                            if s0[i] == "a":
                                s0[i] = a
                            elif s0[i] == "b":
                                s0[i] = b
                            elif s0[i] == "c":
                                s0[i] = c
                            elif s0[i] == "d":
                                s0[i] = d
                        p0 = parse_hash(s0,0)[0]
                        if p == p0:
                            ans += 1
        print(p,ans)

    return

#B
def B():
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
    A()