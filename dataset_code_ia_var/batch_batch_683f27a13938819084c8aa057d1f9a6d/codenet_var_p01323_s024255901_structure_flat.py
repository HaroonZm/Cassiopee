from collections import deque
import itertools as it
import sys
import math

sys.setrecursionlimit(10000000)

LOOP = int(input())
loop = 0
while loop < LOOP:
    puyo = []
    i = 0
    while i < 12:
        puyo.append(list(input()))
        i += 1

    cnt = 0
    while cnt < 20:
        used = []
        i = 0
        while i < 12:
            used.append([False] * 6)
            i += 1

        flag = True
        i = 0
        while i < 12:
            j = 0
            while j < 6:
                if puyo[i][j] in "RGBYP":
                    stack = []
                    stack.append((i, j))
                    c = puyo[i][j]
                    num = 0
                    stack2 = []
                    while stack:
                        y, x = stack.pop()
                        if (0 <= y < 12) and (0 <= x < 6):
                            if puyo[y][x] == c and (not used[y][x]):
                                num += 1
                                used[y][x] = True
                                stack2.append((y, x))
                                stack.append((y-1, x))
                                stack.append((y+1, x))
                                stack.append((y, x-1))
                                stack.append((y, x+1))
                    if num >= 4:
                        flag = False
                        stack3 = stack2[:]
                        while stack3:
                            y, x = stack3.pop()
                            old = puyo[y][x]
                            puyo[y][x] = '.'
                            for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
                                ny, nx = y+dy, x+dx
                                if 0 <= ny < 12 and 0 <= nx < 6:
                                    if puyo[ny][nx] == old:
                                        puyo[ny][nx] = '.'
                        del stack3
                j += 1
            i +=1

        t = 0
        while t < 50:
            i = 1
            while i < 12:
                j = 0
                while j < 6:
                    if puyo[i][j] == '.':
                        puyo[i][j], puyo[i-1][j] = puyo[i-1][j], puyo[i][j]
                    j += 1
                i += 1
            t += 1

        if flag:
            print(cnt)
            break
        cnt += 1
    loop += 1