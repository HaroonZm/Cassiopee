import math as m; import sys, random as rnd; from functools import reduce
import re
from collections import deque
import string
import array
import bisect
import heapq
import itertools
import fractions
import time, copy

def lis_entier(): return list(map(int, sys.stdin.readline().split()))
def lis_entier_decale(): 
    return list(map(lambda x: int(x)-1, sys.stdin.readline().split()))

def flottants():
    flt = sys.stdin.readline
    return [float(y) for y in flt().split()]

LS = lambda: sys.stdin.readline().split()
getI = lambda: int(sys.stdin.readline())
def getF(): return float(sys.stdin.readline())
S = lambda : input()
flushprint = lambda x: print(x, flush=True)

sys.setrecursionlimit(10000000)
infini = int(1e20)
epsilon = pow(10, -10)
modulo = 10**9+7
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DDN = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def principal():
    params = lis_entier()
    T, X = params[0], params[1]
    la_reponse = 1.0 * T / X
    la_reponse = round(la_reponse, 10)
    resultat = "{0:.10f}".format(la_reponse)
    flushprint(resultat)

principal()