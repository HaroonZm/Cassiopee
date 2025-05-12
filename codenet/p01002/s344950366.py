import itertools
from collections import defaultdict, deque
from copy import deepcopy
ml = [[0,1],[0,-1],[-1,0],[1,0]]
def main(n):
    def move(fi,mli,y,x):
        f = deepcopy(fi)
        for mi in mli:
            mx,my = ml[mi]
            mx += x
            my += y
            if 0 <= mx <= 4 and 0 <= my <= 4:
                f[y][x], f[my][mx] = f[my][mx], f[y][x]
                x, y = mx, my
            else:
                return False
        return f

    def d(b):
        a = 0
        de = []
        for y in range(5):
            for x in range(5):
                if c[y][x]:
                    val = c[y][x]
                    if y == 4 or y == 0:
                        if x == 4 or x == 0:
                            continue
                        if c[y][x+1] == c[y][x-1] == c[y][x]:
                            de.append((y,x, 0))
                    else:
                        if x == 4 or x == 0:
                            if c[y+1][x] == c[y-1][x] == c[y][x]:
                                de.append((y,x, 1))
                            continue
                        else:
                            if c[y][x+1] == c[y][x-1] == c[y][x]:
                                de.append((y,x, 0))
                            if c[y+1][x] == c[y-1][x] == c[y][x]:
                                de.append((y,x, 1))
        for y,x,di in de:
            for i in range(3):
                if di:
                    if c[y+i-1][x]:
                        a += score[c[y+i-1][x]-1] * b
                        c[y+i-1][x] = 0
                else:
                    if c[y][x-1+i]:
                        a += score[c[y][x-1+i]-1] * b
                        c[y][x-1+i] = 0
        if fall():
            a += d(b+1)
        return a

    def fall():
        f = False
        for x in range(5):
            for y in range(3,-1,-1):
                if c[y][x] and c[y+1][x] == 0:
                    for yi in range(y+1,5):
                        if c[yi][x] == 0:
                             continue
                        yi -= 1
                        break
                    c[yi][x],c[y][x] = c[y][x],c[yi][x]
                    f = True
        return f

    ans = 0
    field = [list(map(int, input().split())) for i in range(5)]
    score = list(map(int, input().split()))
    for i in range(n+1):
        mlis = list(itertools.product(range(4),repeat = i))
        for mli in mlis:
            for y in range(5):
                for x in range(5):
                    c = move(field, mli, y, x)
                    if c:
                        ans = max(ans,d(1))
    print(ans)

while 1:
    n = int(input())
    if n == -1:
        break
    main(n)