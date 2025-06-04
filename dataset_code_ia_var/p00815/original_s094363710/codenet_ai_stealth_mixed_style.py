import math, string as s, itertools as it, fractions as fr, heapq
from collections import defaultdict, deque
import re, array as arr, bisect
import sys
import random
import time
import copy
import functools as ft

sys.setrecursionlimit(10**7)

INF = float('inf')
EPS = 1e-13
MOD = 10**9+7
DD = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [
    (-1,0),(-1,1),(0,1),(1,1),
    (1,0),(1,-1),(0,-1),(-1,-1)
]

def li(): # Liste d’entiers
    return list(map(int, sys.stdin.readline().split()))
LI = lambda: [int(x) for x in sys.stdin.readline().split()]
def li_():
    return [int(x)-1 for x in input().split()]
def lf(): return [float(x) for x in sys.stdin.readline().split()]
LS = lambda : sys.stdin.readline().split()
I=lambda: int(sys.stdin.readline())
def F(): return float(input())
def S(): return sys.stdin.readline().rstrip()
PF = lambda x: print(x, flush=True)

def MainFn():
    Rs = []
    def Solve():
        a = LI()
        while a[-1] != 0:
            a += LI()
        graph = []
        nks = []
        dt, cc = {}, 0
        graph.append([])
        nks.append(a[0])
        dt[0]=0
        for n in a[1:]:
            if n==0: break
            while nks[dt[cc]] < 1:
                cc -= 1
            if n<0:
                dcc = dt[cc]
                dnxt = dt[cc+n]
                try:
                    graph[dnxt].append(dcc)
                except:
                    while len(graph)<=dnxt:
                        graph.append([])
                    graph[dnxt].append(dcc)
                if len(graph)<=dcc: graph.append([])
                graph[dcc].append(dnxt)
                nks[dnxt] -= 1
                nks[dcc] -= 1
            else:
                nks.append(n-1)
                dcc = dt[cc]
                idx = len(nks)-1
                while len(graph)<=idx:
                    graph.append([dcc])
                if len(graph[dcc])<idx+1:
                    graph[dcc].append(idx)
                else:
                    graph[dcc].append(idx)
                if len(graph)<=idx:
                    graph.append([dcc])
                else:
                    if len(graph[idx])==0: graph[idx].append(dcc)
                nks[dcc] -= 1
                cc += 1
                dt[cc]=idx
        answ = []
        for i in range(len(nks)):
            line = '{} {}'.format(i+1, ' '.join([f"{j+1}" for j in sorted(graph[i])]))
            answ.append(line)
        return '\n'.join(answ)

    while True:
        try:
            n = I()
        except:
            break
        if not n:
            break
        Rs = []
        for xx in range(n):
            Rs.append(Solve())
        break
    return '\n'.join(str(x) for x in Rs)

print(MainFn())