from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
from functools import reduce
import operator
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]
def IR(n): return list(map(lambda _:I(), range(n)))
def LIR(n): return list(map(lambda _:LI(), range(n)))
def SR(n): return list(map(lambda _:S(), range(n)))
def LSR(n): return list(map(lambda _:LS(), range(n)))
sys.setrecursionlimit(10**6)
mod = 10**9+7

#A
def A():
    s = S()
    # Représente la direction comme une matrice de rotation complexe
    direction = complex(1, 0)
    tracker = [complex(1,0)]
    flag = [False]
    # Tourne de +i pour "R", -i pour "L"
    complex_map = {'R': complex(0,1), 'L': complex(0,-1)}
    # Il faut détecter chaque retour à l'est après au moins une rotation dans le sens positif
    states = []
    k = [False]
    ans = [0]
    def step(c, d, a, k):
        if c == 'R':
            if abs(d[0].real-1)<1e-7 and abs(d[0].imag)<1e-7:
                k[0] = True
            d[0] *= complex_map['R']
            if abs(d[0].real-1)<1e-7 and abs(d[0].imag)<1e-7 and k[0]:
                a[0] += 1
        else:
            if abs(d[0].real-1)<1e-7 and abs(d[0].imag)<1e-7:
                k[0] = False
            d[0] *= complex_map['L']
    list(map(lambda x: step(x, tracker, ans, k), s))
    print(ans[0])
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