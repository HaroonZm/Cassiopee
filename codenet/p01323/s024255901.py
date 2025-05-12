#!/usr/bin/env python

from collections import deque
import itertools as it
import sys
import math

sys.setrecursionlimit(10000000)

LOOP = input()
for loop in range(LOOP):
    puyo = []
    for i in range(12):
        puyo.append(list(raw_input()))
    
    for cnt in range(20):
        used = [[False] * 6 for i in range(12)]
        def func(y, x, c):
            if y < 0 or x < 0 or y >= 12 or x >= 6:
                return 0
            if puyo[y][x] != c or used[y][x]:
                return 0
            used[y][x] = True
            ret = 1
            ret += func(y - 1, x, c)
            ret += func(y + 1, x, c)
            ret += func(y, x - 1, c)
            ret += func(y, x + 1, c)
            return ret

        def erase(y, x, c):
            if y < 0 or x < 0 or y >= 12 or x >= 6:
                return
            if puyo[y][x] == 'O':
                puyo[y][x] = '.'
                return
            if puyo[y][x] != c:
                return
            puyo[y][x] = '.'
            erase(y - 1, x, c)
            erase(y + 1, x, c)
            erase(y, x - 1, c)
            erase(y, x + 1, c)

        flag = True
        for i in range(12):
            for j in range(6):
                if puyo[i][j] in "RGBYP":
                    num = func(i, j, puyo[i][j])
                    if num >= 4:
                        flag = False
                        erase(i, j, puyo[i][j])
        for t in range(50):
            for i in range(1, 12):
                for j in range(6):
                    if puyo[i][j] == '.':
                        puyo[i][j], puyo[i - 1][j] = puyo[i - 1][j], puyo[i][j]
        if flag:
            print cnt
            break