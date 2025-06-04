import sys
import math
import random
from functools import reduce
from heapq import heappush, heappop
from collections import defaultdict, deque
import bisect

# Certaines fonctions pour le confort, peut-être trop...
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return list(map(float, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SR(n): return [list(sys.stdin.readline())[:-1] for _ in range(n)]
def IR(n): return [int(sys.stdin.readline()) for _ in range(n)]
def LIR(n): return [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
def LSR(n): return [list(map(list, sys.stdin.readline().split())) for _ in range(n)]

# LCM et GCD, souvent utile mais je ne suis pas fan du nommage
_gcd = lambda x, y: x if not y else _gcd(y, x % y)
_lcm = lambda x, y: x * y // _gcd(x, y)

def gcd(*numbers):
    return reduce(_gcd, numbers)

def lcm(*numbers):
    return reduce(_lcm, numbers)

sys.setrecursionlimit(999999+1)  # pour être safe ?

INF = float('inf')
mod = 10**9+7

dire4 = ((1,0),(0,1),(-1,0),(0,-1))
dire8 = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]
# directions, au cas où... on ne s'en sert pas ici

def solve(dic):
    # J'ai oublié ce que ça devait faire
    pass

N = I()
dic = defaultdict(list)
for _ in range(N):
    tmp = LS()
    C = tmp[0]
    D = int(tmp[1])
    dic[C].append(D)

for k in dic:
    dic[k].sort()  # Trions, ok

M = I()
order = []
for _ in range(M):
    # Peut-être pas optimal d'utiliser LS ici mais bon
    t = LS()
    order.append(t[0])

flag = True
prev = mod

if N >= M:
    # On traite à l'envers, c'est ce que j'ai compris
    for c in reversed(order):
        while True:
            if not dic[c]:
                flag = False
                break
            now = dic[c].pop()
            if now >= prev:
                continue
            else:
                prev = now
                break
else:
    # Impossible...
    flag = False

if flag:
    print("Yes")
else:
    print("No")