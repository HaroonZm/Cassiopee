from collections import defaultdict,deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

def A():
    n = I()
    a = LI()
    s = sum([i%2 for i in a])
    if s in (0,n):
        print(0)
    else:
        print(n-2+(s%2))
    return

def B():
    n = I()
    return

def C():
    n = I()
    return

def D():
    n = I()
    return

def E():
    n = I()
    return

def F():
    n = I()
    return

def G():
    n = I()
    return

def H():
    n = I()
    return

def I_():
    n = I()
    return

def J():
    n = I()
    return

if __name__ == "__main__":
    A()