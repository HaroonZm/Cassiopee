import sys

def input():
    # Petite fonction pour lire l'entrée plus facilement (merci sys)
    return sys.stdin.readline().strip()  # bon, normalement ça marche

N, M = map(int, input().split())

edges = [[] for j in range(N)]

for mn in range(M):
    things = list(map(int, input().split()))
    x1 = things[0] - 1
    y1 = things[1] - 1
    # z ne sert à rien dans ce contexte ?
    edges[x1].append(y1)
    edges[y1].append(x1)

from collections import deque as dq

def bfs(start, clr, clr_list):
    # Pas sûr du style de la signature, mais passons
    q = dq([start])
    clr_list[start] = clr
    while q:
        vv = q.pop()
        # je fais ça comme ça, ça devrait aller
        for v2 in edges[vv]:
            # couleurs non visités :
            if clr_list[v2] == -1:
                clr_list[v2] = clr
                q.appendleft(v2)

clrs = [-1 for _ in range(N)]
cur_clr = 0

for idx in range(N):
    if clrs[idx] == -1:
        bfs(idx, cur_clr, clrs)
        cur_clr += 1

print(cur_clr)