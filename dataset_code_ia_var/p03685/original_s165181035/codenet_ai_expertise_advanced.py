import os
import sys
from collections import deque, Counter

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10**9)
INF, IINF, MOD = float("inf"), 10**18, 10**9+7

R, C, N = map(int, sys.stdin.readline().split())
XY = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

# Utilisation d'une dict de listes pour factoriser la collecte des points
from itertools import chain

edges = [[], [], [], []]
edge_indices = [
    lambda x, y: y == 0,      # bas
    lambda x, y: x == R,      # droite
    lambda x, y: y == C,      # haut
    lambda x, y: x == 0       # gauche
]
selectors = [(lambda x1, y1, x2, y2: (x1, y1)), (lambda x1, y1, x2, y2: (x2, y2))]

for idx, (x1, y1, x2, y2) in enumerate(XY):
    for x, y in ((x1, y1), (x2, y2)):
        for e, cond in enumerate(edge_indices):
            if cond(x, y):
                edges[e].append(((y if e % 2 else x), idx))
                break

edges[0].sort()                 # bas : croissant x
edges[1].sort()                 # droite : croissant y
edges[2].sort(reverse=True)     # haut : décroissant x
edges[3].sort(reverse=True)     # gauche : décroissant y

# Construction de la liste ordonnée des sommets du bord
points = list(chain.from_iterable(edges))

count = Counter(i for _, i in points)
que = deque()

for _, i in points:
    if count[i] == 1:
        continue
    if que and que[-1] == i:
        que.pop()
    else:
        que.append(i)

while len(que) >= 2 and que[0] == que[-1]:
    que.popleft()
    que.pop()

print('YES' if not que else 'NO')