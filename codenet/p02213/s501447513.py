#!/usr/bin/env python3
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

h, w = map(int, input().split())
edge = [[] for _ in range(8 * w * h)]
field = []
for _ in range(h):
    line = input().rstrip()
    field.append(line)
if field[h-1][w-1] == "#":
    print("NO")
    exit()

def get_index(x, y, state):
    return x * w * 8 + y * 8 + state 

def get_place(index):
    x = index // (w * 8)
    index %= (w * 8)
    y = index // 8
    index %= 8
    state = index
    return x, y, state

if h % 2 == 0 and w % 2 == 0:
    print("NO")
    exit()
# 1: (2,3), (3,5), (5,4), (4,2) 
# 6: (5,3), (3,2), (2,4), (4,5) 
for x in range(h):
    for y in range(w):
        if field[x][y] in "#16":
            continue
        # Up - Down
        if x % 2 == 1 and y % 2 == 0 and x + 1 < h:
            if field[x-1][y] not in "#2345" and field[x+1][y] not in "#2345" and int(field[x-1][y]) + int(field[x+1][y]) == 7:
                path = int(field[x][y])
                # 0 -> 4, 6 -> 2
                if path == 2:
                    edge[get_index(x-1, y, 0)].append(get_index(x+1, y, 4))
                    edge[get_index(x-1, y, 6)].append(get_index(x+1, y, 2))
                    edge[get_index(x+1, y, 4)].append(get_index(x-1, y, 0))
                    edge[get_index(x+1, y, 2)].append(get_index(x-1, y, 6))
                # 1 -> 7, 5 -> 3
                if path == 3:
                    edge[get_index(x-1, y, 1)].append(get_index(x+1, y, 7))
                    edge[get_index(x-1, y, 5)].append(get_index(x+1, y, 3))
                    edge[get_index(x+1, y, 7)].append(get_index(x-1, y, 1))
                    edge[get_index(x+1, y, 3)].append(get_index(x-1, y, 5))
                # 3 -> 5, 7 -> 1
                if path == 4:
                    edge[get_index(x-1, y, 3)].append(get_index(x+1, y, 5))
                    edge[get_index(x-1, y, 7)].append(get_index(x+1, y, 1))
                    edge[get_index(x+1, y, 5)].append(get_index(x-1, y, 3))
                    edge[get_index(x+1, y, 1)].append(get_index(x-1, y, 7))
                # 2 -> 6, 4 -> 0
                if path == 5:
                    edge[get_index(x-1, y, 2)].append(get_index(x+1, y, 6))
                    edge[get_index(x-1, y, 4)].append(get_index(x+1, y, 0))
                    edge[get_index(x+1, y, 6)].append(get_index(x-1, y, 2))
                    edge[get_index(x+1, y, 0)].append(get_index(x-1, y, 4))
        # Right - Left
        if x % 2 == 0 and y % 2 == 1 and y + 1 < w:
            if field[x][y-1] not in "#2345" and field[x][y+1] not in "#2345" and int(field[x][y-1]) + int(field[x][y+1]) == 7:
                path = int(field[x][y])
                # 3 -> 7, 5 -> 1
                if path == 2:
                    edge[get_index(x, y-1, 3)].append(get_index(x, y+1, 7))
                    edge[get_index(x, y-1, 5)].append(get_index(x, y+1, 1))
                    edge[get_index(x, y+1, 7)].append(get_index(x, y-1, 3))
                    edge[get_index(x, y+1, 1)].append(get_index(x, y-1, 5))
                # 7 -> 3, 1 -> 5
                if path == 5:
                    edge[get_index(x, y-1, 7)].append(get_index(x, y+1, 3))
                    edge[get_index(x, y-1, 1)].append(get_index(x, y+1, 5))
                    edge[get_index(x, y+1, 3)].append(get_index(x, y-1, 7))
                    edge[get_index(x, y+1, 5)].append(get_index(x, y-1, 1))
                # 0 -> 6, 4 -> 2
                if path == 3:
                    edge[get_index(x, y-1, 0)].append(get_index(x, y+1, 6))
                    edge[get_index(x, y-1, 4)].append(get_index(x, y+1, 2))
                    edge[get_index(x, y+1, 6)].append(get_index(x, y-1, 0))
                    edge[get_index(x, y+1, 2)].append(get_index(x, y-1, 4))
                # 6 -> 0, 2 -> 4
                if path == 4:
                    edge[get_index(x, y-1, 6)].append(get_index(x, y+1, 0))
                    edge[get_index(x, y-1, 2)].append(get_index(x, y+1, 4))
                    edge[get_index(x, y+1, 0)].append(get_index(x, y-1, 6))
                    edge[get_index(x, y+1, 4)].append(get_index(x, y-1, 2))

visited = [False] * (8 * w * h)
def dfs(start):
    visited[start] = True
    for nv in edge[start]:
        if not visited[nv]:
            dfs(nv)
dfs(0)

if h % 2 == 1 and w % 2 == 1:
    ok = False
    for i in range(8):
        if visited[get_index(h-1, w-1, i)]:
            ok = True
    if ok:
        print("YES")
        exit()
    else:
        print("NO")
elif h % 2 == 0:
    if int(field[h-1][w-1]) == 2:
        if visited[get_index(h-2, w-1, 0)] or visited[get_index(h-2, w-1, 6)]:
            print("YES")
        else:
            print("NO")
    elif int(field[h-1][w-1]) == 3:
        if visited[get_index(h-2, w-1, 1)] or visited[get_index(h-2, w-1, 5)]:
            print("YES")
        else:
            print("NO")
    elif int(field[h-1][w-1]) == 4:
        if visited[get_index(h-2, w-1, 3)] or visited[get_index(h-2, w-1, 7)]:
            print("YES")
        else:
            print("NO")
    elif int(field[h-1][w-1]) == 5:
        if visited[get_index(h-2, w-1, 2)] or visited[get_index(h-2, w-1, 4)]:
            print("YES")
        else:
            print("NO")
elif w % 2 == 0:
    if int(field[h-1][w-1]) == 2:
        if visited[get_index(h-1, w-2, 3)] or visited[get_index(h-1, w-2, 5)]:
            print("YES")
        else:
            print("NO")
    elif int(field[h-1][w-1]) == 3:
        if visited[get_index(h-1, w-2, 0)] or visited[get_index(h-1, w-2, 4)]:
            print("YES")
        else:
            print("NO")
    elif int(field[h-1][w-1]) == 4:
        if visited[get_index(h-1, w-2, 2)] or visited[get_index(h-1, w-2, 6)]:
            print("YES")
        else:
            print("NO")
    elif int(field[h-1][w-1]) == 5:
        if visited[get_index(h-1, w-2, 1)] or visited[get_index(h-1, w-2, 7)]:
            print("YES")
        else:
            print("NO")
else:
    print("NO")