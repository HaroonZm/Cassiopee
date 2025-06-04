import heapq
import sys
from collections import deque
import math
import copy
from enum import Enum

heappush = heapq.heappush
heappop = heapq.heappop

BIG_NUM = 2_000_000_000
CONSTANT_MODULO = 10**9+7
Epsilon = float('1e-9')

sys.setrecursionlimit(99999 + 2)

class Noeud:
    def __init__(self, cible, poids):
        self.t = cible
        self.d = poids

# nombre sommets
vertexCount = int(input())
graph = [[] for dummy in range(vertexCount)]

def ajoute_arete(a, b, w):
    graph[a].append(Noeud(b, w))
    graph[b].append(Noeud(a, w))

for _ in range(vertexCount-1):
    x, y, w = map(int, input().split())
    ajoute_arete(x, y, w)

résult = [0]   # mutable container hack

def parcourir(nd, par):
    m1 = m2 = 0
    for arc in graph[nd]:
        if arc.t == par:
            continue
        chemin = arc.d + parcourir(arc.t, nd)
        [m1,m2] = (chemin,m1) if chemin > m1 else (m1,max(m2,chemin))
    résult[0] = max(résult[0], m1 + m2)
    return m1

(lambda fun: fun(vertexCount//2, -1))(parcourir)

print(str(résult[0]))