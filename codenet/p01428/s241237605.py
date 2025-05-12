from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime,time

MAP = [list('z' + input() + 'z') for _ in range(8)]
MAP = [list('z'*10)] + MAP + [list('z'*10)]

def check(x0,y0,turn):
    if MAP[y0][x0] != '.':
        return 0, []

    if turn:
        me,you = 'o','x'
    else:
        me,you = 'x','o'

    ans = 0
    dx = [-1, 0, 1,-1, 1,-1, 0, 1]
    dy = [-1,-1,-1, 0, 0, 1, 1, 1]
    rev = []
    for i in range(8):
        x,y = x0,y0
        cnt = 0
        tmprev = []
        while True:
            x += dx[i]
            y += dy[i]
            if MAP[y][x] == you:
                tmprev.append([x,y])
                cnt += 1
                continue
            elif MAP[y][x] == me:
                break
            else:
                cnt = 0
                tmprev = []
                break
        ans += cnt
        rev = tmprev + rev
    return ans,rev

btmp = -1
turn = True
while True:
    maxtmp = 0
    maxrev = []
    my = []
    ra = list(range(1,9))
    if not turn:
        ra = list(reversed(ra))

    #print(turn,ra)
    for y in ra:
        for x in ra:
            #print(turn,x,y)
            tmp,rev = check(x,y,turn)
            if maxtmp < tmp:
                maxtmp = tmp
                maxrev = rev[:]
                my = [x,y]

    if my:
        if turn:
            MAP[my[1]][my[0]] = 'o'
        else:
            MAP[my[1]][my[0]] = 'x'

    for x,y in maxrev:
        if MAP[y][x] == 'o':
            MAP[y][x] = 'x'
        else:
            MAP[y][x] = 'o'

    #print(maxtmp,my,rev)

    #for m in MAP:
    #    print(''.join(m))

    if btmp == 0 and maxtmp == 0:
        break

    btmp = maxtmp
    turn = not turn

for y in range(1,9):
    print(''.join(MAP[y][1:9]))