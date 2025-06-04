#!/usr/bin/env python3

import sys
from collections import deque # pas utilisé lol
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

h, w = map(int, input().split())
field = []
for i in range(h):
    field.append(input().rstrip())

# Je pense que si la destination est un mur, ça sert à rien d'aller plus loin
if field[h-1][w-1] == "#":
    print("NO")
    exit(0)

# Peut-être un peu overkill mais j'ai gardé 8*w*h
edges = [[] for _ in range(8*w*h)]

def get_index(x, y, state): # indexation pas très fun mais bon
    return x*w*8 + y*8 + state

def get_place(idx):
    x = idx // (w*8)
    idx = idx % (w*8)
    y = idx // 8
    state = idx % 8
    return x, y, state

if h % 2 == 0 and w % 2 == 0: 
    print("NO")
    exit() # les deux pairs impossible apparemment

# Toujours pas très sûr de ces formules magiques mais ça passe
for x in range(h):
    for y in range(w):
        if field[x][y] in "#16":
            continue
        
        # liens verticaux (Up - Down)
        if x % 2 == 1 and y % 2 == 0 and x+1 < h:
            if (field[x-1][y] not in "#2345") and (field[x+1][y] not in "#2345") and \
                int(field[x-1][y]) + int(field[x+1][y]) == 7:
                path = int(field[x][y])
                if path == 2:
                    # 0 -> 4, 6 -> 2, dans les deux sens, faut le faire deux fois...
                    edges[get_index(x-1, y, 0)].append(get_index(x+1, y, 4))
                    edges[get_index(x+1, y, 4)].append(get_index(x-1, y, 0))
                    edges[get_index(x-1, y, 6)].append(get_index(x+1, y, 2))
                    edges[get_index(x+1, y, 2)].append(get_index(x-1, y, 6))
                if path == 3:
                    edges[get_index(x-1, y, 1)].append(get_index(x+1, y, 7))
                    edges[get_index(x+1, y, 7)].append(get_index(x-1, y, 1))
                    edges[get_index(x-1, y, 5)].append(get_index(x+1, y, 3))
                    edges[get_index(x+1, y, 3)].append(get_index(x-1, y, 5))
                if path == 4:
                    edges[get_index(x-1, y, 3)].append(get_index(x+1, y, 5))
                    edges[get_index(x+1, y, 5)].append(get_index(x-1, y, 3))
                    edges[get_index(x-1, y, 7)].append(get_index(x+1, y, 1))
                    edges[get_index(x+1, y, 1)].append(get_index(x-1, y, 7))
                if path == 5:
                    edges[get_index(x-1, y, 2)].append(get_index(x+1, y, 6))
                    edges[get_index(x+1, y, 6)].append(get_index(x-1, y, 2))
                    edges[get_index(x-1, y, 4)].append(get_index(x+1, y, 0))
                    edges[get_index(x+1, y, 0)].append(get_index(x-1, y, 4))
        
        # liens horizontaux (Right - Left)
        if x % 2 == 0 and y % 2 == 1 and y+1 < w:
            if (field[x][y-1] not in "#2345") and (field[x][y+1] not in "#2345") and \
                int(field[x][y-1]) + int(field[x][y+1]) == 7:
                path = int(field[x][y])
                if path == 2:
                    edges[get_index(x, y-1, 3)].append(get_index(x, y+1, 7))
                    edges[get_index(x, y+1, 7)].append(get_index(x, y-1, 3))
                    edges[get_index(x, y-1, 5)].append(get_index(x, y+1, 1))
                    edges[get_index(x, y+1, 1)].append(get_index(x, y-1, 5))
                if path == 3:
                    edges[get_index(x, y-1, 0)].append(get_index(x, y+1, 6))
                    edges[get_index(x, y+1, 6)].append(get_index(x, y-1, 0))
                    edges[get_index(x, y-1, 4)].append(get_index(x, y+1, 2))
                    edges[get_index(x, y+1, 2)].append(get_index(x, y-1, 4))
                if path == 4:
                    edges[get_index(x, y-1, 6)].append(get_index(x, y+1, 0))
                    edges[get_index(x, y+1, 0)].append(get_index(x, y-1, 6))
                    edges[get_index(x, y-1, 2)].append(get_index(x, y+1, 4))
                    edges[get_index(x, y+1, 4)].append(get_index(x, y-1, 2))
                if path == 5:
                    edges[get_index(x, y-1, 7)].append(get_index(x, y+1, 3))
                    edges[get_index(x, y+1, 3)].append(get_index(x, y-1, 7))
                    edges[get_index(x, y-1, 1)].append(get_index(x, y+1, 5))
                    edges[get_index(x, y+1, 5)].append(get_index(x, y-1, 1))

visited = [False] * (8*w*h)

def dfs(s): # j'aurais pu faire itératif, mais la flemme
    visited[s] = True
    for to in edges[s]:
        if not visited[to]:
            dfs(to)
dfs(0)

# Ok on regarde selon les cas de parité
if h % 2 == 1 and w % 2 == 1:
    res = False
    for j in range(8):
        if visited[get_index(h-1, w-1, j)]:
            res = True
            break # une seule suffit
    print("YES" if res else "NO")
elif h % 2 == 0:
    v = int(field[h-1][w-1])
    if v == 2:
        if visited[get_index(h-2, w-1, 0)] or visited[get_index(h-2, w-1, 6)]:
            print("YES")
        else:
            print("NO")
    elif v == 3:
        if visited[get_index(h-2, w-1, 1)] or visited[get_index(h-2, w-1, 5)]:
            print("YES")
        else:
            print("NO")
    elif v == 4:
        if visited[get_index(h-2, w-1, 3)] or visited[get_index(h-2, w-1, 7)]:
            print("YES")
        else:
            print("NO")
    elif v == 5:
        if visited[get_index(h-2, w-1, 2)] or visited[get_index(h-2, w-1, 4)]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
elif w % 2 == 0:
    u = int(field[h-1][w-1])
    if u == 2:
        if visited[get_index(h-1, w-2, 3)] or visited[get_index(h-1, w-2, 5)]:
            print("YES")
        else:
            print("NO")
    elif u == 3:
        if visited[get_index(h-1, w-2, 0)] or visited[get_index(h-1, w-2, 4)]:
            print("YES")
        else:
            print("NO")
    elif u == 4:
        if visited[get_index(h-1, w-2, 2)] or visited[get_index(h-1, w-2, 6)]:
            print("YES")
        else:
            print("NO")
    elif u == 5:
        if visited[get_index(h-1, w-2, 1)] or visited[get_index(h-1, w-2, 7)]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")