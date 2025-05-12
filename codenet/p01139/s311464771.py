#!/usr/bin/env python

import sys
sys.setrecursionlimit(10**6)

def dfs(x, y, symbol,land):
    if land[y][x] != '.':
        return ([land[y][x]] if not str(land[y][x]).isnumeric() else False), 0
    land[y][x] = symbol
    count = 1
    dxdy = [(1,0),(-1,0),(0,1),(0,-1)]

    owner_list = []
    for dx,dy in dxdy:
        if 0 <= x + dx < len(land[0]) and 0 <= y + dy < len(land):
            ret,c = dfs(x + dx, y + dy, symbol,land)
            count += c

            if ret is not False:
                owner_list += ret
    return (list(set(owner_list)), count)

while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    land = [list(input()) for i in range(0,h)]

    symbol = 0
    count_dict = {'W' :0, 'B' :0}

    for y in range(h):
        for x in range(w):
            if land[y][x] == '.':
                ret, count = dfs(x,y,symbol,land)
                if len(ret) == 1:
                    count_dict[ret[0]] += count
                symbol += 1
    print(count_dict['B'],count_dict['W'])